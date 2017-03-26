#! /usr/bin/env python

import requests, json
from os.path import expanduser

home = expanduser('~')

def parse():
    bitcoin = Bitcoin()
    ethereum = Ethereum()
    monero = Monero()
    file_write(bitcoin, ethereum, monero)

def Bitcoin():
    info = []
    price_url = "http://coinmarketcap-nexuist.rhcloud.com/api/btc/price"
    r = requests.get(price_url)
    jsn_dict = r.json()
    price = jsn_dict['usd']
    volume_url = "http://coinmarketcap-nexuist.rhcloud.com/api/btc/volume"
    t = requests.get(volume_url)
    jsn_dict2 = t.json()
    volume = jsn_dict2['usd']
    change_url = "http://coinmarketcap-nexuist.rhcloud.com/api/btc/change"
    e = requests.get(change_url)
    change = e.json()
    info.extend((price, volume, change))
    return info

def Ethereum():
    info = []
    price_url = "http://coinmarketcap-nexuist.rhcloud.com/api/eth/price"
    r = requests.get(price_url)
    jsn_dict = r.json()
    price = jsn_dict['usd']
    volume_url = "http://coinmarketcap-nexuist.rhcloud.com/api/eth/volume"
    t = requests.get(volume_url)
    jsn_dict2 = t.json()
    volume = jsn_dict2['usd']
    change_url = "http://coinmarketcap-nexuist.rhcloud.com/api/eth/change"
    e = requests.get(change_url)
    change = e.json()
    info.extend((price, volume, change))
    return info

def Monero():
    info = []
    price_url = "http://coinmarketcap-nexuist.rhcloud.com/api/xmr/price"
    r = requests.get(price_url)
    jsn_dict = r.json()
    price = jsn_dict['usd']
    volume_url = "http://coinmarketcap-nexuist.rhcloud.com/api/xmr/volume"
    t = requests.get(volume_url)
    jsn_dict2 = t.json()
    volume = jsn_dict2['usd']
    change_url = "http://coinmarketcap-nexuist.rhcloud.com/api/xmr/change"
    e = requests.get(change_url)
    change = e.json()
    info.extend((price, volume, change))
    return info

def file_write(bitcoin, ethereum, monero):
    bitprice = bitcoin[0]
    bitvolume = bitcoin[1]
    bitchange = bitcoin[2]
    ethprice = ethereum[0]
    ethvolume = ethereum[1]
    ethchange = ethereum[2]
    xmrprice = monero[0]
    xmrvolume = monero[1]
    xmrchange = monero[2]
    file = open("%s/eth-price-graph/price-percentage.txt" % home, 'w')
    file.write("BTC:           $%.2f      %s%% \n" % (bitprice, bitchange))
    file.write("ETH:           $%.2f         %s%% \n" % (ethprice, ethchange))
    file.close

parse()
