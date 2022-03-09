from abc import ABC

from dto.TronGrid.transaction import TrxDto
from models.exceptions import TrxLogLengthNotMatch
from parser.TronGrid.defn_currency import TronGrid_currency_lookup
from parser.base import BaseParser
from parser.currency import Currency


class TronGridParser(BaseParser[TrxDto], ABC):
    @property
    def major_currency(self) -> Currency:
        return TronGrid_currency_lookup.name_to_currency("TRXToken")

    def assert_log_length(self, trx: TrxDto, length: int) -> bool:
        log_len = len(trx.events.data)
        if length != log_len:
            raise TrxLogLengthNotMatch(f"expected log length: {length}; actual: {log_len}")
        return True
