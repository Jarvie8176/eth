#!/usr/bin/env bash

mkdir -p resources/historicalPrice/
wget -O resources/historicalPrice/Bitfinex_TRXUSD_1h.csv \
  https://gist.githubusercontent.com/Jarvie8176/ce7ce8ecf84f158cde949f6509af7e40/raw/c7eecccd2e7c351f8f020d9c284a4684091ff876/Bitfinex_TRXUSD_1h.csv
wget -O resources/historicalPrice/Bitfinex_ETHUSD_1h.csv \
  https://gist.githubusercontent.com/Jarvie8176/0c72c7e1e2acd0abcbfc993015b97764/raw/5b38ec903dc0d3a4f30bd5705d2e9821408fc05c/Bitfinex_ETHUSD_1h.csv
