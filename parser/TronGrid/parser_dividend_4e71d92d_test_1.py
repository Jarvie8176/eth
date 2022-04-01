import json
from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = [{
        "trx_id": "411af3a886ef94993a54bb484a6680fc1db73923bbc1c4093a0a10af434495a1",
        "url": "https://tronscan.org/#/transaction/411af3a886ef94993a54bb484a6680fc1db73923bbc1c4093a0a10af434495a1",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2020-09-08T20:00:24+00:00",
        "in_amount": "0.001668891308322995",
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
        "fee_amount": "0.77838",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }]

    result = prepare_parse_result(__file__)

    assert len(result) == 1
    TestCase().assertDictEqual(expected[0], result[0].to_dto().dict())
