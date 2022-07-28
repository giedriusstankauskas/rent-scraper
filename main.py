from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

rent_form = os.getenv('rent_form')
