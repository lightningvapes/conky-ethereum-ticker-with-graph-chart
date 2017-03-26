# conky-ethereum-ticker-with-graph-chart
Notes:
Displays cryptocurrency price, percentage change, and 12hr price graph on the desktop using conky.
Only available on Linux. Y axis far left values will change in 1$ increments as price fluctuates.


Dependencies:
python 2.7+ (Make sure you have conky downloaded and at least Python 2.7 as your default Python version.)
gnuplot
pip
requests (installed via pip)
conky


Installation:
Download the ZIP and extract to your home directory.
Give executable permissions to the install-graph-and-ticker.sh, install-pip.py, crypto-tickerv2.py and price-grabber.py scripts located within the extracted directory.

		sudo chmod +x install-graph-and-ticker.sh price-grabber.py install-pip.py crypto-tickerv2.py
		sudo ./install-pip.py
		sudo -H pip install requests
		sudo apt-get install python gnuplot conky-all
		./install-graph-and-ticker.sh

Depending on your installed version of conky, use one of the commands below to use the included .conkyrc files included. Or, simply append your current .conkyrc with the appropriate snippet.

For conky versions previous to 1.10:
		mv ~/eth-price-graph/.conkyrc-pre1.10 ~/.conky/.conkyrc

For conky 1.10 and later:
		mv ~/eth-price-graph/.conkyrc-1.10+ ~/.conky/.conkyrc


Customization:
To adjust the location, edit the alignment, gap_x, and gap_y variables within .conkyrc located within you home directory. See http://conky.sourceforge.net/variables.html for help. The prices.gb file contains the styling for the graph output png file.

Currently only supports Bitcoin and Ethereum, however it's not too hard to do a little copying, pasting, and slight modifications to show other currencies instead. Open crypto-tickerv2.py and / or price-grabber.py in a text editor and change things around to your liking.

Want a different time period other than 12 hours? Currently the price information source which the script grabs from updates about every 5 minutes or so. To achieve a 12 hour graph, "tail -n 144" is used withing the prices.gp file. What it does, is plot only the last 144 lines of prices. Why 144? Because 144 lines x 5 minutes = 720 minutes, 720 / 60 = 12 hours. Feel free to change the value to whatever number you would like, and change the "12 hrs" bottom title on the chart to whatever in the same file.

Thanks is owed to sputnik1458 for the text ticker script "crypto-tickerv2.py". His repo for the text-ticker only can be found here: https://github.com/sputnik1458/cryptocurrency-ticker
