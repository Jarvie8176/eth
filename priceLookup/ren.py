from priceLookup.yahoo_finance import YahooPriceLookup


class RENPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "REN"
