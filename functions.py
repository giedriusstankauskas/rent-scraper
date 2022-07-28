from selenium.webdriver.common.by import By
import time


# get links of houses
def create_links_list(soup):
    all_link_elements = soup.select(".list-card-top a")
    links = []
    for link in all_link_elements:
        href = link["href"]
        if "http" not in href:
            links.append(f'https://www.zillow.com{href}')
        else:
            links.append(href)
    return links


# get addresses of houses
def create_addresses_list(soup):
    all_address_elements = soup.select(".list-card-info address")
    addresses = [address.get_text() for address in all_address_elements]
    return addresses


# get prices of houses
def create_prices_list(soup):
    all_price_elements = soup.select(".list-card-price")
    prices = [price.get_text().split("+")[0] for price in all_price_elements]
    return prices


def fill_forms(links, addresses, prices, driver, rent_form):
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

