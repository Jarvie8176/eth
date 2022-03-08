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
    default parser for swap transactions (swap between non-TRON)
    example: https://tronscan.org/#/transaction/a107cc9748e755c579f46df1b0319cb9c6be01e099d771bf43e15d2b28912b35
    """

    def can_handle(self, trx: TrxDto) -> bool:
        try:
            contract = trx.get_contract()
            if not contract:
                return False

            if trx.events.meta.page_size != 6:
                return False

            contract_type = contract.type

            is_smart_contract = contract_type == ContractType.TriggerSmartContract
            has_valid_sigs = "transfer" in trx.events.get_event_by_index(0).event_name.lower() and \
                             "transfer" in trx.events.get_event_by_index(1).event_name.lower() and \
                             "tokenpurchase" in trx.events.get_event_by_index(2).event_name.lower() and \
                             "snapshot" in trx.events.get_event_by_index(3).event_name.lower() and \
                             "trxpurchase" in trx.events.get_event_by_index(4).event_name.lower() and \
                             "snapshot" in trx.events.get_event_by_index(5).event_name.lower()

            return is_smart_contract and has_valid_sigs

        except Exception as e:
            logger.warning(f"failed to parse contract: {e}")
            return False

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        in_event = trx.events.get_event_by_index(1)
        out_event = trx.events.get_event_by_index(0)
        value_equiv_event = trx.events.get_event_by_index(2)

        in_amount = in_event.result.get("value")
        if in_amount is None:
            in_amount = in_event.result.get("wad")
            if in_amount is None:
                raise ValueError("cannot find in amount")
        out_amount = out_event.result.get("value")
        if out_amount is None:
            out_amount = out_event.result.get("wad")
            if out_amount is None:
                raise ValueError("cannot find in amount")
        value_equiv_amount = value_equiv_event.result.get("trx_sold")
        if value_equiv_amount is None:
            raise ValueError("cannot find amount of major currency")

        in_contract_addr = in_event.contract_address
        out_contract_addr = out_event.contract_address

        in_currency = TronGrid_currency_lookup.contract_address_to_currency(in_contract_addr)
        out_currency = TronGrid_currency_lookup.contract_address_to_currency(out_contract_addr)

        if not in_currency:
            raise ValueError(f"cannot find in currency: {in_contract_addr}")
        if not out_currency:
            raise ValueError(f"cannot find out currency: {out_contract_addr}")

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
                                  value_major=value_equiv_amount,
                                  currency=in_currency
                                  ),
            out_payload=TrxPayload(value=out_amount,
                                   value_major=value_equiv_amount,
                                   currency=out_currency),
            fee_payload=TrxPayload(value=fee_amount,
                                   currency=fee_currency))]
