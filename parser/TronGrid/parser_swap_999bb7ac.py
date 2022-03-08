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
    default parser for swap transactions (trx purchase)
    example: https://tronscan.org/#/transaction/807e5694ea2397c8f874830c22ab30c41fe23e74f6f8dc59c68b1866486241f9
    """

    def can_handle(self, trx: TrxDto) -> bool:
        try:
            contract = trx.get_contract()
            if not contract:
                return False

            if trx.events.meta.page_size != 4:
                return False

            contract_type = contract.type

            is_smart_contract = contract_type == ContractType.TriggerSmartContract
            has_valid_sigs = "transfer" in trx.events.get_event_by_index(0).event_name.lower().lower() and \
                             "approval" in trx.events.get_event_by_index(1).event_name.lower() and \
                             "trxpurchase" in trx.events.get_event_by_index(2).event_name.lower() and \
                             "snapshot" in trx.events.get_event_by_index(3).event_name.lower()

            return is_smart_contract and has_valid_sigs

        except Exception as e:
            logger.warning(f"failed to parse contract: {e}")
            return False

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        in_contract_addr = trx.events.get_event_by_index(0).contract_address

        event = trx.events.get_event_by_index(2)

        in_currency = self.major_currency
        if not in_currency:
            raise ValueError(f"cannot find in currency: {in_contract_addr}")
        in_amount = event.result.get("trx_bought")
        if in_amount is None:
            raise ValueError("cannot find in amount")

        out_currency = TronGrid_currency_lookup.contract_address_to_currency(in_contract_addr)
        out_amount = event.result.get("tokens_sold")
        if out_amount is None:
            raise ValueError("cannot find out amount")

        fee_currency = self.major_currency
        fee_amount = str(trx.info.fee)

        return [ParsedTrx(
            trx_id=trx.trx_id,
            url=f"https://tronscan.org/#/transaction/{trx.trx_id}",
            type=ParsedTrxType.Swap,
            status=trx.status,
            timestamp=datetime.fromtimestamp(trx.info.blockTimeStamp / 1000,
                                             tz=pytz.UTC),
            major_currency=self.major_currency,
            in_payload=TrxPayload(value=in_amount,
                                  value_major=in_amount,
                                  currency=in_currency
                                  ),
            out_payload=TrxPayload(value=out_amount,
                                   value_major=in_amount,
                                   currency=out_currency),
            fee_payload=TrxPayload(value=fee_amount,
                                   currency=fee_currency))]
