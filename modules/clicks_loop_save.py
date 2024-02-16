#/modules/click_save_loop.py
from selenium.common.exceptions import NoSuchElementException
from configuration import driver, URLCLICK, by_xpath
import time
from clickfunktion import click_multiple_times
from read_result2 import read_all_questions_and_answers
from navigate_to_response_page import navigate_to_response_page
from datebase.create_db import create_db_and_tables
from datebase.save_db import save_data


def click_save_loop():
    
    counter = 0
    while counter < 150:  # Gesamtzahl der Durchläufe
        if URLCLICK == driver.current_url:
            print('Aktuelle URL: ', driver.current_url)
        else:
            driver.get(URLCLICK)
            print('URL click erfolgreich')
            time.sleep(1)
        
        if not navigate_to_response_page():
            continue  
        else: 
            print("navigate_to_response_page() erfolgreich")
        
        print("clickfunktion()")
        click_multiple_times(10)
        
        print("")

        fragen_ergebnisse = read_all_questions_and_answers()
        print("read_all_questions_and_answers()")
        
        print("")
        
        fragen_ergebnisse = read_all_questions_and_answers()
        print("save_data(fragen_ergebnisse)")
        save_data(fragen_ergebnisse)
        
        print("")

        print("daten erfolgeich gespeichert")    
        
        try:
            save_result = by_xpath('/html/body/div[1]/div/div/main/div/div[1]/div[1]/div/div[2]/table/tbody/tr/td[1]/a')
            save_result.click()
            print("Counter: click speichern", counter)
            counter += 1  
        except NoSuchElementException:
            print("Button 'save_result' nicht gefunden, versuche erneut...")  
            continue  