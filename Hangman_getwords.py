import sqlite3, Hangman_read
#returns a users score from the database requied field is username
def getgamewords():
    allwords = []
    alllevels = []
    allhints = []
    search = "SELECT * FROM words ORDER BY hiddenword"
    wordinfo = ""
    wordinfo = Hangman_read.read_data(search)
    for w in wordinfo:
        allwords.append(w[0])
        alllevels.append(w[1])
        allhints.append(w[2])
    return allwords, alllevels, allhints