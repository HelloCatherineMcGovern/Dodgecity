import sqlite3
#Creates a user in the database, needs supplied fields user, password, and score
#returns 0 if user was created, returns -1 if user was not created.
def insert_row(user, password, score):
    conn = None
    try:
        conn = sqlite3.connect('dodgecity.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO users (user, password, score)
                    VALUES (?,?,?)''',
                    (user, password, score))
        conn.commit()
        success = 0
    except sqlite3.Error as err:
        print('Database Error', err)
        success = -1
    finally:
        if conn != None:
            conn.close()
    return success