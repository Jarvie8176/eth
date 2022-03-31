import json
from unittest import TestCase

from parser.Infura.defn_parser import Infura_parser_lookup
from parser.Infura.util import prepare_parse_result


def test() -> None:
    expected = [{
        "trx_id": "0x535cd400510fb4d3415e28136e096be9a96af81d713ff1a684b228ba889daf09",
        "url": "https://etherscan.io/tx/0x535cd400510fb4d3415e28136e096be9a96af81d713ff1a684b228ba889daf09",
        "type": "Sell",
        "status": "SUCCESS",
        "timestamp": "2021-04-12T09:04:54+00:00",
        "in_amount": None,
        "in_amount_major": None,
        "in_currency": None,
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "38330.413048647023708431",
        "out_amount_major": None,
        "out_currency": "BUSD",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.00169348",
        "fee_currency": "BNB",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }, {
        "trx_id": "0x535cd400510fb4d3415e28136e096be9a96af81d713ff1a684b228ba889daf09",
        "url": "https://etherscan.io/tx/0x535cd400510fb4d3415e28136e096be9a96af81d713ff1a684b228ba889daf09",
        "type": "Sell",
        "status": "SUCCESS",
        "timestamp": "2021-04-12T09:04:54+00:00",
        "in_amount": None,
        "in_amount_major": None,
        "in_currency": None,
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "38265.809941729083449566",
        "out_amount_major": None,
        "out_currency": "USDC",
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
