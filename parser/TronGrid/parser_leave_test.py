import json
from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = [{
        "trx_id": "6434790859e178c3981dede5b40d363f3b593701181a190c3477dfd3b20bcc5f",
        "url": "https://tronscan.org/#/transaction/6434790859e178c3981dede5b40d363f3b593701181a190c3477dfd3b20bcc5f",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2020-09-15T09:58:48+00:00",
        "in_amount": "21.704904",
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
        "fee_amount": "0.77243",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }]

    result = prepare_parse_result(__file__)

    assert len(result) == 1
    TestCase().assertDictEqual(expected[0], result[0].to_dto().dict())
