import pathlib
from os import path

from aggregator.price import PriceAggregator, PriceAggregatorCreateOptions


def create_price_aggregator() -> PriceAggregator:
    cwd = pathlib.Path(__file__).parent.resolve()

    return PriceAggregator.create(
        options=PriceAggregatorCreateOptions(
            eth_price_data_file_path=path.join(cwd, "../resources/historicalPrice/Bitfinex_ETHUSD_1h.csv"),
            bnb_price_data_file_path=path.join(cwd, "../resources/historicalPrice/BNB-USD.csv"),
            auto_price_data_file_path=path.join(cwd, "../resources/historicalPrice/AUTO-USD.csv"),
            cake_price_data_file_path=path.join(cwd, "../resources/historicalPrice/CAKE-USD.csv"),
            eps_price_data_file_path=path.join(cwd, "../resources/historicalPrice/EPS1-USD.csv"),
            key_price_data_file_path=path.join(cwd, "../resources/historicalPrice/KEY2-USD.csv"),
            nrv_price_data_file_path=path.join(cwd, "../resources/historicalPrice/NRV-USD.csv"),

            mist_price_data_file_path=path.join(cwd, "../resources/historicalPrice/MIST1-USD.csv"),
            lowb_price_data_file_path=path.join(cwd, "../resources/historicalPrice/LOWB-USD.csv"),
            fnx_price_data_file_path=path.join(cwd, "../resources/historicalPrice/FNX-USD.csv"),
            cyc_price_data_file_path=path.join(cwd, "../resources/historicalPrice/CYC-USD.csv"),
            bunny_price_data_file_path=path.join(cwd, "../resources/historicalPrice/BUNNY-USD.csv"),
            mdx_price_data_file_path=path.join(cwd, "../resources/historicalPrice/MDX1-USD.csv"),
            mGOOGL_price_data_file_path=path.join(cwd, "../resources/historicalPrice/GOOGL.csv"),
            mTSLA_price_data_file_path=path.join(cwd, "../resources/historicalPrice/TSLA.csv"),
            mNFLX_price_data_file_path=path.join(cwd, "../resources/historicalPrice/NFLX.csv"),
            ust_price_data_file_path=path.join(cwd, "../resources/historicalPrice/UST-USD.csv"),

            yfie_price_data_file_path=path.join(cwd, "../resources/historicalPrice/YFIE-USD.csv"),
            yfi_price_data_file_path=path.join(cwd, "../resources/historicalPrice/YFI-USD.csv"),
            yfii_price_data_file_path=path.join(cwd, "../resources/historicalPrice/YFII-USD.csv"),
            srm_price_data_file_path=path.join(cwd, "../resources/historicalPrice/SRM-USD.csv"),
            sushi_price_data_file_path=path.join(cwd, "../resources/historicalPrice/SUSHI-USD.csv"),
            unifi_price_data_file_path=path.join(cwd, "../resources/historicalPrice/UNIFI-USD.csv"),
            ren_price_data_file_path=path.join(cwd, "../resources/historicalPrice/REN-USD.csv"),
            dai_price_data_file_path=path.join(cwd, "../resources/historicalPrice/DAI-USD.csv"),
            crv_price_data_file_path=path.join(cwd, "../resources/historicalPrice/CRV-USD.csv"),
            cream_price_data_file_path=path.join(cwd, "../resources/historicalPrice/CREAM-USD.csv"),
            band_price_data_file_path=path.join(cwd, "../resources/historicalPrice/BAND-USD.csv"),
            uni_price_data_file_path=path.join(cwd, "../resources/historicalPrice/UNI1-USD.csv"),

            trx_price_data_file_path=path.join(cwd, "../resources/historicalPrice/Bitfinex_TRXUSD_1h.csv"),
        ))
