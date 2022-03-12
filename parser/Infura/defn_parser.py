from typing import List

from dto.Infura.transaction import TrxDto
from dto.parsedTrx import ParsedTrxStatus
from parser.Infura import parser_swapETHForExactTokens, parser_swapExactTokensForETH, parser_swapTokensForExactTokens, \
    parser_addLiquidityETH, parser_removeLiquidityETHWithPermit, parser_withdraw, \
    parser_claim, parser_claim_0x4e71d92d, parser_withdraw_0x441a3e70, parser_swapExactTokensForTokens, \
    parser_swapTokensForExactETH, parser_hardcoded, parser_getReward, parser_deposit
from parser.Infura.defn_status import parse_status
from parser.Infura.parser_base import InfuraParser
from parser.parserLookup import ParserLookup

parser_list: List[InfuraParser] = [
    parser_swapETHForExactTokens.Parser(),
    parser_swapTokensForExactETH.Parser(),
    parser_swapTokensForExactTokens.Parser(),
    parser_swapExactTokensForETH.Parser(),
    parser_swapExactTokensForTokens.Parser(),

    parser_addLiquidityETH.Parser(),
    parser_removeLiquidityETHWithPermit.Parser(),
    parser_withdraw.Parser(),
    parser_withdraw_0x441a3e70.Parser(),
    parser_claim.Parser(),
    parser_claim_0x4e71d92d.Parser(),
    parser_hardcoded.Parser(),
    parser_getReward.Parser(),
    parser_deposit.Parser(),
]


def pre_condition_assert(trx: TrxDto) -> None:
    status = parse_status(trx.receipt.status)
    if ParsedTrxStatus.Success != status:
        raise ValueError(f"invalid status: expected {ParsedTrxStatus.Success}, actual {status}")


Infura_parser_lookup: ParserLookup[TrxDto] = ParserLookup.from_parser_list(parser_list,
                                                                           pre_condition_assert=pre_condition_assert)
