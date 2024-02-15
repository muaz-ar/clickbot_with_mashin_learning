from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from configuration import driver
from datebase.id_check import check_id_and_get_answers
import random
import re



def clickfunktion():
    quiz_frage_xpath = '/html/body/div[1]/div/div/main/div/div[1]/div[1]/div/form/span/p'
    antworten_xpath_template = '/html/body/div[1]/div/div/main/div/div[1]/div[1]/div/form/table/tbody/tr[{}]/td[1]/label'
    id_xpath = '.tx-pt-certification > form:nth-child(4) > div:nth-child(4) .question-id'

    try:
        # Extrahieren der Frage-ID
        id_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, id_xpath)))
        id_text = id_element.text
        match = re.search(r"\(ID-(\d+)\)", id_text)
        if match:
            id_value = int(match.group(1))
            saved_answers = check_id_and_get_answers(id_value)
        else:
            id_value = None
            saved_answers = None

        antworten = []

        for i in range(1, 6):
            xpath = antworten_xpath_template.format(i)
            try:
                antwort_element = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
                antworten.append(antwort_element.text)
            except TimeoutException:
                break

        if saved_answers is not None:
            for index, richtigkeit in enumerate(saved_answers):
                if richtigkeit:
                    xpath = antworten_xpath_template.format(index + 1)
                    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        else:
            if len(antworten) <= 3:
                ausgewaehlte_indices = random.sample(range(len(antworten)), 1)
            else:
                ausgewaehlte_indices = random.sample(range(len(antworten)), random.randint(2, 3))

            for index in ausgewaehlte_indices:
                xpath = antworten_xpath_template.format(index + 1)
                WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

        button_weiter_xpath = '/html/body/div[1]/div/div/main/div/div[1]/div[1]/div/form/div[3]/span/input'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_weiter_xpath))).click()

    except Exception as e:
        print(f"Fehler beim Ausführen der clickfunktion: {e}")
