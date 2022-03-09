from unittest import TestCase

from parser.Infura.util import prepare_parse_result


def test() -> None:
    expected = {
        "trx_id": "0xaef8e7af467d4e4b563d2ae8cf6e3804c834824ebb864c07944ed868ca9e9762",
        "url": "https://etherscan.io/tx/0xaef8e7af467d4e4b563d2ae8cf6e3804c834824ebb864c07944ed868ca9e9762",
        "type": "Swap",
        "status": "SUCCESS",
        "timestamp": "2020-08-30T12:09:40+00:00",
        "in_amount": "3.496859168201799455",
        "in_amount_major": "3.496859168201799455",
        "in_currency": "ETH",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "1435.574936",
        "out_amount_major": "3.496859168201799455",
        "out_currency": "USDT",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.01890383",
        "fee_currency": "ETH",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    result = prepare_parse_result(__file__)
    assert len(result) == 1
    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
