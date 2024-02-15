import sqlite3

def create_db_and_tables():
    conn = sqlite3.connect('fragen_antworten.db')
    c = conn.cursor()

    # Tabelle für Fragestellungen
    c.execute('''CREATE TABLE IF NOT EXISTS fragen (
                 id INTEGER PRIMARY KEY,
                 fragestellung TEXT)''')

    # Tabelle für Antworten
    c.execute('''CREATE TABLE IF NOT EXISTS antworten (
                 id INTEGER,
                 richtigkeit BOOLEAN,
                 FOREIGN KEY(id) REFERENCES fragen(id))''')
    conn.commit()
    conn.close()

