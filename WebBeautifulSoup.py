
#url = "https://www.betriheim.fo/"
#results = requests.get(url)
#doc = BeautifulSoup(results.text, "html.parser")

#priceClass = doc.find_all(class_="info")

#prices = doc.find_all(text=re.compile("Kr.*"))
#for prices in prices:
    #print(prices.strip("Kr.*"))
    #print(prices.strip("Seinasta bo�: Kr.*"))
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import re

class FaroesProperties:
    # addresses
    # prices
    # LatestPrices
    # validDates
    # dates
    # buildingSizes
    # landSizes
    # rooms 
    # floors
    def __init__(self, address=None, price=None, LatesPrice=None, validDate=None, date=None, buildingSize=None, landSize=None, room=None, floor=None):
        if address is None:
            self.addresses = "None"
        self.addresses = address
        self.prices = price
        self.LatestPrices = LatesPrice
        self.validDates = validDate
        self.dates = date
        self.buildingSizes = buildingSize
        if landSize is None:
            self.landSizes = "None"
        self.landSizes = landSize
        if rooms is None:
            self.rooms = "None"
        self.rooms = room
        if floors is None:
            self.floors = "None"
        self.floors = floor
    def display(self):
        print(self.addresses)
        print(self.prices)
        print(self.LatestPrices)
        print(self.validDates)
        print(self.dates)
        print(self.buildingSizes)
        print(self.landSizes)
        print(self.rooms)
        print(self.floors)


url = 'https://www.betriheim.fo/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# sections = soup.find_all('section', class_='properties')
# properties = soup.find_all('div', class_="price")
# for property in properties:
#     price = property.text
#     print(price.strip('Kr. '))
# print(type(price))

# addressesUnfiltered = soup.find_all('address', class_="medium")
# pricesUnfiltered = soup.find_all('div', class_="price")
# LatestPricesUnfiltered = soup.find_all('div', class_="latest-offer")
# validDatesUnfiltered = soup.find_all('div', class_="valid")
# datesUnfiltered = soup.find_all('span', class_="c-icon construction-date")
# buildingSizesUnfiltered = soup.find_all('span', class_="c-icon building-size")
# landSizesUnfiltered = soup.find_all('div', class_="c-icon land-size")
# roomsUnfiltered = soup.find_all('div', class_="c-icon rooms")
# floorsUnfiltered = soup.find_all('div', class_="c-icon floors")
AllPropertyWrappers = soup.find_all('div', class_="properties-wrapper")
properties = []

for property in AllPropertyWrappers:
    addresses = property.find('address', class_="medium").text
    prices = property.find('div', class_="price").text
    LatestPrices = property.find('div', class_="latest-offer").text
    validDates = property.find('div', class_="valid")
    dates = property.find('span', class_="c-icon construction-date").text
    buildingSizes = property.find('span', class_="c-icon building-size")
    landSizes = property.find('div', class_="c-icon land-size")
    rooms = property.find('div', class_="c-icon rooms")
    floors = property.find('div', class_="c-icon floors")
    prop = FaroesProperties(addresses,prices,LatestPrices,validDates,dates,buildingSizes,landSizes,rooms,floors)
    properties.append(prop)

for prop in properties:
    print(prop.validDates, prop.addresses)

print(type(properties))

for prop in properties:
    print(prop)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


# stringval = soup.get_text(str(addressClass), strip=True)

#facts =[addressClass,priceClass,dateClass,buildingSizeClass,landSizeClass,roomsClass,floorsClass]
#print(stringval)

