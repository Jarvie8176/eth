from unittest import TestCase

from parser.Infura.util import prepare_parse_result


def test() -> None:
    expected = {
        "trx_id": "0x3cc2f4aa41a4e897daac600147e17d46d8e6d3a469edb9cde57d61948995c0b9",
        "url": "https://etherscan.io/tx/0x3cc2f4aa41a4e897daac600147e17d46d8e6d3a469edb9cde57d61948995c0b9",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2020-09-17T07:09:34+00:00",
        "in_amount": "400.012405",
        "in_amount_major": None,
        "in_currency": "UNI",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.081827",
        "fee_currency": "ETH",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    result = prepare_parse_result(__file__)
    assert len(result) == 1
    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
