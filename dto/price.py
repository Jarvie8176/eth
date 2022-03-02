from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel


class PriceDto(BaseModel):
    timestamp: datetime
    symbol: str
    close: str

    def __lt__(self, other: PriceDto) -> bool:
        return self.timestamp < other.timestamp
