from priceLookup.yahoo_finance import YahooPriceLookup


class YFIIPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "YFII"
