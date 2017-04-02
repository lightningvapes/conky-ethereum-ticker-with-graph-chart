#!/usr/bin/env bash

USER_HOME=$(eval echo ~${SUDO_USER})

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

chmod +x ${DIR}/eth-crypto-tickerv2.py

chmod +x ${DIR}/btc-crypto-tickerv2.py

chmod +x ${DIR}/price-grabber.py

chmod +x ${DIR}/install-pip.py

chmod +x ${DIR}/cloud-prices.sh

chmod +x ${DIR}/get-balance.sh

chmod +x ${DIR}/truncate_coinbase_balance.sh

crontab -l > mycron
echo "*/2 * * * * ${DIR}/crypto-tickerv2-eth.py" >> mycron
echo "*/2 * * * * ${DIR}/crypto-tickerv2-btc.py" >> mycron
# Local grabbing of prices. Use this instead of cloud-prices.sh if your computer is always on
#echo "*/5 * * * * ${DIR}/price-grabber.py" >> mycron
echo "*/5 * * * * ${DIR}/cloud-prices.sh" >> mycron
echo "*/5 * * * * ${DIR}/get-balance.sh" >> mycron
echo "*/5 * * * * ${DIR}/truncate_coinbase_balance.sh" >> mycron
echo "*/5 * * * * /usr/bin/gnuplot ${DIR}/prices.gp > ${DIR}/download.png" >> mycron
crontab mycron
rm mycron

${DIR}/./crypto-tickerv2-eth.py

${DIR}/./crypto-tickerv2-btc.py

${DIR}/./cloud-prices.sh

${DIR}/./get-balance.sh

${DIR}/./truncate_coinbase_balance.sh

/usr/bin/gnuplot ${DIR}/prices.gp > ${DIR}/download.png

echo done
