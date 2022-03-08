from __future__ import annotations
from typing import List, Sequence

from models.exceptions import CurrencyNotFound
from parser.currency import Currency


class CurrencyLookup:
    def __init__(self) -> None:
        self.currency_list: List[Currency] = []

    def add_currency(self, c: Currency) -> CurrencyLookup:
        self.currency_list.append(c)
        return self

    def name_to_currency(self, name: str) -> Currency:
        return next(i for i in self.currency_list if i.name == name)

    def contract_address_to_currency(self, addr: str) -> Currency:
        try:
            return next(i for i in self.currency_list if i.contract_address == addr)
        except StopIteration:
            raise CurrencyNotFound(f"cannot find currency of {addr}")

    @staticmethod
    def from_currency_list(currency_list: Sequence[Currency]) -> CurrencyLookup:
        currency_lookup = CurrencyLookup()
        for c in currency_list:
            currency_lookup.add_currency(c)

        return currency_lookup
