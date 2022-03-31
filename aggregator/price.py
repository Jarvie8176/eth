from __future__ import annotations
from typing import List, Optional

from loguru import logger
from pydantic.main import BaseModel

from dto.parsedTrx import ParsedTrx
from priceLookup.auto import AUTOPriceLookup
from priceLookup.band import BANDPriceLookup
from priceLookup.base import BasePriceLookup
from priceLookup.bnb import BNBPriceLookup
from priceLookup.bunny import BUNNYPriceLookup
from priceLookup.cake import CAKEPriceLookup
from priceLookup.cream import CREAMPriceLookup
from priceLookup.crv import CRVPriceLookup
from priceLookup.cyc import CYCPriceLookup
from priceLookup.dai import DAIPriceLookup
from priceLookup.eps import EPSPriceLookup
from priceLookup.eth import ETHPriceLookup
from priceLookup.fnx import FNXPriceLookup
from priceLookup.lowb import LOWBPriceLookup
from priceLookup.mGOOGL import MGOOGLPriceLookup
from priceLookup.mNFLX import MNFLXPriceLookup
from priceLookup.mTSLA import MTSLAPriceLookup
from priceLookup.mdx import MDXPriceLookup
from priceLookup.mist import MISTPriceLookup
from priceLookup.momo_key import MoMoKEYPriceLookup
from priceLookup.nrv import NRVPriceLookup
from priceLookup.ren import RENPriceLookup
from priceLookup.srm import SRMPriceLookup
from priceLookup.sushi import SUSHIPriceLookup
from priceLookup.trx import TRXPriceLookup
from priceLookup.uni import UNIPriceLookup
from priceLookup.unifi import UNIFIPriceLookup
from priceLookup.ust import USTPriceLookup
from priceLookup.yfi import YFIPriceLookup
from priceLookup.yfie import YFIEPriceLookup
from priceLookup.yfii import YFIIPriceLookup


class PriceAggregatorCreateOptions(BaseModel):
    trx_price_data_file_path: Optional[str]
    eth_price_data_file_path: Optional[str]
    bnb_price_data_file_path: Optional[str]
    auto_price_data_file_path: Optional[str]
    cake_price_data_file_path: Optional[str]
    eps_price_data_file_path: Optional[str]
    key_price_data_file_path: Optional[str]
    nrv_price_data_file_path: Optional[str]
    mist_price_data_file_path: Optional[str]
    lowb_price_data_file_path: Optional[str]
    fnx_price_data_file_path: Optional[str]
    cyc_price_data_file_path: Optional[str]
    bunny_price_data_file_path: Optional[str]
    mdx_price_data_file_path: Optional[str]
    mGOOGL_price_data_file_path: Optional[str]
    mTSLA_price_data_file_path: Optional[str]
    mNFLX_price_data_file_path: Optional[str]
    ust_price_data_file_path: Optional[str]
    yfie_price_data_file_path: Optional[str]
    yfi_price_data_file_path: Optional[str]
    yfii_price_data_file_path: Optional[str]
    srm_price_data_file_path: Optional[str]
    sushi_price_data_file_path: Optional[str]
    unifi_price_data_file_path: Optional[str]
    ren_price_data_file_path: Optional[str]
    dai_price_data_file_path: Optional[str]
    crv_price_data_file_path: Optional[str]
    cream_price_data_file_path: Optional[str]
    band_price_data_file_path: Optional[str]
    uni_price_data_file_path: Optional[str]


