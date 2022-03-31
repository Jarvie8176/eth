from priceLookup.yahoo_finance import YahooPriceLookup


class EPSPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "EPS"
