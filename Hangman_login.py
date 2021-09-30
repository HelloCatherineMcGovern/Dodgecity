import sqlite3
#verifies if user is admin
#! this is not used currently!
def adminverify(username, password):
    conn = None
    try:
        conn = sqlite3.connect('dodgecity.db')
        cur = conn.cursor()
        cur.execute('SELECT isAdmin FROM users WHERE upper(user) == ?', [username.upper()])
        DatabaseisAdmins = cur.fetchall()
        if login(username, passoword):
            if not DatabaseisAdmins:
                return False
            for name in DatabaseisAdmins:
                DatabaseisAdmin = name[0]
            if DatabaseisAdmin == 1:
                return True
    except sqlite3.Error as err:
            print('Database Error', err)
    finally:
            if conn != None:
                conn.close()
    return False
#verifies that the supplied username and password match database
#returns true if username and password are correct and exist in the database
#returns false if no username or password is supplied or if username or password is incorrect
def checkUsername(username):
    conn = None
    try:
        conn = sqlite3.connect('dodgecity.db')
        cur = conn.cursor()
        cur.execute('SELECT user FROM users WHERE upper(user) == ?''', [username.upper()])
        DatabaseUsernames = cur.fetchall()
        if not DatabaseUsernames:
            return False
        for name in DatabaseUsernames:
            DatabaseUsername = name[0]
        if DatabaseUsername == username:
            return True
    except sqlite3.Error as err:
            print('Database Error', err)
    finally:
            if conn != None:
                conn.close()
    return False
