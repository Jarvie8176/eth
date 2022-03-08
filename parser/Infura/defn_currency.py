from typing import List

from parser.currency import Currency
from parser.currencyLookup import CurrencyLookup

currency_list: List[Currency] = [
    Currency(name="Ether", unit="ETH", decimal_places=18,
             contract_address=""),
    Currency(name="Wrapped Ether", unit="ETH", decimal_places=18,
             contract_address="0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"),
    Currency(name="Serum", unit="SRM", decimal_places=6,
             contract_address="0x476c5e26a75bd202a9683ffd34359c0cc15be0ff"),
    Currency(name="dandy.dego", unit="DANDY", decimal_places=18,
             contract_address="0x9dfc4b433d359024eb3e810d77d60fbe8b0d9b82"),
    Currency(name="Tether_USD", unit="USDT", decimal_places=6,
             contract_address="0xdac17f958d2ee523a2206206994597c13d831ec7"),
    Currency(name="YFIEXCHANGE.FINANCE", unit="YFIE", decimal_places=18,
             contract_address="0x8f57e8e38e61975a0433fa792542f453d8ed4d7d"),
    Currency(name="BandToken", unit="BAND", decimal_places=18,
             contract_address="0xba11d00c5f74255f56a5e366f4f77f5a186d7f55"),
    Currency(name="SushiToken", unit="SUSHI", decimal_places=18,
             contract_address="0x6b3595068778dd592e39a122f4f5a5cf09c90fe2"),
    Currency(name="Uniswap", unit="UNI", decimal_places=18,
             contract_address="0x1f9840a85d5af5bf1d1762f925bdaddc4201f984"),
    Currency(name="Dai_Stablecoin", unit="DAI", decimal_places=18,
             contract_address="0x6b175474e89094c44da98b954eedeac495271d0f"),
    Currency(name="Curve_DAO_Token", unit="CRV", decimal_places=18,
             contract_address="0xd533a949740bb3306d119cc777fa900ba034cd52"),
    Currency(name="Cream", unit="CREAM", decimal_places=18,
             contract_address="0x2ba592f78db6436527729929aaf6c908497cb200"),
    Currency(name="Uniswap_V2", unit="UNI-V2", decimal_places=18,
             contract_address="0x59f96b8571e3b11f859a09eaf5a790a138fc64d0"),
    Currency(name="yearn.finance", unit="YFI", decimal_places=18,
             contract_address="0x0bc529c00c6401aef6d220be8c6ea1667f6ad93e"),
    Currency(name="YFII.finance", unit="YFII", decimal_places=18,
             contract_address="0xa1d0e215a23d7030842fc67ce582a6afa3ccab83"),
    Currency(name="UNIFI", unit="UNIFI", decimal_places=18,
             contract_address="0x0ef3b2024ae079e6dbc2b37435ce30d2731f0101"),
]

Infura_currency_lookup = CurrencyLookup.from_currency_list(currency_list)
