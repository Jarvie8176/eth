from unittest import TestCase

from parser.Infura.defn_parser import Infura_parser_lookup
from parser.Infura.util import prepare_parse_result


def test() -> None:
    expected = [{
        "trx_id": "0xac34a84bb9bb2749f687497deaa1ce649ec7e2b4038bafd076ebf1913d8e13cc",
        "url": "https://etherscan.io/tx/0xac34a84bb9bb2749f687497deaa1ce649ec7e2b4038bafd076ebf1913d8e13cc",
        "type": "Buy",
        "status": "SUCCESS",
        "timestamp": "2021-03-24T03:23:11+00:00",
        "in_amount": "14926.494126486088145971",
        "in_amount_major": None,
        "in_currency": "UST",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.00183351",
        "fee_currency": "BNB",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }, {
        "trx_id": "0xac34a84bb9bb2749f687497deaa1ce649ec7e2b4038bafd076ebf1913d8e13cc",
        "url": "https://etherscan.io/tx/0xac34a84bb9bb2749f687497deaa1ce649ec7e2b4038bafd076ebf1913d8e13cc",
        "type": "Buy",
        "status": "SUCCESS",
        "timestamp": "2021-03-24T03:23:11+00:00",
        "in_amount": "7.166088229532989111",
        "in_amount_major": None,
        "in_currency": "mGOOGL",
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
