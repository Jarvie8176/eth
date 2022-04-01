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
    default parser for remove liquidity
    example: https://tronscan.org/#/transaction/2233a3c9dd5b591d5742221ffa479987c1e5f00ba756feec493cae9d41fc0d63
    """

    def can_handle(self, trx: TrxDto) -> bool:
        return trx.details.method_id == "f88bf15a"

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        remove_liquidity_event = self.find_remove_liquidity_event(trx)
        if not remove_liquidity_event:
            raise ValueError("cannot find remove liquidity event")

        transfer_in_events = self.find_all_transfer_in_logs(trx)

        trx_in_value = remove_liquidity_event.result.get("trx_amount")
        token_amount = remove_liquidity_event.result.get("token_amount")

        token_in_event = None
        for event in transfer_in_events:
            if event.result.get("value") == token_amount or event.result.get("wad") == token_amount:
                token_in_event = event

        if not token_in_event:
            raise ValueError("remove liquidity event found but no matching token in event")

        trx_in_payload = TrxPayload(value=trx_in_value,
                                    value_major=trx_in_value,
                                    currency=self.major_currency)
        transfer_in_payload = TrxPayload(value=token_amount,
                                         currency=TronGrid_currency_lookup.contract_address_to_currency(
                                             token_in_event.contract_address))
        fee_payload = TrxPayload(value=str(trx.info.fee),
                                 currency=self.major_currency)

        return [ParsedTrx(trx_id=trx.trx_id,
                          url=f"https://tronscan.org/#/transaction/{trx.trx_id}",
                          type=ParsedTrxType.Buy,
                          status=trx.status,
                          timestamp=datetime.fromtimestamp(trx.info.blockTimeStamp / 1000, tz=pytz.UTC),
                          major_currency=self.major_currency,
                          in_payload=trx_in_payload,
                          fee_payload=fee_payload),
                ParsedTrx(trx_id=trx.trx_id,
                          url=f"https://tronscan.org/#/transaction/{trx.trx_id}",
                          type=ParsedTrxType.Buy,
                          status=trx.status,
                          timestamp=datetime.fromtimestamp(trx.info.blockTimeStamp / 1000, tz=pytz.UTC),
                          major_currency=self.major_currency,
                          in_payload=transfer_in_payload)]

    def find_in_trx_log(self, trx: TrxDto) -> Optional[EventDataDto]:
        return self.find_second_transfer_in_log(trx)
