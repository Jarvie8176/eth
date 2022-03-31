from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel


class PriceDto(BaseModel):
    timestamp: datetime
    symbol: str
    close: str

    def __lt__(self, other: PriceDto) -> bool:
        return self.timestamp < other.timestamp

    def to_usd(self, amount: str) -> str:
        """
        converts the amount to USD. todo: it assumes symbols are other_currency / USD
        :param amount:
        :return:
        """
        return str(float(amount) * float(self.close))
