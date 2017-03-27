#!/usr/bin/env bash

USER_HOME=$(eval echo ~${SUDO_USER})

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

chmod +x ${DIR}/crypto-tickerv2.py

chmod +x ${DIR}/price-grabber.py

chmod +x ${DIR}/install-pip.py

chmod +x ${DIR}/cloud-prices.sh

crontab -l > mycron
echo "*/1 * * * * ${DIR}/crypto-tickerv2.py" >> mycron
# Local grabbing of prices. Use this instead of cloud-prices.sh if your computer is always on
#echo "*/5 * * * * ${DIR}/price-grabber.py" >> mycron
echo "*/5 * * * * ${DIR}/cloud-prices.sh" >> mycron
echo "*/5 * * * * /usr/bin/gnuplot ${DIR}/prices.gp > ${DIR}/download.png" >> mycron
crontab mycron
rm mycron

echo done
