from abc import ABC

from dto.TronGrid.transaction import TrxDto
from parser.TronGrid.defn_currency import TronGrid_currency_lookup
from parser.base import BaseParser
from parser.currency import Currency


class TronGridParser(BaseParser[TrxDto], ABC):
    @property
    def major_currency(self) -> Currency:
        return TronGrid_currency_lookup.name_to_currency("TRXToken")
