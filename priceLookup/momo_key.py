from priceLookup.yahoo_finance import YahooPriceLookup


class MoMoKEYPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "KEY"
