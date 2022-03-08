from unittest import TestCase

from parser.Infura.util import prepare_parse_result


def test() -> None:
    expected = {
        "trx_id": "0x2ef93fa1cf02cd2b08a1e62ef9380da7e56f1806867c35e6cec3ba47701dbf0e",
        "url": "https://etherscan.io/tx/0x2ef93fa1cf02cd2b08a1e62ef9380da7e56f1806867c35e6cec3ba47701dbf0e",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2020-09-27T20:01:08+00:00",
        "in_amount": "0.05",
        "in_amount_major": None,
        "in_currency": "DANDY",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.018234322618694786",
        "fee_currency": "ETH",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    result = prepare_parse_result(__file__)
    assert len(result) == 1
    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
