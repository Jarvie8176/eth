from unittest import TestCase

from parser.Infura.util import prepare_parse_result


def test() -> None:
    expected = {
        "trx_id": "0xc4358d3b95206957c478587210dcc235ee0eb242a2a61c35cc513413bcf916f9",
        "url": "https://etherscan.io/tx/0xc4358d3b95206957c478587210dcc235ee0eb242a2a61c35cc513413bcf916f9",
        "type": "Swap",
        "status": "SUCCESS",
        "timestamp": "2020-08-31T18:19:24+00:00",
        "in_amount": "1000.0",
        "in_amount_major": "6.637512045967350683",
        "in_currency": "SRM",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "6.637512045967350683",
        "out_amount_major": "6.637512045967350683",
        "out_currency": "ETH",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.040091996",
        "fee_currency": "ETH",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    result = prepare_parse_result(__file__)
    assert len(result) == 1
    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
