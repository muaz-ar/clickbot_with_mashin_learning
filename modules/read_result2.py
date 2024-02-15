#/modules/read_result2.py
from configuration import driver, by_xpath
from selenium.webdriver.common.by import By
import re
from selenium.common.exceptions import NoSuchElementException

def read_all_questions_and_answers():
    fragen_ergebnisse = []  # Liste zum Speichern der Ergebnisse für alle Fragen

    for frage_index in range(4, 14):  # Startet bei 4, endet bei 13 für die CSS-Selektoren
        try:
            # ID der Frage auslesen
            element_id = driver.find_element(By.CSS_SELECTOR, f"table.exercise-table:nth-child({frage_index}) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > span:nth-child(3)")
            id_text = element_id.text
            match = re.search(r"\(ID=(\d+)\)", id_text)
            if not match:
                print(f"ID für Frage {frage_index - 3} konnte nicht extrahiert werden.")
                continue
            id_value = match.group(1)

            # Fragestellung auslesen
            fragestellung_element = driver.find_element(By.CSS_SELECTOR, f"table.exercise-table:nth-child({frage_index}) > tbody:nth-child(1) > tr:nth-child(2) > td")
            fragestellung_text = fragestellung_element.text

            # Antworten Richtigkeit auslesen
            antworten_richtigkeit = []
            antworten_elements = driver.find_elements(By.CSS_SELECTOR, f"table.exercise-table:nth-child({frage_index}) > tbody:nth-child(1) > tr")
            antworten_anzahl = len(antworten_elements) - 2
            for antwort_index in range(3, 3 + antworten_anzahl):
                try:
                    element_antwort = driver.find_element(By.CSS_SELECTOR, f"table.exercise-table:nth-child({frage_index}) > tbody:nth-child(1) > tr:nth-child({antwort_index}) > td:nth-child(2) > img")
                    antworten_richtigkeit.append(element_antwort.get_attribute('alt') == "richtig")
                except NoSuchElementException:
                    antworten_richtigkeit.append(False)

            # Ergebnisobjekt für diese Frage
            frage_ergebnis = {
                "ID": id_value,
                "Fragestellung": fragestellung_text,
                "Antworten_Richtigkeit": antworten_richtigkeit
            }
            fragen_ergebnisse.append(frage_ergebnis)
        except Exception as e:
            print(f"Fehler beim Lesen der Daten für Frage {frage_index - 3}: {e}")

    return fragen_ergebnisse

