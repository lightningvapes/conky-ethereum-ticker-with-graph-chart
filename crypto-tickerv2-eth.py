#! /usr/bin/env python

import requests, json
from os.path import expanduser

home = expanduser('~')

def parse():
    ethereum = Ethereum()    
    file_write(ethereum)

def Ethereum():
    info = []
    price_url = "https://api.coinmarketcap.com/v1/ticker/ethereum/"
    r = requests.get(price_url)
    jsn_dict = r.json()
    price = jsn_dict[0]['price_usd']
    volume_url = "https://api.coinmarketcap.com/v1/ticker/ethereum/"
    t = requests.get(volume_url)
    jsn_dict2 = t.json()
    volume = jsn_dict2[0]['24h_volume_usd']
    change_url = "https://api.coinmarketcap.com/v1/ticker/ethereum/"
    e = requests.get(change_url)
    jsn_dict3 = e.json()
    change = jsn_dict3[0]['percent_change_1h']
    info.extend((price, volume, change))
    return info

def file_write(ethereum):
    ethprice = ethereum[0]
    ethvolume = ethereum[1]
    ethchange = ethereum[2]
    file = open("%s/conky-ethereum-ticker-with-graph-chart-master/eth-price-percentage.txt" % home, 'w')
    file.write("ETH:"+"           $"+str(ethprice[:ethprice.find('.')+3])+"         "+str(ethchange)+"%"'\n')
    file.close

parse()

