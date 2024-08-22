import requests
import threading
import time
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

class part:
    def __init__(self, link):
        self.link = link
        reqs = requests.get(link)
        soup = BeautifulSoup(reqs.text, 'html.parser')

        # sku

        element1 = soup.find(class_="productView-sku-input")
        if element1 and "value" in element1:
            sku = element1["value"]
            self.sku = sku
        else:
            sku = "N/A"
            self.sku = sku
        
        
        #title

        element2 = soup.find(class_="productView-title")
        if element2:
            title = element2.text
            self.title = title
        else:
            title = "N/A"
            self.title = title
        
        #cost

        element3 = soup.find("meta", itemprop="price")
        if element3:
            price = element3["content"]
            self.price = price
        else:
            price = "N/A"
            self.price = price
        
        #step file

        element4 = soup.find(class_="product-downloadsList-listItem-link ext-zip")
        if element4:
            step = "https://www.gobilda.com" + element4["href"]
            self.step = step
        else:
            step = "N/A"
            self.step = step

    def __str__(self):
        return f"{self.title}, {self.sku}, {self.link}, {self.price}, {self.step}"
    
    def spreadsheet(self):
        ssList = self.title, self.sku, self.link, self.price, self.step
        return ssList
