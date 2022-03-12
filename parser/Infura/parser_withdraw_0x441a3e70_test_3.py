from unittest import TestCase

from parser.Infura.util import prepare_parse_result


def test() -> None:
    expected = {
        "trx_id": "0x13d47ffc2a60d8028dcf4da046fe898542b3fa2ea475c546e7a0919f6a19814a",
        "url": "https://etherscan.io/tx/0x13d47ffc2a60d8028dcf4da046fe898542b3fa2ea475c546e7a0919f6a19814a",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2021-04-17T00:29:50+00:00",
        "in_amount": "0.10204081632653062",
        "in_amount_major": None,
        "in_currency": "KEY",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.00307214",
        "fee_currency": "BNB",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    result = prepare_parse_result(__file__)
    assert len(result) == 1
    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
