from unittest import TestCase

from parser.Infura.defn_parser import Infura_parser_lookup
from parser.Infura.util import prepare_parse_result


def test() -> None:
    expected = [{
        "trx_id": "0xc5139f340ccb725624044f4eb96f14f5a3080d046dae8324e3322bbc027ea1a0",
        "url": "https://etherscan.io/tx/0xc5139f340ccb725624044f4eb96f14f5a3080d046dae8324e3322bbc027ea1a0",
        "type": "Buy",
        "status": "SUCCESS",
        "timestamp": "2021-04-29T02:18:44+00:00",
        "in_amount": "39445.219043464621224847",
        "in_amount_major": None,
        "in_currency": "BUSD",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.00110508",
        "fee_currency": "BNB",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }, {
        "trx_id": "0xc5139f340ccb725624044f4eb96f14f5a3080d046dae8324e3322bbc027ea1a0",
        "url": "https://etherscan.io/tx/0xc5139f340ccb725624044f4eb96f14f5a3080d046dae8324e3322bbc027ea1a0",
        "type": "Buy",
        "status": "SUCCESS",
        "timestamp": "2021-04-29T02:18:44+00:00",
        "in_amount": "69.860046161809954494",
        "in_amount_major": "69.860046161809954494",
        "in_currency": "BNB",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": None,
        "fee_currency": None,
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }]

    Infura_parser_lookup.update_major_currency("BNB")
    result = prepare_parse_result(__file__)
    Infura_parser_lookup.update_major_currency("Ether")  # patch back

    assert len(result) == 2

    TestCase().assertDictEqual(expected[0], result[0].to_dto().dict())
    TestCase().assertDictEqual(expected[1], result[1].to_dto().dict())
