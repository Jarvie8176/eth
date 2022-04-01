import json
from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = [{
        "trx_id": "f0e3a0992ecef757bf7e17b182dabd8a20add414b63eb9c1211707f52f38befe",
        "url": "https://tronscan.org/#/transaction/f0e3a0992ecef757bf7e17b182dabd8a20add414b63eb9c1211707f52f38befe",
        "type": "Swap",
        "status": "SUCCESS",
        "timestamp": "2020-09-08T10:21:42+00:00",
        "in_amount": "3.0",
        "in_amount_major": "3.433463",
        "in_currency": "JST",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "3.433463",
        "out_amount_major": "3.433463",
        "out_currency": "TRON",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.53691",
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
