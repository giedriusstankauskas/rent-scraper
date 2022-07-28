from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

# Google form URL
rent_form = os.getenv('rent_form')
# Zillow.com URL
url = os.getenv('zillow_url')

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,lt;q=0.8"
}

response = requests.get(url, headers=header)
data = response.text
soup = BeautifulSoup(data, "html.parser")

# get links of houses
all_link_elements = soup.select(".list-card-top a")
links = []
for link in all_link_elements:
    href = link["href"]
    if "http" not in href:
        links.append(f'https://www.zillow.com{href}')
    else:
        links.append(href)

# get addresses of houses
all_address_elements = soup.select(".list-card-info address")
addresses = [address.get_text() for address in all_address_elements]

# get prices of houses
all_price_elements = soup.select(".list-card-price")
prices = [price.get_text().split("+") for price in all_price_elements]
