import pandas as pd

from gather_info import gatherInfoFromURL

def scraper():
    carinfo = gatherInfoFromURL(url="http://www.cars-data.com/en/sport-cars.html")
    #carInfo = {"cars": [], "year": [], "power": [], "carType": []}

    print(len(carinfo["cars"]))

    carDataFrame = pd.DataFrame({"Cars": carinfo.get("cars")})
    print(carDataFrame.info())

if __name__ == '__main__':
    scraper()
