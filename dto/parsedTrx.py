from pydantic.main import BaseModel


class ParsedTrx(BaseModel):
    trx_id: str
    url: str
    type: str
    status: str
    timestamp: str
    in_amount: str
    in_currency: str
    fee_amount: str
    fee_currency: str
