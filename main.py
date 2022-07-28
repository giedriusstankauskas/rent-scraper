from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
from functions import create_links_list, create_addresses_list, create_prices_list, fill_forms

load_dotenv()

# Google form URL
rent_form = os.getenv('rent_form_url')
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
links = create_links_list(soup)

# get addresses of houses
addresses = create_addresses_list(soup)

# get prices of houses
prices = create_prices_list(soup)

# check if scraping works
print(links)
print(addresses)
print(prices)

# selenium
chrome_driver_path = os.getenv('chrome_path')
s = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=s)

# fill forms
fill_forms(links, addresses, prices, driver, rent_form)

