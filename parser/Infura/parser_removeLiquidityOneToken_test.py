import json
from unittest import TestCase

from parser.Infura.defn_parser import Infura_parser_lookup
from parser.Infura.util import prepare_parse_result


def test() -> None:
    expected = [{
        "trx_id": "0x67d314a74306cde4c808d55fc481625e779bd9244c6eed25dee3171bb4333595",
        "url": "https://etherscan.io/tx/0x67d314a74306cde4c808d55fc481625e779bd9244c6eed25dee3171bb4333595",
        "type": "Buy",
        "status": "SUCCESS",
        "timestamp": "2021-04-12T09:41:52+00:00",
        "in_amount": "76518.756262969362941027",
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
        "fee_amount": "0.002478984",
        "fee_currency": "BNB",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }]

    Infura_parser_lookup.update_major_currency("BNB")
    result = prepare_parse_result(__file__)
    Infura_parser_lookup.update_major_currency("Ether")  # patch back

    assert len(result) == 1

    TestCase().assertDictEqual(expected[0], result[0].to_dto().dict())
