import pathlib
from os import path
from dateutil import parser

from priceLookup.trx import TRXPriceLookup


def test_usage() -> None:
    source_file_path = path.join(
        pathlib.Path(__file__).parent.resolve(),
        "../resources/historicalPrice/Bitfinex_TRXUSD_1h.csv")
    trx_price_lookup = TRXPriceLookup(source_file_path=source_file_path)

    # usage
    assert trx_price_lookup.time_to_price(
        parser.parse("2022-02-26T15:00:00+00:00")).close == "0.059783"

    # timestamp higher than the latest
    assert trx_price_lookup.time_to_price(
        parser.parse("2023-02-26T15:00:00Z")).close == "0.057905"

    # timestamp lower than the earliest
    assert trx_price_lookup.time_to_price(
        parser.parse("2000-02-26T15:00:00Z")).close == "0.0725"

    # timestamp closer to left
    assert trx_price_lookup.time_to_price(
        parser.parse("2022-02-27T22:01:00Z")).close == "0.058276"

    # timestamp closer to right
    assert trx_price_lookup.time_to_price(
        parser.parse("2022-02-27T22:59:00Z")).close == "0.05815"
