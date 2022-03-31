from priceLookup.yahoo_finance import YahooPriceLookup


class SUSHIPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "SUSHI"
