from typing import Optional

from parser.tronGrid.currency import Currency


trx_token = Currency(
    decimal_places=6, unit="TRON",
    contract_address="")

gold_coin_token = Currency(
    decimal_places=6, unit="GOLD",
    contract_address="TQs33VBR68syFx93KQ9iYSg8Xyr68t3A3L")

currency_defn = {
    "trx_token": trx_token,
    "gold_coin_token": gold_coin_token
}


def contract_address_to_currency(addr: str) -> Optional[Currency]:
    try:
        return next(i for i in currency_defn.values() if i.contract_address == addr)
    except StopIteration:
        return None
