import bisect
import csv
from datetime import datetime
from typing import Dict, List, Any

import pytz

from dto.price import PriceDto
from priceLookup.base import BasePriceLookup


class TRXPriceLookup(BasePriceLookup):
    @property
    def unit(self) -> str:
        return "TRON"

    def __init__(self, source_file_path: str):
        super()
        self.price_data: List[PriceDto] = []
        self.source_file_path = source_file_path
        self.load()

    def load(self) -> None:
        """
        loads price data from csv, parse into a sorted list of price records in ascending order (first is earliest)
        """
        with open(self.source_file_path, "r") as f:
            reader = csv.DictReader(f)
            self.price_data = list(map(self._csv_row_to_trx_price_dto, reader))
            self.price_data.sort(key=lambda x: x.timestamp, reverse=False)

    @staticmethod
    def _csv_row_to_trx_price_dto(row: Dict[str, Any]) -> PriceDto:
        row_unix = int(row["unix"])
        unix_time_in_sec = row_unix / 1000 if row_unix > 32503680000 else row_unix  # 3000-01-01
        timestamp = datetime.fromtimestamp(unix_time_in_sec, tz=pytz.UTC)
        symbol = row["symbol"]
        close = row["close"]
        return PriceDto(timestamp=timestamp, symbol=symbol, close=close)

    def time_to_price(self, timestamp: datetime) -> PriceDto:
        candidate = PriceDto(timestamp=timestamp, symbol="", close="")
        left_idx = bisect.bisect_left(self.price_data, candidate)
        left_idx = left_idx - 1  # shift to the actual left, not insert place
        right_idx = max(min(len(self.price_data) - 1, left_idx + 1), 0)

        left = self.price_data[left_idx]
        right = self.price_data[right_idx]

        closest = left if abs(timestamp - left.timestamp) < abs(
            timestamp - right.timestamp) else right

        return closest
