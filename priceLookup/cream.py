from priceLookup.yahoo_finance import YahooPriceLookup


class CREAMPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "CREAM"
