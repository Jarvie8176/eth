from unittest import TestCase

from parser.Infura.defn_parser import Infura_parser_lookup
from parser.Infura.util import prepare_parse_result


def test() -> None:
    expected = {
        "trx_id": "0x41fbf069d38431c4302bff5701701bfa500d78c17ca3c676bf7bf222d85a2642",
        "url": "https://etherscan.io/tx/0x41fbf069d38431c4302bff5701701bfa500d78c17ca3c676bf7bf222d85a2642",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2021-04-08T20:31:55+00:00",
        "in_amount": "6.176336984556762044",
        "in_amount_major": None,
        "in_currency": "Cake",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.000556645",
        "fee_currency": "BNB",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    Infura_parser_lookup.update_major_currency("BNB")
    result = prepare_parse_result(__file__)
    Infura_parser_lookup.update_major_currency("Ether")  # patch back
    assert len(result) == 1
    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
