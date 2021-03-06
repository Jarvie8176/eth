from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = {
        "trx_id": "1555bcb2abb5213952bdf6d09409027ae6811da2cde07671251b1f8340508081",
        "url": "https://tronscan.org/#/transaction/1555bcb2abb5213952bdf6d09409027ae6811da2cde07671251b1f8340508081",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2020-09-29T02:03:09+00:00",
        "in_amount": "1778.061151",
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
        "fee_amount": "0.66923",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    result = prepare_parse_result(__file__)
    assert len(result) == 1
    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
