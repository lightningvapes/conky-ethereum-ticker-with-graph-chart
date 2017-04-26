#! /usr/bin/env python

import requests, json
from os.path import expanduser

home = expanduser('~')

def parse():
    bitcoin = Bitcoin()
    file_write(bitcoin)

def Bitcoin():
    info = []
    price_url = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"
    r = requests.get(price_url)
    jsn_dict = r.json()
    price = jsn_dict[0]['price_usd']
    volume_url = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"
    t = requests.get(volume_url)
    jsn_dict2 = t.json()
    volume = jsn_dict2[0]['24h_volume_usd']
    change_url = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"
    e = requests.get(change_url)
    jsn_dict3 = e.json()
    change = jsn_dict3[0]['percent_change_1h']
    info.extend((price, volume, change))
    return info

def file_write(bitcoin):
    bitprice = bitcoin[0]
    bitvolume = bitcoin[1]
    bitchange = bitcoin[2]
    file = open("%s/conky-ethereum-ticker-with-graph-chart-master/btc-price-percentage.txt" % home, 'w')
    file.write("BTC:"+"           $"+str(bitprice[:bitprice.find('.')+3])+"     "+str(bitchange)+"%"'\n')
    file.close

parse()
