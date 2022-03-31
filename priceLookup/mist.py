from priceLookup.yahoo_finance import YahooPriceLookup


class MISTPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "MIST"
