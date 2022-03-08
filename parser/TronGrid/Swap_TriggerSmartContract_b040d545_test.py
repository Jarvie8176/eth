from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = {
        "trx_id": "a107cc9748e755c579f46df1b0319cb9c6be01e099d771bf43e15d2b28912b35",
        "url": "https://tronscan.org/#/transaction/a107cc9748e755c579f46df1b0319cb9c6be01e099d771bf43e15d2b28912b35",
        "type": "Swap",
        "status": "SUCCESS",
        "timestamp": "2020-09-29T22:58:30+00:00",
        "in_amount": "50.0",
        "in_amount_major": "1940.689572",
        "in_currency": "USDJ",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "50.569549",
        "out_amount_major": "1940.689572",
        "out_currency": "USDT",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.76688",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    result = prepare_parse_result(__file__)
    assert len(result) == 1
    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
