# /modules/configuration.py

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv
from selenium import webdriver
import os
from selenium.webdriver.common.by import By

load_dotenv()
USER = os.getenv('USER')
KEY = os.getenv('KEY')
URLLOGIN = os.getenv('URLLOGIN')
URLCLICK = os.getenv('URLCLICK')

options = Options()
gecko_path = '/snap/bin/firefox.geckodriver'
service = Service(executable_path=gecko_path)
options.headless = True
driver = webdriver.Firefox(service=service, options=options)

def by_xpath(xpath):
    return driver.find_element(By.XPATH, xpath)
driver.get(URLLOGIN)
print('Configuration')