import pathlib
from os import path
from unittest import TestCase

from dateutil import parser

from aggregator.price import PriceAggregator
from dto.parsedTrx import ParsedTrx, TrxPayload, ParsedTrxStatus, ParsedTrxType
from parser.TronGrid.currencyLookup import name_to_currency


def test_price_lookup() -> None:
    trx_price_data_file_path = path.join(
        pathlib.Path(__file__).parent.resolve(),
        "../resources/historicalPrice/Bitfinex_TRXUSD_1h.csv")
    aggregator = PriceAggregator.create(
        trx_price_data_file_path=trx_price_data_file_path)

    parsed_trx = ParsedTrx(trx_id="", url="",
                           type=ParsedTrxType.Dividend,
                           status=ParsedTrxStatus.Success,
                           timestamp=parser.parse("2020-09-27T02:58:51+00:00"),
                           in_payload=TrxPayload(value="123",
                                                 currency=name_to_currency(
                                                     "GOLDCoinToken")),
                           fee_payload=TrxPayload(value="456",
                                                  currency=name_to_currency(
                                                      "TRXToken")))

    aggregator.update_price(parsed_trx)

    assert parsed_trx.in_payload.price is None  # type: ignore
    TestCase().assertDictEqual(parsed_trx.fee_payload.price.dict(), {  # type: ignore
        "timestamp": parser.parse("2020-09-27T03:00:00+00:00"),
        "symbol": "TRX/USD",
        "close": "0.02744"
    })
