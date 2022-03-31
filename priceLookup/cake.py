from priceLookup.yahoo_finance import YahooPriceLookup


class CAKEPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "Cake"
