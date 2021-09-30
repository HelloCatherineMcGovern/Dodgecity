import sqlite3
#Deletes a user from the database, needs supplied field username
#returns the number of rows deleted
def delete_row(user):
    conn = None
    try:
        conn = sqlite3.connect('dodgecity.db')
        cur = conn.cursor()
        cur.execute('''DELETE FROM users WHERE user == ?''',(user,))
        conn.commit()
        num_deleted = cur.rowcount
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()
    return num_deleted