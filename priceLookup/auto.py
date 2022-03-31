from priceLookup.yahoo_finance import YahooPriceLookup


class AUTOPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "AUTO"
