import sqlite3
#updates the hiddenword, level, and hint in the database, required fields: wordname, level, and hint
#returns num_updated; if 1 then the score was updated if 0 then it was not.
def update_row(name, level, hint):
    conn = None
    try:
        conn = sqlite3.connect('dodgecity.db')
        cur = conn.cursor()
        cur.execute('''UPDATE words
                        SET level = ?, hint = ?
                        WHERE upper(hiddenword) == ?''',
                        (level, hint, name.upper()))
        conn.commit()
        num_updated = cur.rowcount
    except sqlite3.Error as err:
            print('Database Error', err)
    finally:
            if conn != None:
                conn.close()
    return num_updated