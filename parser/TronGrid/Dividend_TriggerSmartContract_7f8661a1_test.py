from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = {
        "trx_id": "035ac031e657c9370f2a7470f8673d23ee576176b57c3a92b6c870adaff2c0f1",
        "url": "https://tronscan.org/#/transaction/035ac031e657c9370f2a7470f8673d23ee576176b57c3a92b6c870adaff2c0f1",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2020-09-29T02:04:06+00:00",
        "in_amount": "12.503696",
        "in_amount_major": None,
        "in_currency": "GOLD",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "1.19978",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    result = prepare_parse_result(__file__)
    assert len(result) == 1
    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
