import json
from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = {
        "trx_id": "71c897f361a164af3d627ea3ef14479c4da16ba805020b279af1d694fce7ec3e",
        "url": "https://tronscan.org/#/transaction/71c897f361a164af3d627ea3ef14479c4da16ba805020b279af1d694fce7ec3e",
        "type": "Transfer",
        "status": "SUCCESS",
        "timestamp": "2020-10-08T06:05:27+00:00",
        "in_amount": None,
        "in_currency": None,
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "100.0",
        "out_currency": "HODL",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.12968",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    print(json.dumps(expected))
    print(json.dumps(prepare_parse_result(__file__).dict()))

    TestCase().assertDictEqual(expected, prepare_parse_result(__file__).dict())
