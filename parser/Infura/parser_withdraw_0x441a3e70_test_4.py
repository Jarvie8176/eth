from unittest import TestCase

from parser.Infura.util import prepare_parse_result


def test() -> None:
    expected = {
        "trx_id": "0x30b2a2afc09159dc5269533c017279fdad985e8c64457540db10d782fdc25ec9",
        "url": "https://etherscan.io/tx/0x30b2a2afc09159dc5269533c017279fdad985e8c64457540db10d782fdc25ec9",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2021-04-17T00:29:50+00:00",
        "in_amount": "43.967386471197569604",
        "in_amount_major": None,
        "in_currency": "SHD",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.0033844",
        "fee_currency": "BNB",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    result = prepare_parse_result(__file__)
    assert len(result) == 1
    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
