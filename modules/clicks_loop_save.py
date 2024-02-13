from selenium.common.exceptions import NoSuchElementException
from configuration import driver, URLCLICK, by_xpath
import time
from random_click import clickfunktion
from read_result import read_result
from read_result2 import read_all_questions_and_answers


def click_save_loop():
    driver.get(URLCLICK)
    for _ in range(10): 
        clickfunktion()
    
    read_result()
    fragen_ergebnisse = read_all_questions_and_answers()

    if fragen_ergebnisse:
        print(fragen_ergebnisse)


    
    
    # counter = 0
    # while counter < 150:  # Gesamtzahl der Durchläufe
    #     driver.get(URLCLICK)
    #     for _ in range(10): 
    #         clickfunktion()
        


    #     try:
    #         save_result = by_xpath('/html/body/div[1]/div/div/main/div/div[1]/div[1]/div/div[2]/table/tbody/tr/td[1]/a')
    #         save_result.click()
    #         print("Counter: click speichern", counter)
    #         counter += 1  
    #     except NoSuchElementException:
    #         print("Button 'save_result' nicht gefunden, versuche erneut...")
    #         time.sleep(1)  
    #         continue  