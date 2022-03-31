from priceLookup.yahoo_finance import YahooPriceLookup


class YFIEPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "YFIE"
