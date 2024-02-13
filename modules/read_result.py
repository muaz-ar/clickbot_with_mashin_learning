from configuration import driver, by_xpath
from selenium.webdriver.common.by import By

def read_result(): 
    print("Lese Ergebnis...")
    element = driver.find_element(By.CSS_SELECTOR, "table.exercise-table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > span:nth-child(3)")

    id_text = element.text
    print("Gefundener Text:", id_text)

    import re
    match = re.search(r"\(ID=(\d+)\)", id_text)
    if match:
        id_value = match.group(1)
        print("Gefundene ID:", id_value)
    else:
        print("ID konnte nicht extrahiert werden")



def check_richtigkeiten():
    ergebnisse = []  # Liste zum Speichern der Ergebnisse
    
    # Anzahl der Fragen, kann angepasst werden, falls nötig
    anzahl_fragen = 5
    
    for i in range(1, anzahl_fragen + 1):
        try:
            element = driver.find_element(By.CSS_SELECTOR, f"table.exercise-table:nth-child(4) > tbody:nth-child(1) > tr:nth-child({6-i}) > td:nth-child(2) > img")
            if element.get_attribute('alt') == "richtig":
                ergebnisse.append(True)
            else:
                ergebnisse.append(False)
        except:
            # Fügt False hinzu, wenn das Element nicht gefunden wird oder kein `img`-Element vorhanden ist
            ergebnisse.append(False)
    
    # Ausgabe der Ergebnisse
    for index, ergebnis in enumerate(ergebnisse, start=1):
        print(f"Frage {index} richtig:", ergebnis)
    
    return ergebnisse



