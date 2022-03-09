from typing import List

from dto.Infura.transaction import TrxDto
from dto.parsedTrx import ParsedTrx
from models.exceptions import TransactionSkipped
from parser.Infura.parser_base import InfuraParser


class Parser(InfuraParser):
    """
    default parser of "withdraw", method_id: "0x2e1a7d4d" (withdraw from ETH pool)
    """

    def can_handle(self, trx: TrxDto) -> bool:
        return trx.details.method_id == "0x2e1a7d4d"

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        raise TransactionSkipped(f"skipped transaction: {trx.trx_id}")
