#! /usr/bin/env python

import requests, json
from os.path import expanduser

from coinbase.wallet.client import Client
home = expanduser('~')
client = Client('YOUR_API_KEY', 'YOUR_API_SECRET')
accounts = client.get_accounts()

print accounts ['data'][0]['balance']

