from typing import List

from dto.Infura.transaction import TrxDto
from parser.Infura import parser_swapETHForExactTokens, parser_swapExactTokensForETH, parser_swapTokensForExactTokens, \
    parser_addLiquidityETH, parser_removeLiquidityETHWithPermit, parser_withdraw, \
    parser_claim, parser_claim_0x4e71d92d, parser_withdraw_0x441a3e70
from parser.Infura.parser_base import InfuraParser
from parser.parserLookup import ParserLookup

parser_list: List[InfuraParser] = [
    parser_swapETHForExactTokens.Parser(),
    parser_swapExactTokensForETH.Parser(),
    parser_swapTokensForExactTokens.Parser(),
    parser_addLiquidityETH.Parser(),
    parser_removeLiquidityETHWithPermit.Parser(),
    parser_withdraw.Parser(),
    parser_withdraw_0x441a3e70.Parser(),
    parser_claim.Parser(),
    parser_claim_0x4e71d92d.Parser(),
]

Infura_parser_lookup: ParserLookup[TrxDto] = ParserLookup.from_parser_list(parser_list)
