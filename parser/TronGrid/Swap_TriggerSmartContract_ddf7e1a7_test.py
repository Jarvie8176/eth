from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = {
        "trx_id": "90713085085541744d004caeac9810e8e51e5f45941f1ffc988ad03a4e6b2d7a",
        "url": "https://tronscan.org/#/transaction/90713085085541744d004caeac9810e8e51e5f45941f1ffc988ad03a4e6b2d7a",
        "type": "Swap",
        "status": "SUCCESS",
        "timestamp": "2020-09-29T21:06:45+00:00",
        "in_amount": "20.587889",
        "in_amount_major": "799.800211",
        "in_currency": "USDT",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "0.059127",
        "out_amount_major": "799.800211",
        "out_currency": "COLA",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.80159",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    result = prepare_parse_result(__file__)
    assert len(result) == 1
    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
