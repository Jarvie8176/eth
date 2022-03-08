from typing import List

from parser.TronGrid import parser_dividend_1c4b774b, parser_swap_4bf3e2d0, \
    parser_dividend_7f8661a1, parser_swap_999bb7ac, parser_transfer_a9059cbb, parser_swap_b040d545, parser_swap_ddf7e1a7
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

TronGrid_parser_lookup = ParserLookup.from_parser_list(parser_list)
