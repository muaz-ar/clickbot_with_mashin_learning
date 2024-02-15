from configuration import driver
from configuration import URLCLICK
from selenium.webdriver.common.by import By


def navigate_to_response_page(): 
    driver.get(URLCLICK)
    button_to_response1 = driver.find_element(By.CSS_SELECTOR, '#ui-id-1')
    button_to_response1.click()
    button_to_response2 = driver.find_element(By.CSS_SELECTOR, '#ui-id-2 > div:nth-child(1) > a:nth-child(1)')
    button_to_response2.click()
