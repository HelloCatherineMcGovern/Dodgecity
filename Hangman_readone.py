import sqlite3
#returns hiddenword, level and hint based on wordname
def read_item(name):
    hiddenword = ""
    level = ""
    hint = ""
    conn = None
    results = []
    try:
        conn = sqlite3.connect('dodgecity.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM words WHERE lower(hiddenword) == ?''',
                    (name.lower(),))
        results = cur.fetchall()
        print(results)
        for row in results:
            hiddenword = row[0]
            level = row[1]
            hint = row[2]
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()
    return hiddenword, level, hint