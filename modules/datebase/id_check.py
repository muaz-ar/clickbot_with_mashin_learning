# /modules/datebase/id_check.py
import sqlite3

def check_id_and_get_answers(id_value):
    conn = sqlite3.connect('fragen_antworten.db')
    c = conn.cursor()
    c.execute('SELECT richtigkeit FROM antworten WHERE id=?', (id_value,))
    results = c.fetchall()
    conn.close()
    if results:
        return [result[0] for result in results]
    else:
        return None
