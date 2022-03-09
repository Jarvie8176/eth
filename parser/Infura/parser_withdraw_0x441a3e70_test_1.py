from unittest import TestCase

from parser.Infura.util import prepare_parse_result


def test() -> None:
    expected = {
        "trx_id": "0x6ea2ccc2485022bdd3cbefa34c200efb6a3b52e53d55105426e375df6755db08",
        "url": "https://etherscan.io/tx/0x6ea2ccc2485022bdd3cbefa34c200efb6a3b52e53d55105426e375df6755db08",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2020-08-31T20:37:19+00:00",
        "in_amount": "48.304587008551555899",
        "in_amount_major": None,
        "in_currency": "SUSHI",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.04033658",
        "fee_currency": "ETH",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    result = prepare_parse_result(__file__)
    assert len(result) == 1
    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
