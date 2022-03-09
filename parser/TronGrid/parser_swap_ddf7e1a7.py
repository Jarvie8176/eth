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
    parser for specific swap transactions (swap between non-TRON)
    example: https://tronscan.org/#/transaction/90713085085541744d004caeac9810e8e51e5f45941f1ffc988ad03a4e6b2d7a
    """

    def can_handle(self, trx: TrxDto) -> bool:
        try:
            contract = trx.get_contract()
            if not contract:
                return False

            if trx.events.meta.page_size != 7:
                return False

            contract_type = contract.type

            is_smart_contract = contract_type == ContractType.TriggerSmartContract
            has_valid_sigs = "transfer" in trx.events.get_event_by_index(0).event_name.lower() and \
                             "approval" in trx.events.get_event_by_index(1).event_name.lower() and \
                             "transfer" in trx.events.get_event_by_index(2).event_name.lower() and \
                             "tokenpurchase" in trx.events.get_event_by_index(3).event_name.lower() and \
                             "snapshot" in trx.events.get_event_by_index(4).event_name.lower() and \
                             "trxpurchase" in trx.events.get_event_by_index(5).event_name.lower() and \
                             "snapshot" in trx.events.get_event_by_index(6).event_name.lower()

            return is_smart_contract and has_valid_sigs and self.assert_log_length(trx, 7)
        except Exception as e:
            logger.warning(f"failed to parse contract: {e}")
        return False

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        in_event = trx.events.get_event_by_index(2)
        in_contract_addr = in_event.contract_address
        in_currency = TronGrid_currency_lookup.contract_address_to_currency(in_contract_addr)
        in_amount = in_event.result.get("value")
        if in_amount is None:
            in_amount = in_event.result.get("wad")
            if in_amount is None:
                raise ValueError("cannot find in amount")

        out_event = trx.events.get_event_by_index(0)
        out_contract_addr = out_event.contract_address
        out_currency = TronGrid_currency_lookup.contract_address_to_currency(out_contract_addr)
        if not out_currency:
            raise ValueError(f"cannot find reward currency: {out_contract_addr}")

        out_amount = out_event.result.get("value")
        if out_amount is None:
            out_amount = out_event.result.get("wad")
            if out_amount is None:
                raise ValueError("cannot find in amount")

        fee_currency = self.major_currency
        fee_amount = str(trx.info.fee)

        value_equiv_event = trx.events.get_event_by_index(3)
        value_equiv_amount = value_equiv_event.result.get("trx_sold")

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
