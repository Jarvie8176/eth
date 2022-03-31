from priceLookup.yahoo_finance import YahooPriceLookup


class UNIFIPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "UNIFI"
