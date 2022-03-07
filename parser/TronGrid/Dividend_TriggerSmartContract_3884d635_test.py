from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = {
        "trx_id": "21e85d2f71ecbab9a10b5c8ee35ddd4714351f8fed0647869aad4d3b145dee85",
        "url": "https://tronscan.org/#/transaction/21e85d2f71ecbab9a10b5c8ee35ddd4714351f8fed0647869aad4d3b145dee85",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2020-09-26T23:22:33+00:00",
        "in_amount": "11.525096",
        "in_currency": "GOLD",
        "fee_amount": "0.54166",
        "fee_currency": "TRON",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    TestCase().assertDictEqual(expected, prepare_parse_result(__file__).dict())
