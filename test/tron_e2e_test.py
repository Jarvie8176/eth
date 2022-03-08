import json
import pathlib
from os import path
from typing import List

from loguru import logger

from aggregator.price import PriceAggregator, PriceAggregatorCreateOptions
from dto.TronGrid.transaction import TrxDto
from dto.parsedTrx import ParsedTrx
from models.exceptions import ParserNotFound
from parser.TronGrid.defn_parser import TronGrid_parser_lookup


def test() -> None:
    test_file = path.join(
        pathlib.Path(__file__).parent.resolve(),
        "../data/test_fixture/tron_TJ7ozAvfPwxpNANWfMnAhVwGBYkwTjuscJ.txt")

    with open(test_file, "r") as f_trx:
        transactions = list(map(lambda line: TrxDto(**json.loads(line)), f_trx.readlines()))

    assert len(transactions) == 172

    parser_lookup = TronGrid_parser_lookup

    parsed_trx: List[ParsedTrx] = []
    failed_trx: List[TrxDto] = []

    for trx in transactions:
        try:
            parsed_trx = parsed_trx + parser_lookup.find_parser(trx).parse(trx)
        except ParserNotFound:
            failed_trx.append(trx)
        except Exception as e:
            logger.error("unexpected error", e)
            failed_trx.append(trx)

    trx_price_data_file_path = path.join(pathlib.Path(__file__).parent.resolve(),
                                         "../resources/historicalPrice/Bitfinex_TRXUSD_1h.csv")
    price_aggregator = PriceAggregator.create(
        options=PriceAggregatorCreateOptions(trx_price_data_file_path=trx_price_data_file_path))
    for i in parsed_trx:
        price_aggregator.update_price(i)

    assert len(parsed_trx) == 76
    assert len(failed_trx) == 96
