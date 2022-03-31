from priceLookup.yahoo_finance import YahooPriceLookup


class MTSLAPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "mTSLA"
