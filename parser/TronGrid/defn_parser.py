from typing import List

from dto.TronGrid.transaction import TrxDto
from dto.parsedTrx import ParsedTrxStatus
from parser.TronGrid import parser_dividend_1c4b774b, parser_swap_4bf3e2d0, \
    parser_dividend_7f8661a1, parser_swap_999bb7ac, parser_transfer_a9059cbb, parser_swap_b040d545, parser_swap_ddf7e1a7
from parser.TronGrid.defn_status import parse_status
from parser.TronGrid.parser_base import TronGridParser
from parser.parserLookup import ParserLookup

parser_list: List[TronGridParser] = [
    parser_dividend_1c4b774b.Parser(),
    parser_dividend_7f8661a1.Parser(),
    parser_swap_4bf3e2d0.Parser(),
    parser_swap_999bb7ac.Parser(),
    parser_swap_b040d545.Parser(),
    parser_swap_ddf7e1a7.Parser(),
    parser_transfer_a9059cbb.Parser(),
]


def pre_condition_assert(trx: TrxDto) -> None:
    status = parse_status(trx.status)
    if ParsedTrxStatus.Success != status:
        raise ValueError(f"invalid status: expected {ParsedTrxStatus.Success}, actual {status}")


TronGrid_parser_lookup = ParserLookup.from_parser_list(parser_list, pre_condition_assert=pre_condition_assert)
