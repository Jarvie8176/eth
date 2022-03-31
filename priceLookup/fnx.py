from priceLookup.yahoo_finance import YahooPriceLookup


class FNXPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "FNX"
