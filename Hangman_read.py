import sqlite3
#reads data from database based on a search string, supply the sql statement in string format
#returns a list of results
def read_data(searchString):
    conn = None
    results = []
    try:
        conn = sqlite3.connect('dodgecity.db')
        cur = conn.cursor()
        cur.execute(searchString)
        results = cur.fetchall()
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()
    return results
