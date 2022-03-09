from unittest import TestCase

from parser.Infura.util import prepare_parse_result


def test() -> None:
    expected = {
        "trx_id": "0x2fc784c727d9bf5db49939f091e0daaa2bf74a12d6078e80b973f284a6ffb110",
        "url": "https://etherscan.io/tx/0x2fc784c727d9bf5db49939f091e0daaa2bf74a12d6078e80b973f284a6ffb110",
        "type": "Swap",
        "status": "SUCCESS",
        "timestamp": "2020-08-30T18:17:56+00:00",
        "in_amount": "105.159311701267387852",
        "in_amount_major": "3.500407592057220649",
        "in_currency": "BAND",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "10.0",
        "out_amount_major": "3.500407592057220649",
        "out_currency": "YFIE",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.050334768",
        "fee_currency": "ETH",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    result = prepare_parse_result(__file__)
    assert len(result) == 1
    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
