from typing import List, Optional

from dto.Infura.transaction import TrxDto, TrxLogDto
from dto.parsedTrx import ParsedTrx, TrxPayload, ParsedTrxType
from models.exceptions import TransactionSkipped
from parser.Infura.parser_base import InfuraParser
from parser.Infura.defn_currency import Infura_currency_lookup
from parser.Infura.defn_status import parse_status


class Parser(InfuraParser):
    """
    default parser of "transfer", method_id: "0xa9059cbb"
    """

    def can_handle(self, trx: TrxDto) -> bool:
        return trx.details.method_id == "0xa9059cbb"

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        raise TransactionSkipped(f"skipped transaction: transfer")
