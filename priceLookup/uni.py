from priceLookup.yahoo_finance import YahooPriceLookup


class UNIPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "UNI"
