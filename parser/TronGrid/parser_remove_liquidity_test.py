import json
from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = [{
        "trx_id": "2233a3c9dd5b591d5742221ffa479987c1e5f00ba756feec493cae9d41fc0d63",
        "url": "https://tronscan.org/#/transaction/2233a3c9dd5b591d5742221ffa479987c1e5f00ba756feec493cae9d41fc0d63",
        "type": "Buy",
        "status": "SUCCESS",
        "timestamp": "2020-09-12T12:33:39+00:00",
        "in_amount": "343101.297016",
        "in_amount_major": "343101.297016",
        "in_currency": "TRON",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.49998",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }, {
        "trx_id": "2233a3c9dd5b591d5742221ffa479987c1e5f00ba756feec493cae9d41fc0d63",
        "url": "https://tronscan.org/#/transaction/2233a3c9dd5b591d5742221ffa479987c1e5f00ba756feec493cae9d41fc0d63",
        "type": "Buy",
        "status": "SUCCESS",
        "timestamp": "2020-09-12T12:33:39+00:00",
        "in_amount": "4594.948298712874026607",
        "in_amount_major": None,
        "in_currency": "BALL",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": None,
        "fee_currency": None,
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }]

    result = prepare_parse_result(__file__)


    assert len(result) == 2
    TestCase().assertDictEqual(expected[0], result[0].to_dto().dict())
    TestCase().assertDictEqual(expected[1], result[1].to_dto().dict())
