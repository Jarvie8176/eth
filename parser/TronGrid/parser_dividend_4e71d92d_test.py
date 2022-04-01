import json
from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = [{
        "trx_id": "199a0d03921597ab1561512943f9d80a0635a37a6ba15759b8d6ec32ea50e4ca",
        "url": "https://tronscan.org/#/transaction/199a0d03921597ab1561512943f9d80a0635a37a6ba15759b8d6ec32ea50e4ca",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2020-09-15T00:26:45+00:00",
        "in_amount": "10.919362",
        "in_amount_major": None,
        "in_currency": "WHALES",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.41204",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }]

    result = prepare_parse_result(__file__)

    assert len(result) == 1
    TestCase().assertDictEqual(expected[0], result[0].to_dto().dict())
