
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
import csv

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
    def __init__(self, website=None, address=None, price=None,
                 LatesPrice=None, validDate=None,
                 date=None, buildingSize=None,
                 landSize=None, room=None,
                 floor=None):
        if website is None:
            self.websites = "None"
        self.websites = website
        if address is None:
            self.addresses = "None"
        self.addresses = address
        if prices is None:
            self.prices = "None"
        self.prices = price
        if LatestPrices is None:
            self.LatestPrices = "None"
        self.LatestPrices = LatesPrice
        if validDates is None:
            self.validDates = "None"
        self.validDates = validDate
        if dates is None:
            self.dates = "None"
        self.dates = date
        if buildingSizes is None:
            self.buildingSizes = "None"
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
        print("Heimasída: ", self.websites, "\nAddressa: ", self.addresses,"\nPrísur: ", self.prices,"\nSeinasti bod: ",
              self.LatestPrices, "\nGaldandi til dato: ", self.validDates,"\nDato: ", self.dates,
              "\nm2 í húsinum: ", self.buildingSizes,"\nm2 á økinum: ", self.landSizes,
              "\nRúm: ", self.rooms,"\nHæddir: ", self.floors, "\n")
    def writeToCSV(self):
        print("test")

betriURL = 'https://www.betriheim.fo/'
betriResponse = requests.get(betriURL)
betriSoup = BeautifulSoup(betriResponse.text, 'html.parser')

skynURL = 'https://www.skyn.fo/ognir-til-soelu'
skynResponse = requests.get(skynURL)
skynSoup = BeautifulSoup(skynResponse.text, 'html.parser')

#meklarinURL = 'https://www.meklarin.fo/'
#meklarinResponse = requests.get(meklarinURL)
#meklarinSoup = BeautifulSoup(meklarinResponse.text, 'html.parser')

BetriPropertyWrappers = betriSoup.find_all('article', class_="c-property c-card grid")
SkynPropertyWrappers = skynSoup.find_all('div', class_="col-md-6 col-sm-6 col-xs-12 col-lg-4 ogn")
SkynPropertyWrappersNewbid = skynSoup.find_all('div', class_="col-md-6 col-sm-6 col-xs-12 col-lg-4 ogn newbid")
SkynPropertyWrappersNewProp = skynSoup.find_all('div', class_="col-md-6 col-sm-6 col-xs-12 col-lg-4 ogn newprop")
SkynPropertyWrappersNewPrice = skynSoup.find_all('div', class_="col-md-6 col-sm-6 col-xs-12 col-lg-4 ogn newprice")
SkynPropertyWrappersSold = skynSoup.find_all('div', class_="col-md-6 col-sm-6 col-xs-12 col-lg-4 ogn sold")
SkynPropertyWrappersFixedPrice = skynSoup.find_all('div', class_="col-md-6 col-sm-6 col-xs-12 col-lg-4 ogn fixedprice")
#meklarinPropertyWrappers = meklarinSoup.find_all('div', class_="property-item")
properties = []

def CheckValueText(property, attribute, classVal):
    value = property.find(attribute, class_=classVal)
    if value is not None:
        value = value.text
    else:
        value = None
    return value

for property in BetriPropertyWrappers:
    websites = "Betri"
    addresses = CheckValueText(property, 'address', "medium")
    prices = CheckValueText(property, 'div', "price")
    LatestPrices = CheckValueText(property, 'div', "latest-offer")
    validDates = CheckValueText(property, 'div', "valid")
    dates = CheckValueText(property, 'div', "date")
    buildingSizes = CheckValueText(property, 'div',"building-size")
    landSizes = CheckValueText(property, 'div', "land-size")
    rooms = CheckValueText(property, 'div', "rooms")
    floors = CheckValueText(property, 'div', "floors")
    prop = FaroesProperties(websites, addresses,prices,LatestPrices,
                            validDates,dates,buildingSizes,
                            landSizes,rooms,floors)
    properties.append(prop)

def skynPropertyScraper(SkynPropertyWrappers,slag):
    for property in SkynPropertyWrappers:
        websites = slag
        addresses = CheckValueText(property, 'div', "ogn_headline")
        prices = CheckValueText(property, 'div', "listprice")
        LatestPrices = CheckValueText(property, 'div', "latestoffer")
        validDates = CheckValueText(property, 'div', "validto")
        dates = CheckValueText(property, 'div', "col-xs-2 text-justify")
        buildingSizes = CheckValueText(property, 'div',"col-xs-2 col-xs-offset-1 text-justify")
        landSizes = CheckValueText(property, 'div', "col-xs-2 text-justify")
        rooms = CheckValueText(property, 'div', "col-xs-2 text-justify")
        floors = CheckValueText(property, 'div', "col-xs-2 text-justify")
        prop = FaroesProperties(websites, addresses,prices,LatestPrices,
                                validDates,dates,buildingSizes,
                                landSizes,rooms,floors)
        properties.append(prop)

skynPropertyScraper(SkynPropertyWrappers,"Skyn")
skynPropertyScraper(SkynPropertyWrappersSold,"Skyn: Selt")
skynPropertyScraper(SkynPropertyWrappersNewbid,"Skyn: Nyggj bod")
skynPropertyScraper(SkynPropertyWrappersNewProp, "Skyn: Nyggj ogn")
skynPropertyScraper(SkynPropertyWrappersNewPrice, "Skyn: Nytt bod")
skynPropertyScraper(SkynPropertyWrappersFixedPrice, "Skyn: Fasturprisur")



SkynPropertyWrappers = skynSoup.find_all('a', class_="row ogn-bottom")

for SkynPropertyWrapper in SkynPropertyWrappers:
    #SkynPropertyWr = SkynPropertyWrapper.find('div', class_="col-xs-2 text-justify").text
    SkynPropertyWr = SkynPropertyWrappers
    print(SkynPropertyWr)

#for property in meklarinPropertyWrappers:
#    websites = "Meklarin"
#    addresses = CheckValueText(property, 'div', "address")
#    prices = CheckValueText(property, 'div', "price")
#    LatestPrices = CheckValueText(property, 'div', "bid")
#    validDates = CheckValueText(property, 'div', "bid-valid-until")
#    dates = CheckValueText(property, 'div', "build")
#    buildingSizes = CheckValueText(property, 'div',"house_area")
#    landSizes = CheckValueText(property, 'div', "area_size")
#    rooms = CheckValueText(property, 'div', "bedrooms")
#    floors = CheckValueText(property, 'div', "info-item")
#    prop = FaroesProperties(websites, addresses,prices,LatestPrices,
#                            validDates,dates,buildingSizes,
#                            landSizes,rooms,floors)
#    properties.append(prop)

#for prop in properties:
#    prop.display()

#file = open('export_data.csv', 'w', newline='')
#writer = csv.writer(file)
#headers = ['Website', 'addressClass', 'priceClass','dateClass', 'buildingSizeClass', 'landSizeClass', 'roomsClass', 'floorsClass']
#writer.writerow(headers)
#for prop in properties:
#    file = open('export_data.csv', 'a', newline='', encoding='utf-8')
#    writer = csv.writer(file)
#    headers = ([prop.websites, prop.addresses, prop.prices, prop.dates, prop.buildingSizes, prop.landSizes, prop.rooms, prop.floors])
#    writer.writerow(headers)
#    file.close()

