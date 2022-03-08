from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import Field
from pydantic.main import BaseModel
from dto.price import PriceDto
from parser.currency import Currency


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

    def _payload_to_readable_major_amount(self, payload: TrxPayload) -> Optional[str]:
        value = payload.value_major
        return None if value is None else self.major_currency.to_readable_value(value)

    def to_dto(self) -> ParsedTrxDto:
        result = ParsedTrxDto(trx_id=self.trx_id,
                              url=self.url,
                              type=self.type,
                              status=self.status,
                              timestamp=self.timestamp.isoformat())

        in_payload = self.in_payload
        if in_payload:
            result.in_amount = in_payload.readable_amount
            result.in_amount_major = self._payload_to_readable_major_amount(in_payload)
            result.in_currency = in_payload.currency.unit

            in_price_dto = in_payload.price
            if in_price_dto:
                result.in_rate = in_price_dto.close
                result.in_rate_unit = in_price_dto.symbol
                result.in_rate_timestamp = in_price_dto.timestamp.isoformat()

        out_payload = self.out_payload
        if out_payload:
            result.out_amount = out_payload.readable_amount
            result.out_amount_major = self._payload_to_readable_major_amount(out_payload)
            result.out_currency = out_payload.currency.unit

            out_price_dto = out_payload.price
            if out_price_dto:
                result.out_rate = out_price_dto.close
                result.out_rate_unit = out_price_dto.symbol
                result.out_rate_timestamp = out_price_dto.timestamp.isoformat()

        fee_payload = self.fee_payload
        if fee_payload:
            result.fee_amount = fee_payload.readable_amount
            result.fee_currency = fee_payload.currency.unit

            fee_price_dto = fee_payload.price
            if fee_price_dto:
                result.fee_rate = fee_price_dto.close
                result.fee_rate_unit = fee_price_dto.symbol
                result.fee_rate_timestamp = fee_price_dto.timestamp.isoformat()

        return result
