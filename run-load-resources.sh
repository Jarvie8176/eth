#!/usr/bin/env bash

mkdir -p resources/historicalPrice/
wget -O resources/historicalPrice/Bitfinex_TRXUSD_1h.csv \
  https://gist.githubusercontent.com/Jarvie8176/ce7ce8ecf84f158cde949f6509af7e40/raw/c7eecccd2e7c351f8f020d9c284a4684091ff876/Bitfinex_TRXUSD_1h.csv
