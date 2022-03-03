from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = {
        "trx_id": "235c1cf9df062dc49bd0a89b45332c93c81d4fceced7ea0a8883c4da999bf6c9",
        "url": "https://tronscan.org/#/transaction/235c1cf9df062dc49bd0a89b45332c93c81d4fceced7ea0a8883c4da999bf6c9",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2020-09-27T02:58:51+00:00",
        "in_amount": "2363.782943",
        "in_currency": "GOLD",
        "fee_amount": "0.66087",
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
