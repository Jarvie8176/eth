import json
import pathlib
from os import path

from dto.Infura.transaction import TrxDetailsDto, TrxReceiptDto


def test_method_id() -> None:
    test_file = path.join(pathlib.Path(__file__).parent.resolve(), "transaction_test.method_id_payload.txt")
    with open(test_file, 'r') as f:
        input = json.load(f)

    assert TrxDetailsDto(**input).method_id == "0x7ff36ab5"


def test_get_log_by_index() -> None:
    test_file = path.join(pathlib.Path(__file__).parent.resolve(), "./transaction_test.get_log_payload.txt")
    with open(test_file, 'r') as f:
        input = json.load(f)

    trx_receipt = TrxReceiptDto(**input)
    assert trx_receipt.get_log_by_index(0).logIndex == "0xef"  # type: ignore
    assert trx_receipt.get_log_by_index(1).logIndex == "0xf0"  # type: ignore
    assert trx_receipt.get_log_by_index(2).logIndex == "0xf1"  # type: ignore
    assert trx_receipt.get_log_by_index(3).logIndex == "0xf2"  # type: ignore
    assert trx_receipt.get_log_by_index(4).logIndex == "0xf3"  # type: ignore
    assert trx_receipt.get_log_by_index(5) is None
    assert trx_receipt.get_log_by_index(-1) is None
