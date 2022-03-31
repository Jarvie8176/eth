from __future__ import annotations

import csv
import json
import pathlib
from os import path
from typing import List, Tuple, TypedDict, Dict, Any

import numpy
from loguru import logger

from aggregator.price import PriceAggregator
from dto.TronGrid.transaction import TrxDto
from dto.failedTrx import FailedTrx
from dto.parsedTrx import ParsedTrx
from explorerClient.tron import TronGridExplorerClient
from models.exceptions import ParserNotFound, CurrencyNotFound, TransactionSkipped, InvalidTransaction
from parser.TronGrid.defn_parser import TronGrid_parser_lookup
from parser.parserLookup import ParserLookup


class TronGridRunnerOptions(TypedDict):
    input_file_path: str
    output_file_path: str
    trx_list_file_path: str
    api_client: TronGridExplorerClient
    parser_lookup: ParserLookup[TrxDto]
    price_aggregator: PriceAggregator


class TronGridRunnerCreateOptions(TypedDict):
    input_file_path: str
    output_file_path: str
    trx_list_file_path: str
    api_client_rpc_endpoint: str
    price_aggregator: PriceAggregator


class TronGridRunner:
    def __init__(self,
                 input_file_path: str, output_file_path: str,
                 trx_list_file_path: str,
                 api_client: TronGridExplorerClient,
                 parser_lookup: ParserLookup[TrxDto],
                 price_aggregator: PriceAggregator):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.trx_list_file_path = trx_list_file_path  # cache file
        self.api_client = api_client
        self.parser_lookup = parser_lookup
        self.price_aggregator = price_aggregator

        # results
        self.parsed_trxs: List[ParsedTrx] = []
        self.failed_trxs: List[FailedTrx] = []

    def to_dict(self) -> Dict[str, Any]:
        return {
            "parsed_trxs": self.parsed_trxs,
            "failed_trxs": self.failed_trxs,
        }

    @staticmethod
    def create(options: TronGridRunnerCreateOptions) -> TronGridRunner:
        api_client = TronGridExplorerClient.create(rpc_endpoint=options["api_client_rpc_endpoint"])
        parser_lookup = TronGrid_parser_lookup
        price_aggregator = options["price_aggregator"]

        return TronGridRunner(api_client=api_client,
                              parser_lookup=parser_lookup,
                              price_aggregator=price_aggregator,
                              input_file_path=options["input_file_path"],
                              output_file_path=options["output_file_path"],
                              trx_list_file_path=options["trx_list_file_path"])

    def run(self) -> None:
        trx_ids = self.load_input_file()
        logger.info(f"{len(trx_ids)} transactions loaded")

        transactions = self.load_trx(trx_ids)

        parsed_trxs, failed_trxs = self.parse_trx(transactions)
        self.aggregate_trx(parsed_trxs)
        logger.info("price data aggregated")

        self.parsed_trxs = parsed_trxs
        self.failed_trxs = failed_trxs

    def load_trx(self, trx_ids: List[str]) -> List[TrxDto]:
        trx_cache = {}
        # noinspection PyBroadException
        try:
            trx_cache = self.load_trx_from_cache()
            logger.info("cache loaded")
        except Exception:
            logger.opt(exception=True).debug("failed to load cache")

        result: List[TrxDto] = []
        for idx, trx_id in enumerate(trx_ids):
            cached_trx = trx_cache.get(trx_id)
            if cached_trx:
                result.append(cached_trx)
                logger.debug(f"({idx + 1}/{len(trx_ids)}) {trx_id}: loaded from cache")
            else:
                trx = self.api_client.get_transaction(trx_id)
                result.append(trx)
                self.save_trx_to_cache([trx], mode="a")
                logger.debug(f"({idx + 1}/{len(trx_ids)}) {trx_id}: saved to cache")

        return result

    def load_input_file(self) -> List[str]:
        """
        loads a list of transaction ids from inout file
        :return:
        """
        with open(self.input_file_path, "r") as f:
            input = csv.DictReader(f)
            result = list(map(lambda row: row.get("hash"), input))
            return result  # type: ignore

    def load_trx_from_cache(self) -> Dict[str, TrxDto]:
        logger.trace("load transactions from cache: begin")
        cache_file = self.trx_list_file_path
        with open(cache_file, 'r') as f_trx:
            rows = f_trx.readlines()
            cache = list(map(lambda line: TrxDto(**json.loads(line)), rows))
            cached_trx = {i.trx_id: i for i in cache}
            return cached_trx

    def save_trx_to_cache(self, trx_list: List[TrxDto], mode: str = "w") -> None:
        """
        writes a list of TrxDto to :param self.options.trx_list_file_path: as a csv file
        :param trx_list:
        :param mode:
        :return:
        """
        logger.trace("save transactions to cache: begin")

        if not len(trx_list):
            return

        pathlib.Path(path.dirname(self.trx_list_file_path)).mkdir(parents=True, exist_ok=True)

        with open(self.trx_list_file_path, mode) as f:
            f.writelines([json.dumps(i.dict()) + "\n" for i in trx_list])

    def parse_trx(self, trx_list: List[TrxDto]) -> Tuple[List[ParsedTrx], List[FailedTrx]]:
        """

        :param trx_list:
        :return: (parsed_trxs, failed_trxs)
        """

        logger.trace("parse transactions: begin")

        parser_lookup = self.parser_lookup
        parsed_trxs: List[ParsedTrx] = []
        failed_trxs: List[FailedTrx] = []

        for trx in trx_list:
            try:
                parsed_trxs = parsed_trxs + parser_lookup.find_parser(trx).parse(trx)
            except InvalidTransaction as e:
                logger.info(f"{trx.trx_id}: invalid transaction")
                failed_trxs.append(FailedTrx(trx_id=trx.trx_id, url=trx.url, method_id="0", err=e))
            except ParserNotFound as e:
                logger.info(f"{trx.trx_id}: parser not found")
                failed_trxs.append(FailedTrx(trx_id=trx.trx_id, url=trx.url, method_id=trx.details.method_id, err=e))
            except CurrencyNotFound as e:
                logger.warning(f"{trx.trx_id}: {str(e)}")
                failed_trxs.append(FailedTrx(trx_id=trx.trx_id, url=trx.url, method_id=trx.details.method_id, err=e))
            except TransactionSkipped as e:
                logger.info(f"{trx.trx_id}: transaction skipped")
                failed_trxs.append(FailedTrx(trx_id=trx.trx_id, url=trx.url, method_id=trx.details.method_id, err=e))
            except Exception as e:
                logger.error(f"{trx.trx_id}: unexpected error: {str(e)}")
                failed_trxs.append(FailedTrx(trx_id=trx.trx_id, url=trx.url, method_id=trx.details.method_id, err=e))

        return parsed_trxs, failed_trxs

    def aggregate_trx(self, parsed_trxs: List[ParsedTrx]) -> None:
        logger.trace("aggregate price data: begin")
        price_aggregator = self.price_aggregator
        for i in parsed_trxs:
            price_aggregator.update_price(i)

    def save_results(self) -> None:
        file_dir = path.dirname(self.output_file_path)
        pathlib.Path(file_dir).mkdir(parents=True, exist_ok=True)

        logger.trace("save results: begin")
        self.save_parsed_trx()
        self.save_failed_trx()

    def save_parsed_trx(self) -> None:
        output_file_path = self.output_file_path
        parsed_trxs = self.parsed_trxs

        csv_dtos = [trx.to_csv_dto() for trx in parsed_trxs]
        rows = [i.dict(by_alias=True) for i in numpy.concatenate(csv_dtos).flat]
        #
        # rows = [trx.to_dto().dict() for trx in parsed_trxs]

        with open(output_file_path, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        logger.info(f"parsed transactions wrote to: {output_file_path}")

    def save_failed_trx(self) -> None:
        output_file_path = self.output_file_path
        file_dir = path.dirname(self.output_file_path)
        output_file_name = pathlib.Path(output_file_path).stem
        failed_trx_file_path = path.join(file_dir, f"{output_file_name}_failed.csv")

        failed_trxs = self.failed_trxs
        rows = [trx.to_dto().dict() for trx in failed_trxs]

        with open(failed_trx_file_path, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)

        logger.info(f"failed transactions wrote to: {failed_trx_file_path}")
