# /modules/database/save_db.py
import sqlite3

def save_data(fragen_ergebnisse):
    conn = sqlite3.connect('fragen_antworten.db')
    c = conn.cursor()
    
    for frage in fragen_ergebnisse:
        # Überprüfen, ob die Frage-ID bereits existiert
        c.execute('SELECT id FROM fragen WHERE id=?', (frage['ID'],))
        if c.fetchone() is None:
            # Fragestellung speichern, wenn die ID noch nicht existiert
            c.execute('INSERT INTO fragen (id, fragestellung) VALUES (?, ?)', (frage['ID'], frage['Fragestellung']))

            # Antworten speichern
            for richtigkeit in frage['Antworten_Richtigkeit']:
                c.execute('INSERT INTO antworten (id, richtigkeit) VALUES (?, ?)', (frage['ID'], richtigkeit))
                
        else:
            print("vorhanden")

    conn.commit()
    conn.close()


