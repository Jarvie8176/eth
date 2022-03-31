from priceLookup.yahoo_finance import YahooPriceLookup


class YFIPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "YFI"
