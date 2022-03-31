from priceLookup.yahoo_finance import YahooPriceLookup


class CRVPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "CRV"
