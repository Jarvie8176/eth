from datetime import datetime
from typing import List, Optional

import pytz

from dto.TronGrid.event import EventDataDto
from dto.TronGrid.transaction import TrxDto
from dto.parsedTrx import ParsedTrx, ParsedTrxType, TrxPayload
from parser.TronGrid.defn_currency import TronGrid_currency_lookup
from parser.TronGrid.parser_base import TronGridParser


class Parser(TronGridParser):
    """
    default parser for add liquidity (sell)
    example: https://tronscan.org/#/transaction/bcf3eecd204aed9bd4312e2e41edc2428209ef0aaca881fcccd4c486bb33fb0f
    """

    def can_handle(self, trx: TrxDto) -> bool:
        return trx.details.method_id == "422f1043"

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        add_liquidity_event = self.find_add_liquidity_event(trx)
        if not add_liquidity_event:
            raise ValueError("cannot find add liquidity event")

        transfer_out_events = self.find_all_transfer_out_logs(trx)

        trx_out_value = add_liquidity_event.result.get("trx_amount")
        token_amount = add_liquidity_event.result.get("token_amount")

        token_out_event = None
        for event in transfer_out_events:
            if event.result.get("value") == token_amount or event.result.get("wad") == token_amount:
                token_out_event = event

        if not token_out_event:
            raise ValueError("add liquidity event found but no matching token out event")

        trx_out_payload = TrxPayload(value=trx_out_value,
                                     value_major=trx_out_value,
                                     currency=self.major_currency)
        transfer_out_payload = TrxPayload(value=token_amount,
                                          currency=TronGrid_currency_lookup.contract_address_to_currency(
                                              token_out_event.contract_address))
        fee_payload = TrxPayload(value=str(trx.info.fee),
                                 currency=self.major_currency)

        return [ParsedTrx(trx_id=trx.trx_id,
                          url=f"https://tronscan.org/#/transaction/{trx.trx_id}",
                          type=ParsedTrxType.Sell,
                          status=trx.status,
                          timestamp=datetime.fromtimestamp(trx.info.blockTimeStamp / 1000, tz=pytz.UTC),
                          major_currency=self.major_currency,
                          out_payload=trx_out_payload,
                          fee_payload=fee_payload),
                ParsedTrx(trx_id=trx.trx_id,
                          url=f"https://tronscan.org/#/transaction/{trx.trx_id}",
                          type=ParsedTrxType.Sell,
                          status=trx.status,
                          timestamp=datetime.fromtimestamp(trx.info.blockTimeStamp / 1000, tz=pytz.UTC),
                          major_currency=self.major_currency,
                          out_payload=transfer_out_payload)]

    def find_out_trx_log(self, trx: TrxDto) -> Optional[EventDataDto]:
        return self.find_first_transfer_out_log(trx)
