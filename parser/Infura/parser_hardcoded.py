from typing import List, Any, Dict

from dto.Infura.transaction import TrxDto
from dto.parsedTrx import ParsedTrx, TrxPayload, ParsedTrxType, ParsedTrxStatus
from parser.Infura.parser_base import InfuraParser
from parser.Infura.defn_currency import Infura_currency_lookup
from parser.Infura.defn_status import parse_status

transaction_ids: Dict[str, List[ParsedTrx]] = {

}


class Parser(InfuraParser):
    """
    parser for transactions with hard coded results
    """

    @property
    def load_order(self) -> int:
        return 9999

    def can_handle(self, trx: TrxDto) -> bool:
        return trx.trx_id in transaction_ids.keys()

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        result = transaction_ids.get(trx.trx_id)
        if not result:
            raise ValueError("transaction is in hard coded list but no result")
        return result
