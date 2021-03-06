from unittest import TestCase

from parser.Infura.util import prepare_parse_result


def test() -> None:
    expected = {
        "trx_id": "0x972572401a09bb427f55d28cc087da7b845369a6f44aeac1b7d5050fa732db6d",
        "url": "https://etherscan.io/tx/0x972572401a09bb427f55d28cc087da7b845369a6f44aeac1b7d5050fa732db6d",
        "type": "Sell",
        "status": "SUCCESS",
        "timestamp": "2020-08-30T18:22:11+00:00",
        "in_amount": "3.490331363853588519",
        "in_amount_major": "3.490331363853588519",
        "in_currency": "ETH",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "105.159311701267387852",
        "out_amount_major": "3.490331363853588519",
        "out_currency": "BAND",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.032898544",
        "fee_currency": "ETH",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    result = prepare_parse_result(__file__)
    assert len(result) == 1
    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
