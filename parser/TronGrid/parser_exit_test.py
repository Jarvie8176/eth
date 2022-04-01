import json
from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = [{
        "trx_id": "a6cf21b3e25047fb54ce13309a789e9f7d3976266826a8efa25981941894dcf8",
        "url": "https://tronscan.org/#/transaction/a6cf21b3e25047fb54ce13309a789e9f7d3976266826a8efa25981941894dcf8",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2020-09-09T02:24:36+00:00",
        "in_amount": "0.00128223971780361",
        "in_amount_major": None,
        "in_currency": "MFI",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "1.59899",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }]

    result = prepare_parse_result(__file__)

    assert len(result) == 1
    TestCase().assertDictEqual(expected[0], result[0].to_dto().dict())
