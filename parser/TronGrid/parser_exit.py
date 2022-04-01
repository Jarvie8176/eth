from datetime import datetime
from typing import List

import pytz

from dto.TronGrid.event import EventDataDto
from dto.TronGrid.transaction import TrxDto
from dto.parsedTrx import ParsedTrx, ParsedTrxType, TrxPayload
from parser.TronGrid.defn_currency import TronGrid_currency_lookup
from parser.TronGrid.parser_base import TronGridParser


class Parser(TronGridParser):
    """
    default parser for exit with dividend
    example:
        https://tronscan.org/#/transaction/4a8ba22b8c11f73e96a2132d67461283ff8cfdbe9d7cdfcb77bf46f17ee897b2
        https://tronscan.org/#/transaction/a6cf21b3e25047fb54ce13309a789e9f7d3976266826a8efa25981941894dcf8
    """

    def can_handle(self, trx: TrxDto) -> bool:
        return trx.details.method_id == "e9fad8ee"

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        in_trx_log = self.find_in_trx_log(trx)
        in_payload = TrxPayload(value=in_trx_log.result.get("value"),
                                currency=TronGrid_currency_lookup.contract_address_to_currency(
                                    in_trx_log.contract_address))
        fee_payload = TrxPayload(value=str(trx.info.fee),
                                 currency=self.major_currency)

        return [ParsedTrx(
            trx_id=trx.trx_id,
            url=f"https://tronscan.org/#/transaction/{trx.trx_id}",
            type=ParsedTrxType.Dividend,
            status=trx.status,
            timestamp=datetime.fromtimestamp(trx.info.blockTimeStamp / 1000, tz=pytz.UTC),
            major_currency=self.major_currency,
            in_payload=in_payload,
            fee_payload=fee_payload)]

    def find_in_trx_log(self, trx: TrxDto) -> EventDataDto:
        with_draw_currency_addrs = [TronGrid_currency_lookup.name_to_currency("Tether_USD").contract_address,
                                    TronGrid_currency_lookup.name_to_currency("JUST_Stablecoin").contract_address]
        # TronGrid_currency_lookup.name_to_currency("TRON").contract_address]
        transfer_in_logs = self.find_all_transfer_in_logs(trx)
        transfer_with_withdraw_currency = None
        transfer_dividend = None
        for log in transfer_in_logs:
            if log.contract_address in with_draw_currency_addrs:
                transfer_with_withdraw_currency = log
            else:
                transfer_dividend = log
        if not transfer_with_withdraw_currency:
            raise ValueError("exit but no transfer of withdraw currency found")
        if not transfer_dividend:
            raise ValueError("exit but no transfer of dividend found")
        return transfer_dividend
