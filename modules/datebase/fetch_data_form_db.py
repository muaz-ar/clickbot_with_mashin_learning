import sqlite3

def fetch_data_from_db():
    conn = sqlite3.connect('fragen_antworten.db')
    cursor = conn.cursor()

    # Daten aus der Tabelle 'fragen' abrufen
    cursor.execute("SELECT * FROM fragen")
    fragen = cursor.fetchall()
    print("Fragen:")
    for frage in fragen:
        print(frage)

    # Daten aus der Tabelle 'antworten' abrufen
    cursor.execute("SELECT * FROM antworten")
    antworten = cursor.fetchall()
    print("\nAntworten:")
    for antwort in antworten:
        print(antwort)

    conn.close()

if __name__ == "__main__":
    fetch_data_from_db()
