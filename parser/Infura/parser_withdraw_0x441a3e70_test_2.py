from unittest import TestCase

from parser.Infura.util import prepare_parse_result


def test() -> None:
    expected = {
        "trx_id": "0x5ee46863ef935cf92d03eb4aec7201a6d5f834c16e722ffeb13f8cfb38cee340",
        "url": "https://etherscan.io/tx/0x5ee46863ef935cf92d03eb4aec7201a6d5f834c16e722ffeb13f8cfb38cee340",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2020-08-28T17:55:57+00:00",
        "in_amount": "3.486442209512133863",
        "in_amount_major": None,
        "in_currency": "SUSHI",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.01009925",
        "fee_currency": "ETH",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    result = prepare_parse_result(__file__)
    assert len(result) == 1
    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
