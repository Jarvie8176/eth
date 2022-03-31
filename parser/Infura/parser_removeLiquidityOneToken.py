from typing import List, Optional

from dto.Infura.transaction import TrxDto, TrxLogDto
from dto.parsedTrx import ParsedTrx, TrxPayload, ParsedTrxType
from parser.Infura import parser_remove_liquidity_one_coin
from parser.Infura.parser_base import InfuraParser
from parser.Infura.defn_currency import Infura_currency_lookup
from parser.Infura.defn_status import parse_status


class Parser(parser_remove_liquidity_one_coin.Parser):
    """
    default parser of "removeLiquidityOneToken", method_id: "0x3e3a1560"
    """

    def can_handle(self, trx: TrxDto) -> bool:
        return trx.details.method_id == "0x3e3a1560"
