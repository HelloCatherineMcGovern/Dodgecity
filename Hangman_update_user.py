import sqlite3
#updates the users password and score in the database, required fields: user, password, and score
#returns num_updated; if 1 then the score was updated if 0 then it was not.
def update_row(user, password, score):
    conn = None
    try:
        conn = sqlite3.connect('dodgecity.db')
        cur = conn.cursor()
        cur.execute('''UPDATE users
                        SET password = ?, score = ?
                        WHERE lower(user) == ?''',
                        (password, score, user.lower()))
        conn.commit()
        num_updated = cur.rowcount
    except sqlite3.Error as err:
            print('Database Error', err)
    finally:
            if conn != None:
                conn.close()
    return num_updated
