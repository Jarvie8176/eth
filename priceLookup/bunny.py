from priceLookup.yahoo_finance import YahooPriceLookup


class BUNNYPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "BUNNY"
