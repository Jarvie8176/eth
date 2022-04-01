import json
from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = [{
        "trx_id": "d6a9f0cb2bd9265a0af98737fef6b06d649c466c8a6c6de31211fa7b45290d04",
        "url": "https://tronscan.org/#/transaction/d6a9f0cb2bd9265a0af98737fef6b06d649c466c8a6c6de31211fa7b45290d04",
        "type": "Swap",
        "status": "SUCCESS",
        "timestamp": "2020-09-12T10:45:18+00:00",
        "in_amount": "103500.0",
        "in_amount_major": "103500.0",
        "in_currency": "TRON",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "3362.339482",
        "out_amount_major": None,
        "out_currency": "USDT",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.41002",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }]

    result = prepare_parse_result(__file__)

    assert len(result) == 1
    TestCase().assertDictEqual(expected[0], result[0].to_dto().dict())
