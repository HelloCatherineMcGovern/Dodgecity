import sqlite3
#updates only the users score in the database, required fields: user and score
#returns num_updated; if 1 then the score was updated if 0 then it was not.
def update_row(user, score):
    conn = None
    try:
        conn = sqlite3.connect('dodgecity.db')
        cur = conn.cursor()
        cur.execute('''UPDATE users
                        SET score = ?
                        WHERE lower(user) == ?''',
                        (score, user.lower()))
        conn.commit()
        num_updated = cur.rowcount
    except sqlite3.Error as err:
            print('Database Error', err)
    finally:
            if conn != None:
                conn.close()
    return num_updated
