import json
from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:

    expected = [{
        "trx_id": "480500082a584d7a945f3206204792734c832d8aeebdf1378c4826dcfa111868",
        "url": "https://tronscan.org/#/transaction/480500082a584d7a945f3206204792734c832d8aeebdf1378c4826dcfa111868",
        "type": "Sell",
        "status": "SUCCESS",
        "timestamp": "2020-09-12T08:09:12+00:00",
        "in_amount": None,
        "in_amount_major": None,
        "in_currency": None,
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "10634.144333",
        "out_amount_major": "10634.144333",
        "out_currency": "TRON",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.66045",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }, {
        "trx_id": "480500082a584d7a945f3206204792734c832d8aeebdf1378c4826dcfa111868",
        "url": "https://tronscan.org/#/transaction/480500082a584d7a945f3206204792734c832d8aeebdf1378c4826dcfa111868",
        "type": "Sell",
        "status": "SUCCESS",
        "timestamp": "2020-09-12T08:09:12+00:00",
        "in_amount": None,
        "in_amount_major": None,
        "in_currency": None,
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "99.933770108476646756",
        "out_amount_major": None,
        "out_currency": "BALL",
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
