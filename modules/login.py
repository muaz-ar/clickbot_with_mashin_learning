# /modules/login.py

from selenium.common.exceptions import NoSuchElementException
from configuration import by_xpath, USER, KEY
def login():
    print("Login...")
    user_bar = by_xpath('//*[@id="loginUser"]')
    user_bar.send_keys(29177060)
    key_bar = by_xpath('//*[@id="loginPlaintextPassword"]')
    key_bar.send_keys('Helga58!?')
    button_login = by_xpath('/html/body/div[1]/div/div/main/div[4]/div/form/fieldset/div[3]/input')
    button_login.click()
    def click_button_if_exists(xpath):
        try:
            button = by_xpath(xpath)
            button.click()
        except NoSuchElementException:
            pass
    click_button_if_exists('/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/form/div[2]/span[2]/input')
    click_button_if_exists('/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/form/div[2]/span[2]/input')