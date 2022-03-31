import pathlib
from os import path
from dateutil import parser

from priceLookup.bnb import BNBPriceLookup


def test_usage() -> None:
    source_file_path = path.join(
        pathlib.Path(__file__).parent.resolve(),
        "../resources/historicalPrice/BNB-USD.csv")
    price_lookup = BNBPriceLookup(source_file_path=source_file_path)

    # usage
    ttp = price_lookup.time_to_price(parser.parse("2021-02-26T15:00:00+00:00"))
    assert ttp.timestamp == parser.parse("2021-02-27T00:00:00Z")
    assert ttp.symbol == "BNB/USD"
    assert ttp.close == "225.249435"
