from pydantic import BaseModel


class Currency(BaseModel):
    unit: str
    decimal_places: int
    contract_address: str

    """
    adds decimal point to the appropriate place; add leading zeros if necessary
    """

    def to_readable_value(self, value: str) -> str:
        if value == "0" or self.decimal_places == 0:
            return value

        result = value.zfill(self.decimal_places + 1)
        insert_at = len(result) - self.decimal_places
        result = result[:insert_at] + "." + result[insert_at:]
        return result.rstrip("0")
