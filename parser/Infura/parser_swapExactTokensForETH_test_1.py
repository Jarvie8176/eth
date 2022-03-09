from unittest import TestCase

from parser.Infura.util import prepare_parse_result


def test() -> None:
    expected = {
        "trx_id": "0x8127bde071aa22c15ff4139e87e3a8abc2e0f2269a5972b06c73b5b66019e156",
        "url": "https://etherscan.io/tx/0x8127bde071aa22c15ff4139e87e3a8abc2e0f2269a5972b06c73b5b66019e156",
        "type": "Swap",
        "status": "SUCCESS",
        "timestamp": "2020-10-08T23:39:53+00:00",
        "in_amount": "0.058365490600203689",
        "in_amount_major": "0.058365490600203689",
        "in_currency": "ETH",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "0.05",
        "out_amount_major": "0.058365490600203689",
        "out_currency": "DANDY",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.005064255",
        "fee_currency": "ETH",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    result = prepare_parse_result(__file__)
    assert len(result) == 1
    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
