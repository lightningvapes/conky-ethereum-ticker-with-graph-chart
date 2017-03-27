#!/usr/bin/env bash

content=$(curl -L https://www.dropbox.com/s/2ko8o6q0ovajry3/prices.txt?dl=1)
echo $content | tr " " "\n" > ~/conky-ethereum-ticker-with-graph-chart-master/prices.txt

