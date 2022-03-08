from datetime import datetime
from typing import List

import pytz
from loguru import logger

from dto.TronGrid.contractType import ContractType
from dto.TronGrid.transaction import TrxDto
from dto.parsedTrx import ParsedTrx, TrxPayload, ParsedTrxType
from parser.TronGrid.defn_currency import TronGrid_currency_lookup
from parser.TronGrid.parser_base import TronGridParser


class Parser(TronGridParser):
    """
    default parser for transfer transactions
    example: https://tronscan.org/#/transaction/71c897f361a164af3d627ea3ef14479c4da16ba805020b279af1d694fce7ec3e
    """

    def can_handle(self, trx: TrxDto) -> bool:
        try:
            contract = trx.get_contract()
            if not contract:
                return False

            if trx.events.meta.page_size != 1:
                return False

            contract_type = contract.type

            is_smart_contract = contract_type == ContractType.TriggerSmartContract
            has_valid_sigs = "transfer" in trx.events.get_event_by_index(0).event_name.lower().lower()

            return is_smart_contract and has_valid_sigs

        except Exception as e:
            logger.warning(f"failed to parse contract: {e}")
            return False

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        out_contract_addr = trx.events.get_event_by_index(0).contract_address

        event = trx.events.get_event_by_index(0)

        out_currency = TronGrid_currency_lookup.contract_address_to_currency(out_contract_addr)
        if not out_currency:
            raise ValueError(f"cannot find reward currency: {out_contract_addr}")

        out_amount = event.result.get("value")
        if out_amount is None:
            out_amount = event.result.get("wad")
            if out_amount is None:
                raise ValueError("cannot find in amount")

        fee_currency = self.major_currency
        fee_amount = str(trx.info.fee)

        return [ParsedTrx(
            trx_id=trx.trx_id,
            url=f"https://tronscan.org/#/transaction/{trx.trx_id}",
            type=ParsedTrxType.Transfer,
            status=trx.status,
            timestamp=datetime.fromtimestamp(trx.info.blockTimeStamp / 1000,
                                             tz=pytz.UTC),
            major_currency=self.major_currency,
            out_payload=TrxPayload(value=out_amount,
                                   currency=out_currency),
            fee_payload=TrxPayload(value=fee_amount,
                                   currency=fee_currency))]
