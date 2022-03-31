from priceLookup.yahoo_finance import YahooPriceLookup


class USTPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "UST"
