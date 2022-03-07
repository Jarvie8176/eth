from typing import Optional

from parser.TronGrid.currency import Currency

currency_list = [
    Currency(name="TRXToken",
             unit="TRON", decimal_places=6,
             contract_address=""),
    Currency(name="GOLDCoinToken",
             unit="GOLD", decimal_places=6,
             contract_address="TQs33VBR68syFx93KQ9iYSg8Xyr68t3A3L"),
    Currency(name="SUNOLD",
             unit="SUNOLD", decimal_places=18,
             contract_address="TKkeiboTkxXKJpbmVFbv4a8ov5rAfRDMf9"),
    Currency(name="TigSwap",
             unit="Tig", decimal_places=18,
             contract_address="THRBFeEwKUoREVJCFpLm7JF4ph24bZAVDG"),
    Currency(name="JUST_Stablecoin",
             unit="USDJ", decimal_places=18,
             contract_address="TMwFHYXLJaRUPeW6421aqXL4ZEzPRFGkGT"),
    Currency(name="Tether_USD",
             unit="USDT", decimal_places=6,
             contract_address="TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"),
    Currency(name="JUST",
             unit="JST", decimal_places=18,
             contract_address="TCFLL5dx5ZJdKnWuesXxi1VPwjLVmWZZy9"),
    Currency(name="HODL",
             unit="HODL", decimal_places=18,
             contract_address="TW8epJzhhPZkCjadUQWWvHFfNi344EkNef"),
    Currency(name="Blockcola_Token",
             unit="COLA", decimal_places=6,
             contract_address="TSNWgunSeGUQqBKK4bM31iLw3bn9SBWWTG"),
    Currency(name="TAI",
             unit="TAI", decimal_places=18,
             contract_address="TRwS7apsNdRGzMBfhB2hVC4RhqfubUYZ8P"),
    Currency(name="PEARL",
             unit="PEARL", decimal_places=18,
             contract_address="TGbu32VEGpS4kDmjrmn5ZZJgUyHQiaweoq"),
]


def name_to_currency(name: str) -> Currency:
    return next(i for i in currency_list if i.name == name)


def contract_address_to_currency(addr: str) -> Optional[Currency]:
    try:
        return next(i for i in currency_list if i.contract_address == addr)
    except StopIteration:
        return None
