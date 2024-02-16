from configuration import driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def navigate_to_response_page():
    try:
        button_to_response1 = driver.find_element(By.CSS_SELECTOR, '#ui-id-1 > div:nth-child(2)')
        button_to_response1.click()
        
        button_to_response2 = driver.find_element(By.CSS_SELECTOR, '#ui-id-2 > div:nth-child(1) > a:nth-child(1)')
        button_to_response2.click()
        
        return True  # Beide Buttons wurden erfolgreich geklickt
    except NoSuchElementException:
        return False 