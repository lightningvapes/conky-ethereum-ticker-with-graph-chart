#!/usr/bin/env bash

content=$(curl -L https://www.dropbox.com/s/ydowv9fzywtyt7z/prices.txt?dl=1)
echo $content | tr " " "\n" > ~/conky-ethereum-ticker-with-graph-chart-master/prices.txt

