from abc import ABC

from dto.Infura.transaction import TrxDto
from parser.Infura.defn_currency import Infura_currency_lookup
from parser.base import BaseParser
from parser.currency import Currency


class InfuraParser(BaseParser[TrxDto], ABC):
    @property
    def major_currency(self) -> Currency:
        return Infura_currency_lookup.name_to_currency("Ether")
