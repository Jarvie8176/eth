import csv
from datetime import datetime
from typing import Any, Dict

import dateutil.parser
import pytz

from dto.price import PriceDto
from priceLookup.base import BasePriceLookup


class YahooPriceLookup(BasePriceLookup):
    @property
    def unit(self) -> str:
        raise NotImplementedError()

    @property
    def symbol(self) -> str:
        return f"{self.unit}/USD"

    def __init__(self, source_file_path: str):
        self.source_file_path = source_file_path
        super().__init__()
        self.load()

    def load(self) -> None:
        """
        loads price data from csv,
        then parse into a sorted list of price records
        in ascending order (first is earliest)
        """
        with open(self.source_file_path, "r") as f:
            reader = csv.DictReader(f)
            self.price_data = list(map(self._csv_row_to_price_dto, reader))
            self.price_data.sort(key=lambda x: x.timestamp, reverse=False)

    def _csv_row_to_price_dto(self, row: Dict[str, Any]) -> PriceDto:
        timestamp = dateutil.parser.parse(row["Date"]).replace(tzinfo=pytz.UTC)
        symbol = self.symbol
        close = row["Close"]
        return PriceDto(timestamp=timestamp, symbol=symbol, close=close)
