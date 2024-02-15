from configuration import driver, by_xpath
from selenium.webdriver.common.by import By
import re
from selenium.common.exceptions import NoSuchElementException

def read_all_questions_and_answers():
    fragen_ergebnisse = []  # Liste zum Speichern der Ergebnisse für alle Fragen

    # Durchlaufen aller Fragen
    for frage_index in range(4, 14):  
        # ID der Frage auslesen
        try:
            element_id = driver.find_element(By.CSS_SELECTOR, f"table.exercise-table:nth-child({frage_index}) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > span:nth-child(3)")
            id_text = element_id.text
            match = re.search(r"\(ID=(\d+)\)", id_text)
            if match:
                id_value = match.group(1)
            else:
                print(f"ID für Frage {frage_index - 3} konnte nicht extrahiert werden.")
                continue  # Zum nächsten Schleifendurchlauf, wenn keine ID gefunden wurde
        except Exception as e:
            print(f"Fehler beim Lesen der ID für Frage {frage_index - 3}: {e}")
            continue

        # Anzahl der Antwortmöglichkeiten ermitteln
        antworten_elements = driver.find_elements(By.CSS_SELECTOR, f"table.exercise-table:nth-child({frage_index}) > tbody:nth-child(1) > tr")
        antworten_anzahl = len(antworten_elements) - 2  # Die ersten zwei `tr` sind keine Antworten

        # Antworten überprüfen
        antworten_richtigkeit = []
        for antwort_index in range(3, 3 + antworten_anzahl):
            try:
                element_antwort = driver.find_element(By.CSS_SELECTOR, f"table.exercise-table:nth-child({frage_index}) > tbody:nth-child(1) > tr:nth-child({antwort_index}) > td:nth-child(2) > img")
                antworten_richtigkeit.append(element_antwort.get_attribute('alt') == "richtig")
            except NoSuchElementException:
                antworten_richtigkeit.append(False)  # Kein `img`-Element, Antwort ist falsch

        # Ergebnisobjekt für diese Frage
        frage_ergebnis = {
            "ID": id_value,
            "Antworten_Richtigkeit": antworten_richtigkeit
        }
        fragen_ergebnisse.append(frage_ergebnis)

    # Ausgabe der Ergebnisse
    for ergebnis in fragen_ergebnisse:
        print(f"Frage ID: {ergebnis['ID']}, Antworten Richtigkeit: {ergebnis['Antworten_Richtigkeit']}")

    return fragen_ergebnisse


