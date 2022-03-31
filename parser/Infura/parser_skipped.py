from dataclasses import dataclass
from typing import List, NoReturn

from dto.Infura.transaction import TrxDto
from dto.parsedTrx import ParsedTrx
from models.exceptions import TransactionSkipped
from parser.Infura.parser_base import InfuraParser


@dataclass
class SkippedMethod:
    name: str
    method_id: str


skipped_methods: List[SkippedMethod] = [
    SkippedMethod(method_id="0xa9059cbb", name="transfer"),
    SkippedMethod(method_id="0x095ea7b3", name="approve"),
    SkippedMethod(method_id="0x095ea7b3", name="approve"),
    SkippedMethod(method_id="0x41441d3b", name="enterStaking"),
    SkippedMethod(method_id="0x9018c818", name="acceptInvitation"),
    SkippedMethod(method_id="0xe9fad8ee", name="exit"),
    SkippedMethod(method_id="0x294091cd", name="stake"),
    SkippedMethod(method_id="0x7acb7757", name="stake"),
    SkippedMethod(method_id="0xe7e4e1f7", name="stake"),
    SkippedMethod(method_id="0xdb006a75", name="redeem"),
    SkippedMethod(method_id="0xc858f5f9", name="borrow"),
    SkippedMethod(method_id="0x5ceae9c4", name="repay"),
    SkippedMethod(method_id="0x42220f34", name="depositBNB"),  # confirmed
    SkippedMethod(method_id="0xde5f6268", name="depositAll"),
    SkippedMethod(method_id="0x853828b6", name="withdrawAll"),
    SkippedMethod(method_id="0xa65b37a1", name="buyXname"),
    SkippedMethod(method_id="0x98a0871d", name="buyXaddr"),
    SkippedMethod(method_id="0x8e1a55fc", name="build"),
    SkippedMethod(method_id="0x685ffd83", name="registerNameXname"),
    # SkippedMethod(method_id="foo", name="bar"),
]


class Parser(InfuraParser):
    """
    method ids to be skipped
    """

    @property
    def load_order(self) -> int:
        return 1

    def can_handle(self, trx: TrxDto) -> bool:
        return trx.details.method_id in [sm.method_id for sm in skipped_methods]

    # noinspection PyTypeChecker
    def parse(self, trx: TrxDto) -> NoReturn:
        skipped_method = next(i for i in skipped_methods if trx.details.method_id == i.method_id)
        raise TransactionSkipped(f"skipped method: {skipped_method.name}")
        pass
