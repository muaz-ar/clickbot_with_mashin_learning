import sqlite3

def check_tables():
    conn = sqlite3.connect('fragen_antworten.db')
    c = conn.cursor()
    # Abrufen der Liste aller Tabellen
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()
    for table in tables:
        print(table[0])
    conn.close()

if __name__ == "__main__":
    check_tables()
