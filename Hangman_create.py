import sqlite3
#Creates a word in the database, needs supplied fields wordname, level, and hint
#returns 0 if word was created, returns -1 if word was not created.
def insert_row(name, level, hint):
    conn = None
    try:
        conn = sqlite3.connect('dodgecity.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO words (hiddenword, level, hint)
                    VALUES (?,?,?)''',
                    (name.upper(), level, hint))
        conn.commit()
        success = 0
    except sqlite3.Error as err:
        print('Database Error', err)
        success = -1
    finally:
        if conn != None:
            conn.close()
    return success