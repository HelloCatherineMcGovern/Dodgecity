import sqlite3
#returns the user, password, and score based on a username
def read_item(name):
    user = ""
    password = ""
    score = ""
    conn = None
    results = []
    try:
        conn = sqlite3.connect('dodgecity.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM users WHERE lower(user) == ?''',
                    (name.lower(),))
        results = cur.fetchall()
        print(results)
        for row in results:
            user = row[0]
            password = row[1]
            score = row[2]
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()
    return user, password, score