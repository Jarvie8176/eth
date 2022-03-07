import json
import pathlib
from os import path
from typing import List

from aggregator.price import PriceAggregator
from dto.TronGrid.transaction import TrxDto
from dto.parsedTrx import ParsedTrx
from models.exceptions import ParserNotFound
from parser.TronGrid.parserLookup import ParserLookup


def test() -> None:
    test_file = path.join(
        pathlib.Path(__file__).parent.resolve(),
        "../data/test_fixture/tron_TJ7ozAvfPwxpNANWfMnAhVwGBYkwTjuscJ.txt")

    with open(test_file, "r") as f_trx:
        transactions = list(map(lambda line: TrxDto(**json.loads(line)), f_trx.readlines()))

    assert len(transactions) == 172

    parser_lookup = ParserLookup.create()

    parsed_trx: List[ParsedTrx] = []
    failed_trx: List[TrxDto] = []

    for trx in transactions:
        print(trx.trx_id)
        try:
            parsed_trx.append(parser_lookup.find_parser(trx).parse(trx))
        except ParserNotFound:
            failed_trx.append(trx)
        except Exception:
            failed_trx.append(trx)

    trx_price_data_file_path = path.join(pathlib.Path(__file__).parent.resolve(),
                                         "../resources/historicalPrice/Bitfinex_TRXUSD_1h.csv")
    price_aggregator = PriceAggregator.create(trx_price_data_file_path=trx_price_data_file_path)
    for i in parsed_trx:
        price_aggregator.update_price(i)

    assert len(parsed_trx) == 76
    assert len(failed_trx) == 96
