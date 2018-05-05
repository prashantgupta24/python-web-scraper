A fun web scraper written in python to scrap car information from this URL:

http://www.cars-data.com/en/sport-cars.html

# Main screen

## This is how the main screen looks like:

![](https://github.com/prashantgupta24/python-web-scraper/blob/master/images/main_screen.jpg)

## I scrape all the links from that page

![](https://github.com/prashantgupta24/python-web-scraper/blob/master/images/links.jpg)

## And for each page, I scrape all car names and information.

Voila!

![](https://github.com/prashantgupta24/python-web-scraper/blob/master/images/csv.jpg)

# Code

The scraping and generating the csv is done through [this](https://github.com/prashantgupta24/python-web-scraper/blob/master/src/carinfo_scraper.ipynb) python script, which I have presented in the form of a `Jupyter` notebook. 

The main function `gatherInfoFromURL` is present in [this](https://github.com/prashantgupta24/python-web-scraper/blob/master/src/gather_info.py) file, which scraps the data off the web pages.

The plotting of various graphs is done on [this](https://github.com/prashantgupta24/python-web-scraper/blob/master/src/carinfo_plots.ipynb) Jupyter notebook.
