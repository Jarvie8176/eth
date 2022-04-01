from dataclasses import dataclass
from typing import List, NoReturn

from dto.TronGrid.transaction import TrxDto
from models.exceptions import TransactionSkipped
from parser.TronGrid.parser_base import TronGridParser


@dataclass
class SkippedMethod:
    name: str
    method_id: str


skipped_methods: List[SkippedMethod] = [
    SkippedMethod(method_id="095ea7b3", name="approve"),
    SkippedMethod(method_id="3a4b66f1", name="stake"),
    SkippedMethod(method_id="7b0472f0", name="stake"),
    SkippedMethod(method_id="a694fc3a", name="stake"),
    SkippedMethod(method_id="51cff8d9", name="withdraw"),
    SkippedMethod(method_id="5ceae9c4", name="repay"),
    SkippedMethod(method_id="d2d0e066", name="deposit"),
    SkippedMethod(method_id="d0e30db0", name="deposit"),
    SkippedMethod(method_id="c858f5f9", name="borrow"),
    SkippedMethod(method_id="049878f3", name="join"),
    SkippedMethod(method_id="a9059cbb", name="transfer"),
    SkippedMethod(method_id="abbc44ed", name="bulksendTokenSimple"),
    SkippedMethod(method_id="b688a363", name="join"),
    SkippedMethod(method_id="daea85c5", name="approve"),

    SkippedMethod(method_id="e655a9d1", name="buyUnitRaffleTicket"),
    SkippedMethod(method_id="28a3623e", name="claimFirstUnit"),
    SkippedMethod(method_id="5dc22cce", name="attackPlayer"),
    SkippedMethod(method_id="709375d0", name="spendTalentPoint"),
    SkippedMethod(method_id="a21f74b8", name="fundGooResearch"),
    SkippedMethod(method_id="a5a2cb19", name="buyUpgrade"),
    SkippedMethod(method_id="4b8772c1", name="buyUnit"),
    SkippedMethod(method_id="f340fa01", name="deposit"),

    SkippedMethod(method_id="db006a75", name="redeem"),
    SkippedMethod(method_id="4a9321ef", name="depositTRX"),

    # SkippedMethod(method_id="foo", name="bar"),
    # SkippedMethod(method_id="foo", name="bar"),

    # SkippedMethod(method_id="foo", name="bar"),



    # SkippedMethod(method_id="foo", name="bar"),
]


class Parser(TronGridParser):
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
