from bs4 import BeautifulSoup
import requests
from bs4 import UnicodeDammit
import re

url = "https://www.betriheim.fo/"
results = requests.get(url)
new_doc = BeautifulSoup(results.text, "html.parser")
doc = UnicodeDammit.detwingle(new_doc)

#priceClass = doc.find_all(class_="info")

addressClass = doc.find_all(class_="medium")
stringval = doc.get_text(str(addressClass), strip=True)
priceClass = doc.find_all(class_="price")
dateClass = doc.find_all(class_="c-icon construction-date")
buildingSizeClass = doc.find_all(class_="c-icon building-size")
landSizeClass = doc.find_all(class_="c-icon land-size")
roomsClass = doc.find_all(class_="c-icon rooms")
floorsClass = doc.find_all(class_="c-icon floors")

facts =[addressClass,priceClass,dateClass,buildingSizeClass,landSizeClass,roomsClass,floorsClass]
print(stringval)

#prices = doc.find_all(text=re.compile("Kr.*"))
#for prices in prices:
    #print(prices.strip("Kr.*"))
    #print(prices.strip("Seinasta bo�: Kr.*"))