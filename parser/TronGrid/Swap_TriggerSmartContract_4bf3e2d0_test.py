from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = {
        "trx_id": "c96f0d6a3bce8099b1351a9858abd26d9071d7b1da8a4df71f951c8ff4d20284",
        "url": "https://tronscan.org/#/transaction/c96f0d6a3bce8099b1351a9858abd26d9071d7b1da8a4df71f951c8ff4d20284",
        "type": "Swap",
        "status": "SUCCESS",
        "timestamp": "2020-09-16T18:31:33+00:00",
        "in_amount": "3664.354797",
        "in_amount_major": "139000.0",
        "in_currency": "USDT",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "139000.0",
        "out_amount_major": "139000.0",
        "out_currency": "TRON",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.48363",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    result = prepare_parse_result(__file__)
    assert len(result) == 1
    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
