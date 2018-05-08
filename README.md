A fun web scraper written in python to scrap car information from this URL:

http://www.cars-data.com/en/sport-cars.html

# Main screen

## This is how the main screen looks like:

![](https://github.com/prashantgupta24/python-web-scraper/blob/master/images/main_screen.jpg)

## I scrape all the other links from that page

![](https://github.com/prashantgupta24/python-web-scraper/blob/master/images/links.jpg)

## And from each page, I scrape all car names and information.

### Voila!

![](https://github.com/prashantgupta24/python-web-scraper/blob/master/images/csv.jpg)

### Then I make some cool graphs:

![](https://github.com/prashantgupta24/python-web-scraper/blob/master/images/car%20pie%20chart.jpg)

# Code

## Raw data
The scraped data is present in [carInfo.csv](https://github.com/prashantgupta24/python-web-scraper/blob/dev/src/carInfo.csv)

## Scraping files

- The scraping and generating the csv is done through [carinfo_scraper.ipynb](https://github.com/prashantgupta24/python-web-scraper/blob/master/src/carinfo_scraper.ipynb) script, which I have presented in the form of a `Jupyter` notebook. 

- The main function `gatherInfoFromURL` is present in the [gather_info.py](https://github.com/prashantgupta24/python-web-scraper/blob/master/src/gather_info.py) file, which scraps the data off the web pages.

## Plotting
- The plotting of various graphs is done on [carinfo_plots.ipynb](https://github.com/prashantgupta24/python-web-scraper/blob/master/src/carinfo_plots.ipynb) Jupyter notebook.
