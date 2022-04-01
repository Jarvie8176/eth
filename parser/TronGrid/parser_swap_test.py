import json
from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = [{
        "trx_id": "4493595fc618e7a692ee7150a65fbd09bf6d0d6f71194aa883df38a85d9ca82f",
        "url": "https://tronscan.org/#/transaction/4493595fc618e7a692ee7150a65fbd09bf6d0d6f71194aa883df38a85d9ca82f",
        "type": "Swap",
        "status": "SUCCESS",
        "timestamp": "2020-09-14T09:12:33+00:00",
        "in_amount": "0.028627",
        "in_amount_major": None,
        "in_currency": "USDT",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "2.94",
        "out_amount_major": None,
        "out_currency": "DASH",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.87144",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }]

    result = prepare_parse_result(__file__)

    print(json.dumps(expected[0]))
    print(json.dumps(result[0].to_dto().dict()))


    assert len(result) == 1
    TestCase().assertDictEqual(expected[0], result[0].to_dto().dict())
