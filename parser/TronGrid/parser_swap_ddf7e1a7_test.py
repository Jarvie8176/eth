import json
from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = [{
        "trx_id": "29f1b423237fd0684b589d158104ca9d537b244507c7544edbe99712897494e7",
        "url": "https://tronscan.org/#/transaction/29f1b423237fd0684b589d158104ca9d537b244507c7544edbe99712897494e7",
        "type": "Swap",
        "status": "SUCCESS",
        "timestamp": "2020-09-15T02:11:09+00:00",
        "in_amount": "0.003945640559881641",
        "in_amount_major": "0.133438",
        "in_currency": "DRACO",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "0.004",
        "out_amount_major": "0.133438",
        "out_currency": "USDT",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.88209",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }]

    result = prepare_parse_result(__file__)

    assert len(result) == 1
    TestCase().assertDictEqual(expected[0], result[0].to_dto().dict())
