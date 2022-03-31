from priceLookup.yahoo_finance import YahooPriceLookup


class LOWBPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "lowb"
