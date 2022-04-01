import json
from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = [{
        "trx_id": "b5347459c4179fb6d86abba1e0a0c37478d63ed9a671b0924902b476c31e6e7a",
        "url": "https://tronscan.org/#/transaction/b5347459c4179fb6d86abba1e0a0c37478d63ed9a671b0924902b476c31e6e7a",
        "type": "Buy",
        "status": "SUCCESS",
        "timestamp": "2020-09-14T10:58:42+00:00",
        "in_amount": "34.574806",
        "in_amount_major": "34.574806",
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
        "fee_amount": "0.50851",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }, {
        "trx_id": "b5347459c4179fb6d86abba1e0a0c37478d63ed9a671b0924902b476c31e6e7a",
        "url": "https://tronscan.org/#/transaction/b5347459c4179fb6d86abba1e0a0c37478d63ed9a671b0924902b476c31e6e7a",
        "type": "Buy",
        "status": "SUCCESS",
        "timestamp": "2020-09-14T10:58:42+00:00",
        "in_amount": "0.998779579261230644",
        "in_amount_major": None,
        "in_currency": "USDJ",
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
