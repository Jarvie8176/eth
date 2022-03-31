from __future__ import annotations

from datetime import datetime
from dateutil import tz as tzlib
from enum import Enum
from typing import Optional, List

from pydantic import Field
from pydantic.main import BaseModel
from dto.price import PriceDto
from parser.currency import Currency


class CsvDto(BaseModel):
    timestamp: Optional[str] = Field(alias="Timestamp")  # YYYY-MM-DD hh:mm:ss (in PST)
    type: Optional[str] = Field(alias="Type")
    in_amount: Optional[str] = Field(alias="IN Amount")
    in_currency: Optional[str] = Field(alias="IN Currency")
    in_amount_usd: Optional[str] = Field(alias="IN Amount (USD)")  # if type is Dividend
    out_amount: Optional[str] = Field(alias="Out Amount")
    out_currency: Optional[str] = Field(alias="Out Currency")
    out_amount_usd: Optional[str] = Field(alias="Out Amount (USD)")  # if type is Dividend
    fee_amount: Optional[str] = Field(alias="Fee Amount")
    fee_currency: Optional[str] = Field(alias="Fee Currency")
    transaction_id: str = Field(alias="Transaction ID")

    class Config:
        allow_population_by_field_name = True

    @staticmethod
    def from_parsed_trx(trx: ParsedTrx) -> CsvDto:  # todo
        timestamp = trx.readable_timestamp(trx.timestamp)
        type = trx.type
        in_amount = trx.in_payload.readable_amount if trx.in_payload else None
        in_currency = trx.in_payload.currency.unit if trx.in_payload and trx.in_payload.currency else None
        out_amount = trx.out_payload.readable_amount if trx.out_payload else None
        out_currency = trx.out_payload.currency.unit if trx.out_payload and trx.out_payload.currency else None
        fee_amount = trx.fee_payload.readable_amount if trx.fee_payload else None
        fee_currency = trx.fee_payload.currency.unit if trx.fee_payload and trx.fee_payload.currency else None
        in_amount_usd = trx.in_payload.price.to_usd(
            trx.in_payload.readable_amount) if trx.in_payload and trx.in_payload.price else None
        out_amount_usd = trx.out_payload.price.to_usd(
            trx.out_payload.readable_amount) if trx.out_payload and trx.out_payload.price else None

        result = CsvDto(timestamp=timestamp,
                        type=type,
                        in_amount=in_amount,
                        in_currency=in_currency,
                        in_amount_usd=in_amount_usd,
                        out_amount=out_amount,
                        out_currency=out_currency,
                        out_amount_usd=out_amount_usd,
                        fee_amount=fee_amount,
                        fee_currency=fee_currency,
                        transaction_id=trx.trx_id)
        return result


class ParsedTrxDto(BaseModel):
    trx_id: str
    url: str
    type: str
    status: str
    timestamp: str
    in_amount: Optional[str]
    in_amount_major: Optional[str]
    in_currency: Optional[str]
    in_rate: Optional[str]
    in_rate_unit: Optional[str]
    in_rate_timestamp: Optional[str]
    out_amount: Optional[str]
    out_amount_major: Optional[str]
    out_currency: Optional[str]
    out_rate: Optional[str]
    out_rate_unit: Optional[str]
    out_rate_timestamp: Optional[str]
    fee_amount: Optional[str]
    fee_currency: Optional[str]
    fee_rate: Optional[str]
    fee_rate_unit: Optional[str]
    fee_rate_timestamp: Optional[str]


class ParsedTrxType(str, Enum):
    Dividend = "Dividend"
    Swap = "Swap"
    Transfer = "Transfer"
    Sell = "Sell"
    Buy = "Buy"
    Withdraw = "Withdraw"


class ParsedTrxStatus(str, Enum):
    Success = "SUCCESS"
    Fail = "FAIL"


class TrxPayload(BaseModel):
    value: str
    value_major: Optional[str] = Field(description="equivalent value in major currency (e.g. TRX or ETH); "
                                                   "None if there is not parsable (e.g. rewards)")
    currency: Currency
    price: Optional[PriceDto]

    @property
    def unit(self) -> str:
        return self.currency.unit

    @property
    def readable_amount(self) -> str:
        return self.currency.to_readable_value(self.value)


