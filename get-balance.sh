#!/bin/bash

PROCESS="geth"

    RESULT=`pgrep ${PROCESS}`

    if [ "${RESULT:-null}" = null ]; then
            echo "${PROCESS} not running. Open Mist or Ethereum Wallet"            
    else
            cat <<EOF | geth attach | sed -n -r  's/^([0-9\.]+)$/\1/p' | cut -c1-5 > ~/conky-ethereum-ticker-with-graph-chart-master/miner_balance.txt
web3.fromWei(eth.getBalance(eth.coinbase), "ether")
exit
EOF
    fi    

exit   
