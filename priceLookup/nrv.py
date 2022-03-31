from priceLookup.yahoo_finance import YahooPriceLookup


class NRVPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "NRV"
