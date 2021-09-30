import sqlite3
#returns a users score from the database requied field is username
def getscore(user):
    conn = None
    score = 0.0
    try:
        conn = sqlite3.connect('dodgecity.db')
        cur = conn.cursor()
        cur.execute('SELECT score FROM users WHERE upper(user) == ?''', [user.upper()])
        scores = cur.fetchall()
        for s in scores:
            score = s[0]
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()
    return score
