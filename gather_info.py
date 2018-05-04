from urllib.request import urlopen
from bs4 import BeautifulSoup

def gatherInfoFromURL(url):
    pageRefs = []
    carInfo = {"cars": [], "year": [], "power": [], "carType": []}

    html = urlopen(url)
    html_soup = BeautifulSoup(html, "html.parser")

    pageRefs.append(url)
    for x in html_soup.find("p", class_ = "links").find_all("a"):
        if x["href"] not in pageRefs:
            pageRefs.append(x["href"])

    for page in pageRefs:

        html = urlopen(page)
        html_soup = BeautifulSoup(html, "html.parser")

        carContainers = html_soup.find("section", class_ = "models").find_all("div", class_ = "col-4")
        '''[<div class="col-4"> <a href="http://www.cars-data.com/en/ferrari-laferrari-2013/3783" title="Ferrari LaFerrari"> <img alt="Ferrari LaFerrari" src="http://www.cars-data.com/pictures/thumbs/350px/ferrari/ferrari-laferrari_3783_1.jpg" title="Ferrari LaFerrari"/> Ferrari LaFerrari</a>]
        <p>2013 - present<br/>963 HP, coupe</p>
        </div>, ...]
        '''

        carsOnPage = [x.find("a").text.strip() for x in carContainers]
        carInfo["cars"].extend(carsOnPage)
        '''
        '[Ferrari LaFerrari', 'Porsche 918 Spyder, ...]'
        '''

        carDetail = [x.find("p") for x in carContainers]
        '''
        [<p>2013 - present<br/>963 HP, coupe</p>, <p>2014 - 2016<br/>887 HP, convertible</p>, ...]
        '''

        info = []
        for detail in carDetail:
            for string in detail.strings:
                info.append(string)
        '''
        info:
        ['2013 - present', '963 HP, coupe', '2014 - 2016', '887 HP, convertible',...]
        '''

        carInfo["year"].extend(info[::2])
        carInfo["power"].extend([x.split(",")[0].strip().split()[0].strip() for x in info[1::2]])
        carInfo["carType"].extend([x.split(",")[1].strip() for x in info[1::2]])

        print(f"Found {len(carsOnPage)} cars on page : {page}")

    return carInfo
