from unittest import TestCase

from parser.Infura.util import prepare_parse_result


def test() -> None:
    expected = {
        "trx_id": "0xe01329bbd42050057a6f9b6b18c666f15d7baf4c33b62d6b673d2d2dbe6e5491",
        "url": "https://etherscan.io/tx/0xe01329bbd42050057a6f9b6b18c666f15d7baf4c33b62d6b673d2d2dbe6e5491",
        "type": "Swap",
        "status": "SUCCESS",
        "timestamp": "2020-08-30T07:34:51+00:00",
        "in_amount": "9.0",
        "in_amount_major": "4.38002138944889871",
        "in_currency": "YFIE",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "1780.010567",
        "out_amount_major": "4.38002138944889871",
        "out_currency": "USDT",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.0491475",
        "fee_currency": "ETH",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    result = prepare_parse_result(__file__)
    assert len(result) == 1
    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
