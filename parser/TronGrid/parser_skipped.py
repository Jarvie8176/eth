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
