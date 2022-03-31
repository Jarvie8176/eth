from priceLookup.yahoo_finance import YahooPriceLookup


class DAIPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "DAI"
