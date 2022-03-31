from priceLookup.yahoo_finance import YahooPriceLookup


class MNFLXPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "mNFLX"
