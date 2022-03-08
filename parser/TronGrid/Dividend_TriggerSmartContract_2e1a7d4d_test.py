from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = {
        "trx_id": "04ba5584757fc22b865835a90955af86be5eb2d58d2327723d6d1c7930d8f721",
        "url": "https://tronscan.org/#/transaction/04ba5584757fc22b865835a90955af86be5eb2d58d2327723d6d1c7930d8f721",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2020-09-14T03:17:21+00:00",
        "in_amount": "23.0",
        "in_amount_major": None,
        "in_currency": "SUNOLD",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.71189",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    result = prepare_parse_result(__file__)
    assert len(result) == 1
    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
