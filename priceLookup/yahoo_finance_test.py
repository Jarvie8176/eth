import pathlib
from os import path
from dateutil import parser

from priceLookup.yahoo_finance import YahooPriceLookup


def test_usage() -> None:
    class TestPriceLookup(YahooPriceLookup):
        @property
        def unit(self) -> str:
            return "test_unit"

    source_file_path = path.join(
        pathlib.Path(__file__).parent.resolve(),
        "../resources/historicalPrice/AUTO-USD.csv")
    price_lookup = TestPriceLookup(source_file_path=source_file_path)

    # usage
    ttp = price_lookup.time_to_price(parser.parse("2021-04-17T10:00:00+00:00"))
    assert ttp.timestamp == parser.parse("2021-04-17T00:00:00Z")
    assert ttp.symbol == "test_unit/USD"
    assert ttp.close == "3439.811768"