class PriceAggregator:
    def __init__(self) -> None:
        self.price_lookups: List[BasePriceLookup] = []

    def add_price_lookup(self, price_lookup: BasePriceLookup) -> PriceAggregator:
        logger.debug(f"adding price lookup for {price_lookup.unit}")
        self.price_lookups.append(price_lookup)
        return self

    def update_price(self, parsed_trx: ParsedTrx) -> ParsedTrx:
        timestamp = parsed_trx.timestamp

        if parsed_trx.in_payload:
            in_price_lookup = self._find_price_lookup_by_unit(
                parsed_trx.in_payload.unit)
            if in_price_lookup:
                parsed_trx.in_payload.price = in_price_lookup.time_to_price(timestamp)

        if parsed_trx.out_payload:
            out_price_lookup = self._find_price_lookup_by_unit(
                parsed_trx.out_payload.unit)
            if out_price_lookup:
                parsed_trx.out_payload.price = out_price_lookup.time_to_price(timestamp)

        if parsed_trx.fee_payload:
            fee_price_lookup = self._find_price_lookup_by_unit(
                parsed_trx.fee_payload.unit)
            if fee_price_lookup:
                parsed_trx.fee_payload.price = fee_price_lookup.time_to_price(timestamp)

        return parsed_trx

    def _find_price_lookup_by_unit(self, unit: str) -> Optional[BasePriceLookup]:
        try:
            return next(i for i in self.price_lookups if i.unit == unit)
        except StopIteration:
            return None

    @staticmethod
    def create(options: PriceAggregatorCreateOptions) -> PriceAggregator:
        price_aggregator = PriceAggregator()

        if options.trx_price_data_file_path:
            price_aggregator.add_price_lookup(TRXPriceLookup(options.trx_price_data_file_path))

        if options.eth_price_data_file_path:
            price_aggregator.add_price_lookup(ETHPriceLookup(options.eth_price_data_file_path))

        if options.bnb_price_data_file_path:
            price_aggregator.add_price_lookup(BNBPriceLookup(options.bnb_price_data_file_path))

        if options.auto_price_data_file_path:
            price_aggregator.add_price_lookup(AUTOPriceLookup(options.auto_price_data_file_path))

        if options.cake_price_data_file_path:
            price_aggregator.add_price_lookup(CAKEPriceLookup(options.cake_price_data_file_path))

        if options.eps_price_data_file_path:
            price_aggregator.add_price_lookup(EPSPriceLookup(options.eps_price_data_file_path))

        if options.key_price_data_file_path:
            price_aggregator.add_price_lookup(MoMoKEYPriceLookup(options.key_price_data_file_path))

        if options.nrv_price_data_file_path:
            price_aggregator.add_price_lookup(NRVPriceLookup(options.nrv_price_data_file_path))

        if options.mist_price_data_file_path:
            price_aggregator.add_price_lookup(MISTPriceLookup(options.mist_price_data_file_path))

        if options.lowb_price_data_file_path:
            price_aggregator.add_price_lookup(LOWBPriceLookup(options.lowb_price_data_file_path))

        if options.fnx_price_data_file_path:
            price_aggregator.add_price_lookup(FNXPriceLookup(options.fnx_price_data_file_path))

        if options.cyc_price_data_file_path:
            price_aggregator.add_price_lookup(CYCPriceLookup(options.cyc_price_data_file_path))

        if options.bunny_price_data_file_path:
            price_aggregator.add_price_lookup(BUNNYPriceLookup(options.bunny_price_data_file_path))

        if options.mdx_price_data_file_path:
            price_aggregator.add_price_lookup(MDXPriceLookup(options.mdx_price_data_file_path))

        if options.mGOOGL_price_data_file_path:
            price_aggregator.add_price_lookup(MGOOGLPriceLookup(options.mGOOGL_price_data_file_path))

        if options.mTSLA_price_data_file_path:
            price_aggregator.add_price_lookup(MTSLAPriceLookup(options.mTSLA_price_data_file_path))

        if options.mNFLX_price_data_file_path:
            price_aggregator.add_price_lookup(MNFLXPriceLookup(options.mNFLX_price_data_file_path))

        if options.ust_price_data_file_path:
            price_aggregator.add_price_lookup(USTPriceLookup(options.ust_price_data_file_path))

        if options.yfie_price_data_file_path:
            price_aggregator.add_price_lookup(YFIEPriceLookup(options.yfie_price_data_file_path))

        if options.yfi_price_data_file_path:
            price_aggregator.add_price_lookup(YFIPriceLookup(options.yfi_price_data_file_path))

        if options.yfii_price_data_file_path:
            price_aggregator.add_price_lookup(YFIIPriceLookup(options.yfii_price_data_file_path))

        if options.srm_price_data_file_path:
            price_aggregator.add_price_lookup(SRMPriceLookup(options.srm_price_data_file_path))

        if options.sushi_price_data_file_path:
            price_aggregator.add_price_lookup(SUSHIPriceLookup(options.sushi_price_data_file_path))

        if options.unifi_price_data_file_path:
            price_aggregator.add_price_lookup(UNIFIPriceLookup(options.unifi_price_data_file_path))

        if options.ren_price_data_file_path:
            price_aggregator.add_price_lookup(RENPriceLookup(options.ren_price_data_file_path))

        if options.dai_price_data_file_path:
            price_aggregator.add_price_lookup(DAIPriceLookup(options.dai_price_data_file_path))

        if options.crv_price_data_file_path:
            price_aggregator.add_price_lookup(CRVPriceLookup(options.crv_price_data_file_path))

        if options.cream_price_data_file_path:
            price_aggregator.add_price_lookup(CREAMPriceLookup(options.cream_price_data_file_path))

        if options.band_price_data_file_path:
            price_aggregator.add_price_lookup(BANDPriceLookup(options.band_price_data_file_path))

        if options.uni_price_data_file_path:
            price_aggregator.add_price_lookup(UNIPriceLookup(options.uni_price_data_file_path))

        return price_aggregator
