from typing import List

from parser.currency import Currency
from parser.currencyLookup import CurrencyLookup

currency_list: List[Currency] = [
    # ETH network
    Currency(name="Ether", unit="ETH", decimal_places=18,
             contract_address="0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"),
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
    Currency(name="Republic", unit="REN", decimal_places=18,
             contract_address="0x408e41876cccdc0f92210600ef50372656052a38"),
    Currency(name="YFValue", unit="YFV", decimal_places=18,
             contract_address="0x45f24baeef268bb6d63aee5129015d69702bcdfa"),
    Currency(name="Aave Interest bearing YFI", unit="aYFI", decimal_places=18,
             contract_address="0x12e51e77daaa58aa0e9247db7510ea4b46f9bead"),


    # BSC network
    Currency(name="BNB", unit="BNB", decimal_places=18,
             contract_address="0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c"),
    Currency(name="Wrapped BNB", unit="BNB", decimal_places=18,
             contract_address="0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c"),
    Currency(name="Binance-Peg USD Coin", unit="USDC", decimal_places=18,
             contract_address="0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d"),
    Currency(name="PancakeSwap Token", unit="Cake", decimal_places=18,
             contract_address="0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82"),
    Currency(name="AUTOv2", unit="AUTO", decimal_places=18,
             contract_address="0xa184088a740c695e156f91f5cc086a06bb78b827"),
    Currency(name="Pancake LPs", unit="Cake-LP", decimal_places=18,
             contract_address="0xd5664d2d15cdffd597515f1c0d945c6c1d3bf85b"),
    Currency(name="Ellipsis.finance BUSD/USDC/USDT", unit="3EPS", decimal_places=18,
             contract_address="0xaf4de8e872131ae328ce21d909c74705d3aaf452"),
    Currency(name="Binance-Peg BUSD Token", unit="BUSD", decimal_places=18,
             contract_address="0xe9e7cea3dedca5984780bafc599bd69add087d56"),
    Currency(name="MDX Token", unit="MDX", decimal_places=18,
             contract_address="0x9c65ab58d8d978db963e63f2bfb7121627e3a739"),
    Currency(name="Pancake LPs", unit="Cake-LP", decimal_places=18,
             contract_address="0x680dd100e4b394bda26a59dd5c119a391e747d18"),
    Currency(name="Nerve", unit="NRV", decimal_places=18,
             contract_address="0x42f6f551ae042cbe50c739158b4f0cac0edb9096"),
    Currency(name="Wrapped UST Token ", unit="UST", decimal_places=18,
             contract_address="0x23396cf899ca06c4472205fc903bdb4de249d6fc"),
    Currency(name="Wrapped Mirror GOOGL Token", unit="mGOOGL", decimal_places=18,
             contract_address="0x62d71b23bf15218c7d2d7e48dbbd9e9c650b173f"),
    Currency(name="Wrapped UST Token ", unit="UST", decimal_places=18,
             contract_address="0x23396cf899ca06c4472205fc903bdb4de249d6fc"),
    Currency(name="Binance-Peg BSC-USD", unit="BSC-USD", decimal_places=18,
             contract_address="0x55d398326f99059ff775485246999027b3197955"),
    Currency(name="Wrapped Mirror NFLX Token", unit="mNFLX", decimal_places=18,
             contract_address="0xa04f060077d90fe2647b61e4da4ad1f97d6649dc"),
    Currency(name="Ellipsis", unit="EPS", decimal_places=18,
             contract_address="0xa7f552078dcc247c2684336020c03648500c6d9f"),
    Currency(name="FinNexus", unit="FNX", decimal_places=18,
             contract_address="0xdfd9e2a17596cad6295ecffda42d9b6f63f7b5d5"),
    Currency(name="MoMo KEY", unit="KEY", decimal_places=18,
             contract_address="0x85c128ee1feeb39a59490c720a9c563554b51d33"),
    Currency(name="ShardingDAO", unit="SHD", decimal_places=18,
             contract_address="0x5845cd0205b5d43af695412a79cf7c1aeddb060f"),
    Currency(name="Mist", unit="MIST", decimal_places=18,
             contract_address="0x68e374f856bf25468d365e539b700b648bf94b67"),
    Currency(name="Cyclone Protocol", unit="CYC", decimal_places=18,
             contract_address="0x810ee35443639348adbbc467b33310d2ab43c168"),
    Currency(name="Bunny Token", unit="BUNNY", decimal_places=18,
             contract_address="0xc9849e6fdb743d08faee3e34dd2d1bc69ea11a51"),
    Currency(name="loser coin", unit="lowb", decimal_places=18,
             contract_address="0x843d4a358471547f51534e3e51fae91cb4dc3f28"),
    Currency(name="Wrapped Mirror TSLA Token", unit="mTSLA", decimal_places=18,
             contract_address="0xf215a127a196e3988c09d052e16bcfd365cd7aa3"),
    Currency(name="Wrapped UST Token", unit="UST", decimal_places=18,
             contract_address="0x23396cf899ca06c4472205fc903bdb4de249d6fc"),
    Currency(name="Pancake LPs", unit="Cake-LP", decimal_places=18,
             contract_address="0x852a68181f789ae6d1da3df101740a59a071004f"),
    Currency(name="Nerve 3pool LP", unit="3NRV-LP", decimal_places=18,
             contract_address="0xf2511b5e4fb0e5e2d123004b672ba14850478c14"),
    Currency(name="Pancake LPs", unit="Cake-LP", decimal_places=18,
             contract_address="0xf609ade3846981825776068a8ed7746470029d1f"),
    Currency(name="Binance-Peg Ethereum Token", unit="ETH", decimal_places=18,
             contract_address="0x2170ed0880ac9a755fd29b2688956bd959f933f8"),
    Currency(name="Nerve anyETH/ETH LP", unit="nrvETH", decimal_places=18,
             contract_address="0x0d283bf16a9bde49cfc48d8dc050af28b71bdd90"),
    Currency(name="ACryptoS PancakeSwap Token", unit="acsCake", decimal_places=18,
             contract_address="0xb6eb654fbdc697edd73174a19b074bc67c00a0c0"),
]

Infura_currency_lookup = CurrencyLookup.from_currency_list(currency_list)
