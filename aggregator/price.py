from __future__ import annotations
from typing import List, Optional

from loguru import logger
from pydantic.main import BaseModel

from dto.parsedTrx import ParsedTrx
from priceLookup.base import BasePriceLookup
from priceLookup.eth import ETHPriceLookup
from priceLookup.trx import TRXPriceLookup


class PriceAggregatorCreateOptions(BaseModel):
    trx_price_data_file_path: Optional[str]
    eth_price_data_file_path: Optional[str]


class PriceAggregator:
    def __init__(self) -> None:
        self.price_lookups: List[BasePriceLookup] = []

    def add_price_lookup(self, price_lookup: BasePriceLookup) -> PriceAggregator:
        logger.debug(f"adding price lookup for {price_lookup.unit}")
        self.price_lookups.append(price_lookup)
        return self

    def update_price(self, parsed_trx: ParsedTrx) -> ParsedTrx:
        timestamp = parsed_trx.timestamp

        if parsed_trx.in_payload:
            in_price_lookup = self._find_price_lookup_by_unit(
                parsed_trx.in_payload.unit)
            if in_price_lookup:
                parsed_trx.in_payload.price = in_price_lookup.time_to_price(timestamp)

        if parsed_trx.out_payload:
            out_price_lookup = self._find_price_lookup_by_unit(
                parsed_trx.out_payload.unit)
            if out_price_lookup:
                parsed_trx.out_payload.price = out_price_lookup.time_to_price(timestamp)

        if parsed_trx.fee_payload:
            fee_price_lookup = self._find_price_lookup_by_unit(
                parsed_trx.fee_payload.unit)
            if fee_price_lookup:
                parsed_trx.fee_payload.price = fee_price_lookup.time_to_price(timestamp)

        return parsed_trx

    def _find_price_lookup_by_unit(self, unit: str) -> Optional[BasePriceLookup]:
        try:
            return next(i for i in self.price_lookups if i.unit == unit)
        except StopIteration:
            return None

    @staticmethod
    def create(options: PriceAggregatorCreateOptions) -> PriceAggregator:
        price_aggregator = PriceAggregator()

        if options.trx_price_data_file_path:
            price_aggregator.add_price_lookup(TRXPriceLookup(options.trx_price_data_file_path))

        if options.eth_price_data_file_path:
            price_aggregator.add_price_lookup(ETHPriceLookup(options.eth_price_data_file_path))

        return price_aggregator
