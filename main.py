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
prices = [price.get_text().split("+")[0] for price in all_price_elements]

print(links)
print(addresses)
print(prices)

# selenium
chrome_driver_path = os.getenv('chrome_path')
s = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=s)

for n in range(len(links)):
    driver.get(rent_form)
    time.sleep(2)
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address_input.send_keys(addresses[n])
    price_input.send_keys(prices[n])
    link_input.send_keys(links[n])
    submit_button.click()

