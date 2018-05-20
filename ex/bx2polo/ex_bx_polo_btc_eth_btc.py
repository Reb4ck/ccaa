#!/usr/bin/env python3
# -*- encoding : utf-8 -*-

# buy bx -> sell polo
# buy eth, send eth, sell eth

from init import *

def run():
    invest = 1
    withdrawal_fee = 0.0005

    exchange1 = 'btc_eth'
    exchange2 = 'btc_eth'

    print("invest = {} btc".format(invest))
    buy_volume = BX().get_asks_rate(exchange1, invest)
    print("{} btc = {} eth".format(invest, buy_volume))
    total_currency = format_float(Decimal(buy_volume) - Decimal(withdrawal_fee))
    print("total = withdrawal fee (volume - {}) = {} eth".format(withdrawal_fee, total_currency))

    #-------------
    print()
    #-------------

    sell_volume = POLO().get_bids_rate(exchange2, total_currency)
    print("sell {} eth = {} btc".format(buy_volume, sell_volume))

if __name__ == '__main__':
    try:
        run()

    except KeyboardInterrupt:
        pass