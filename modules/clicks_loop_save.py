#/modules/click_save_loop.py
from selenium.common.exceptions import NoSuchElementException
from configuration import driver, URLCLICK, by_xpath
import time
from clickfunktion import clickfunktion
from read_result import read_result
from read_result2 import read_all_questions_and_answers
from navigate_to_response_page import navigate_to_response_page
from datebase.create_db import create_db_and_tables
from datebase.save_db import save_data

print("click_save_loop.py")
def click_save_loop():
    print('Navigiere zur Ergebnisseite')
    navigate_to_response_page()
    for _ in range(10): 
        print("random_click.py")
        clickfunktion()
    
    read_result()
    print("read_result.py", read_result())
    fragen_ergebnisse = read_all_questions_and_answers()
    print("create_db_and_tables()")
    create_db_and_tables()
    print("save_data(fragen_ergebnisse)")
    save_data(fragen_ergebnisse)

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