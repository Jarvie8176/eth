from typing import List

from dto.Infura.transaction import TrxDto
from dto.parsedTrx import ParsedTrxStatus
from parser.Infura import parser_swapETHForExactTokens, parser_swapExactTokensForETH, parser_swapTokensForExactTokens, \
    parser_addLiquidityETH, parser_removeLiquidityETHWithPermit, \
    parser_claim, parser_claim_0x4e71d92d, parser_withdraw, parser_swapExactTokensForTokens, \
    parser_swapTokensForExactETH, parser_hardcoded, parser_getReward, parser_deposit, parser_skipped, \
    parser_remove_liquidity_one_coin, parser_removeLiquidityWithPermit, parser_removeLiquidityOneToken, \
    parser_swapExactETHForTokens, parser_leaveStaking, parser_addLiquidity
from parser.Infura.defn_status import parse_status
from parser.Infura.parser_base import InfuraParser
from parser.parserLookup import ParserLookup

parser_list: List[InfuraParser] = [
    parser_hardcoded.Parser(),
    parser_skipped.Parser(),

    parser_claim.Parser(),
    parser_claim_0x4e71d92d.Parser(),
    parser_getReward.Parser(),

    parser_addLiquidity.Parser(),
    parser_addLiquidityETH.Parser(),

    parser_remove_liquidity_one_coin.Parser(),
    parser_removeLiquidityOneToken.Parser(),
    parser_removeLiquidityWithPermit.Parser(),
    parser_removeLiquidityETHWithPermit.Parser(),

    parser_swapETHForExactTokens.Parser(),
    parser_swapTokensForExactETH.Parser(),
    parser_swapTokensForExactTokens.Parser(),
    parser_swapExactTokensForETH.Parser(),
    parser_swapExactETHForTokens.Parser(),
    parser_swapExactTokensForTokens.Parser(),

    parser_withdraw.Parser(),
    parser_deposit.Parser(),
    parser_leaveStaking.Parser(),
]


def pre_condition_assert(trx: TrxDto) -> None:
    status = parse_status(trx.receipt.status)
    if ParsedTrxStatus.Success != status:
        raise ValueError(f"invalid status: expected {ParsedTrxStatus.Success}, actual {status}")


Infura_parser_lookup: ParserLookup[TrxDto] = ParserLookup.from_parser_list(parser_list,
                                                                           pre_condition_assert=pre_condition_assert)
