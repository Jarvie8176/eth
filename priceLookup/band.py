from priceLookup.yahoo_finance import YahooPriceLookup


class BANDPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "BAND"
