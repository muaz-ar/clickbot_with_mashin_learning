import sqlite3

def save_data(fragen_ergebnisse):
    conn = sqlite3.connect('fragen_antworten.db')
    c = conn.cursor()
    
    for frage in fragen_ergebnisse:
        # Fragestellung speichern
        c.execute('INSERT INTO fragen (id, fragestellung) VALUES (?, ?)', (frage['ID'], frage['Fragestellung']))
        
        # Antworten speichern
        for richtigkeit in frage['Antworten_Richtigkeit']:
            c.execute('INSERT INTO antworten (id, richtigkeit) VALUES (?, ?)', (frage['ID'], richtigkeit))
    
    conn.commit()
    conn.close()
