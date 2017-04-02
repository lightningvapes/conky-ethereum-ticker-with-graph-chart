# conky-ethereum-ticker-with-graph-chart

![alt tag](https://github.com/lightningvapes/conky-ethereum-ticker-with-graph-chart/blob/master/screenshot2.png)


Notes:
Displays cryptocurrency balance, price, percentage change, and 12hr price graph on the desktop using conky.
Only available on Linux. Y axis far left values will change in 1$ increments as price fluctuates.


Dependencies:
python 2.7+ (Make sure you have conky downloaded and at least Python 2.7 as your default Python version.)
gnuplot
pip
requests (installed via pip)
conky
ethereum / geth (use Mist or Ethereum-Wallet for easiness sake. geth used only for grabbing account balance)


Installation:
Download the ZIP and extract to your home directory.
Give executable permissions to the install-graph-and-ticker.sh, install-pip.py, crypto-tickerv2.py and price-grabber.py scripts located within the extracted directory.

		cd ~/conky-ethereum-ticker-with-graph-chart-master/
		sudo add-apt-repository -y ppa:ethereum/ethereum
		sudo apt-get update		
		sudo chmod +x install-graph-and-ticker.sh install-pip.py
		sudo ./install-pip.py
		sudo -H pip install requests
		sudo apt-get install python gnuplot conky-all curl ethereum
		./install-graph-and-ticker.sh
		
		#For conky versions previous to 1.10:
		mv ~/conky-ethereum-ticker-with-graph-chart-master/.conkyrc-pre1.10 ~/.conky/.conkyrc
		
		#For conky 1.10 and later:
		mv ~/conky-ethereum-ticker-with-graph-chart-master/.conkyrc-1.10+ ~/.conky/.conkyrc

If the cloud-prices.sh doesn't work for whatever reason (relies on a computer of mine running a separate script), then use crontab -e in terminal and point instead to price-grabber.py. This will grab the most recent data, though for historical accuracy throughout the graph it's best if the computer runs 24/7.

Depending on your installed version of conky, use one of the commands below to use the included .conkyrc files included. Or, simply append your current .conkyrc with the appropriate snippet.



Customization:
To adjust the location, edit the alignment, gap_x, and gap_y variables within .conkyrc located within you home directory. See http://conky.sourceforge.net/variables.html for help. The prices.gb file contains the styling for the graph output png file.

Currently only supports Bitcoin and Ethereum, however it's not too hard to do a little copying, pasting, and slight modifications to show other currencies instead. Open crypto-tickerv2.py and / or price-grabber.py in a text editor and change things around to your liking.

Want a different time period other than 12 hours? Currently the price information source which the script grabs from updates about every 5 minutes or so. To achieve a 12 hour graph, "tail -n 144" is used withing the prices.gp file. What it does, is plot only the last 144 lines of prices. Why 144? Because 144 lines x 5 minutes = 720 minutes, 720 / 60 = 12 hours. Feel free to change the value to whatever number you would like, and change the "12 hrs" bottom title on the chart to whatever in the same file.

Thanks is owed to sputnik1458 for the text ticker script "crypto-tickerv2.py". His repo for the text-ticker only can be found here: https://github.com/sputnik1458/cryptocurrency-ticker