class ParsedTrx(BaseModel):
    trx_id: str
    url: str
    type: ParsedTrxType
    status: ParsedTrxStatus
    timestamp: datetime
    major_currency: Currency
    in_payload: Optional[TrxPayload]
    out_payload: Optional[TrxPayload]
    fee_payload: Optional[TrxPayload]

    @staticmethod
    def readable_timestamp(timestamp: datetime) -> str:
        tz = tzlib.gettz('America/Vancouver')  # todo: configurable
        return timestamp.astimezone(tz).strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def iso_timestamp(timestamp: datetime) -> str:
        return timestamp.isoformat()

    def _payload_to_readable_major_amount(self, payload: TrxPayload) -> Optional[str]:
        value = payload.value_major
        return None if value is None else self.major_currency.to_readable_value(value)

    def to_dto(self) -> ParsedTrxDto:
        result = ParsedTrxDto(trx_id=self.trx_id,
                              url=self.url,
                              type=self.type,
                              status=self.status,
                              timestamp=self.iso_timestamp(self.timestamp))

        in_payload = self.in_payload
        if in_payload:
            result.in_amount = in_payload.readable_amount
            result.in_amount_major = self._payload_to_readable_major_amount(in_payload)
            result.in_currency = in_payload.currency.unit

            in_price_dto = in_payload.price
            if in_price_dto:
                result.in_rate = in_price_dto.close
                result.in_rate_unit = in_price_dto.symbol
                result.in_rate_timestamp = self.iso_timestamp(in_price_dto.timestamp)

        out_payload = self.out_payload
        if out_payload:
            result.out_amount = out_payload.readable_amount
            result.out_amount_major = self._payload_to_readable_major_amount(out_payload)
            result.out_currency = out_payload.currency.unit

            out_price_dto = out_payload.price
            if out_price_dto:
                result.out_rate = out_price_dto.close
                result.out_rate_unit = out_price_dto.symbol
                result.out_rate_timestamp = self.iso_timestamp(out_price_dto.timestamp)

        fee_payload = self.fee_payload
        if fee_payload:
            result.fee_amount = fee_payload.readable_amount
            result.fee_currency = fee_payload.currency.unit

            fee_price_dto = fee_payload.price
            if fee_price_dto:
                result.fee_rate = fee_price_dto.close
                result.fee_rate_unit = fee_price_dto.symbol
                result.fee_rate_timestamp = self.iso_timestamp(fee_price_dto.timestamp)

        return result

    def to_csv_dto(self) -> List[CsvDto]:
        """
        converts to final output schema
        :return:
        """
        decomposed_dtos = self._parsed_dto_decompose()
        return [CsvDto.from_parsed_trx(dto) for dto in decomposed_dtos]

    def _get_amount_major(self) -> Optional[str]:
        """
        :return:
        """

        return None

    def _parsed_dto_decompose(self) -> List[ParsedTrx]:
        """
        breaks composite dto into individual records
        :return:
        """

        major_payload = self.in_payload if self.in_payload and self.in_payload.price and self.in_payload.currency == self.major_currency else self.out_payload
        major_amount = major_payload.readable_amount if major_payload else None
        usd_amount = major_payload.price.to_usd(
            major_amount) if major_payload and major_payload.price and major_amount else None
        usd_currency = Currency(name="USD", unit="USD", decimal_places=0, contract_address="")
        usd_payload = TrxPayload(value=usd_amount,
                                 currency=usd_currency) if usd_amount is not None and usd_currency is not None else None

        if self.type in [ParsedTrxType.Transfer, ParsedTrxType.Withdraw]:
            return []

        if self.type in [ParsedTrxType.Buy, ParsedTrxType.Sell, ParsedTrxType.Dividend]:
            return [self]

        if self.type == ParsedTrxType.Swap:
            sell_dto = ParsedTrx(**self.dict())
            sell_dto.type = ParsedTrxType.Sell
            sell_dto.in_payload = usd_payload

            buy_dto = ParsedTrx(**self.dict())
            buy_dto.type = ParsedTrxType.Buy
            buy_dto.out_payload = usd_payload
            buy_dto.fee_payload = None

            return sell_dto._parsed_dto_decompose() + buy_dto._parsed_dto_decompose()

        raise ValueError(f"transaction type has no decompose logic: {self.type}")
