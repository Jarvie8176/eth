from typing import List

from dto.TronGrid.transaction import TrxDto
from dto.parsedTrx import ParsedTrxStatus
from models.exceptions import InvalidTransaction
from parser.TronGrid import parser_dividend_1c4b774b, parser_swap_4bf3e2d0, \
    parser_dividend_7f8661a1, parser_swap_999bb7ac, parser_transfer_a9059cbb, parser_swap_b040d545, \
    parser_swap_ddf7e1a7, parser_skipped, parser_leave, parser_remove_liquidity, parser_swap, parser_dividend_4e71d92d, \
    parser_add_liquidity, parser_withdraw, parser_swap_a8f85ca6, parser_exit
from parser.TronGrid.defn_status import parse_status
from parser.TronGrid.parser_base import TronGridParser
from parser.parserLookup import ParserLookup

parser_list: List[TronGridParser] = [
    parser_dividend_1c4b774b.Parser(),
    parser_dividend_7f8661a1.Parser(),
    parser_dividend_4e71d92d.Parser(),
    parser_swap.Parser(),
    parser_swap_4bf3e2d0.Parser(),
    parser_swap_999bb7ac.Parser(),
    parser_swap_b040d545.Parser(),
    parser_swap_ddf7e1a7.Parser(),
    parser_swap_a8f85ca6.Parser(),
    parser_transfer_a9059cbb.Parser(),
    parser_skipped.Parser(),
    parser_leave.Parser(),
    parser_add_liquidity.Parser(),
    parser_remove_liquidity.Parser(),
    parser_withdraw.Parser(),
    parser_exit.Parser(),
]



def pre_condition_assert(trx: TrxDto) -> None:
    status = parse_status(trx.status)
    if ParsedTrxStatus.Success != status:
        raise ValueError(f"invalid status: expected {ParsedTrxStatus.Success}, actual {status}")

    try:
        if trx.details.method_id is None:
            raise ValueError("invalid method: None")
    except Exception as e:
        raise InvalidTransaction(f"failed to find method id: {str(e)}")


TronGrid_parser_lookup = ParserLookup.from_parser_list(parser_list, pre_condition_assert=pre_condition_assert)
