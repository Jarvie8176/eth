import json
from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = [{
        "trx_id": "4a8ba22b8c11f73e96a2132d67461283ff8cfdbe9d7cdfcb77bf46f17ee897b2",
        "url": "https://tronscan.org/#/transaction/4a8ba22b8c11f73e96a2132d67461283ff8cfdbe9d7cdfcb77bf46f17ee897b2",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2020-09-11T21:34:12+00:00",
        "in_amount": "0.122969130460551302",
        "in_amount_major": None,
        "in_currency": "KIT",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.94178",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }]

    result = prepare_parse_result(__file__)

    assert len(result) == 1
    TestCase().assertDictEqual(expected[0], result[0].to_dto().dict())
