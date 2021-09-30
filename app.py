from flask import Flask, render_template, request, redirect
import Hangman_create, Hangman_create_user, Hangman_read, Hangman_readone, Hangman_readone_user, Hangman_delete, Hangman_delete_user, Hangman_update, Hangman_update_user, Hangman_update_user_score, Hangman_login, Hangman_user_get_score, Hangman_getwords

app = Flask(__name__)
wordinfo = []
userinfo = []
#>--------------------------LOGIN PAGE:
#>--------------------------LOGIN PAGE: 
#>--------------------------LOGIN PAGE:
#>--------------------------LOGIN PAGE:
@app.route("/",methods = ['POST','GET'])
def homepage():
    user = ""
    password = ""
    errormsg = ""
    score = ""
    allwords = []
    alllevels = []
    allhints = []
    if request.method == 'POST':
        allwords, alllevels, allhints = Hangman_getwords.getgamewords()
        if request.form['btn_id'] == 'Login':
            user = request.form['user'].lower()
            if not user:
                errormsg = "You must enter a valid user name or password."
            else:
                isloggedin = Hangman_login.checkUsername(user)
                if isloggedin:
                    score = Hangman_user_get_score.getscore(user)
                    return render_template("hangman.html", user = user, score = score, allwords = allwords, alllevels = alllevels, allhints = allhints)
                else:
                    errormsg = "INVALID CREDENTIALS"
    return render_template("index.html", errormsg = errormsg)
#>--------------------------MANAGE WORDS:   
#>--------------------------MANAGE WORDS:     
#>--------------------------MANAGE WORDS:    
#>--------------------------MANAGE WORDS:
@app.route("/manage_words_readuser/<string:user>", methods = ['POST','GET'])
def manage_words(user):
    return render_template("manage_words.html", user = user)
#>--------------------------HANGMAN GAME ROUTE:   
#>--------------------------HANGMAN GAME ROUTE:   
#>--------------------------HANGMAN GAME ROUTE:   
#>--------------------------HANGMAN GAME ROUTE:  
@app.route("/<string:user>", methods = ['POST','GET'])
def hangman(user):
    topscores = []
    userinfo = []
    errormsg = ""
    searchUser = ""
    searchPassword = ""
    searchScore = ""
    allwords, alllevels, allhints = Hangman_getwords.getgamewords()
    score = Hangman_user_get_score.getscore(user)
    if request.method == 'GET':
        return render_template("hangman.html", user = user, score = score, allwords = allwords, alllevels = alllevels, allhints = allhints)
#>--------------------------------------record SCORES:
#>--------------------------------------record SCORES:
    if request.form['btn_id'] == 'recordScore':
        user = request.form['scoreUser']
        testscore = request.form['score']
        score = Hangman_user_get_score.getscore(user)
        if not testscore == "":
            if float(score) < float(testscore):
                score = testscore
                errormsg = "Score Updated!"
                num_updated = Hangman_update_user_score.update_row(user, score)
                if num_updated == 0:
                    errormsg = "database error"
            else:
                errormsg = "Your old highscore is too high to save your current one!"
        else:
            errormsg = "there is no new score to update."
#>--------------------------------------SEARCH TOP SCORES:
#>--------------------------------------SEARCH TOP SCORES:
    elif request.form['btn_id'] == 'Top Scores':
        search = 'SELECT user, score FROM users ORDER BY score DESC LIMIT 3'
        userinfo = Hangman_read.read_data(search)
#>--------------------------------------SEARCH SCORES: 
#>--------------------------------------SEARCH SCORES: 
    elif request.form['btn_id'] == 'Search User':
        searchUser = request.form['userSearch']
        if not searchUser:
            errormsg = "Please enter a user to search for!"
        isuser = Hangman_login.checkUsername(searchUser)
        if not isuser:
            errormsg = "not a valid user!"
            searchUser = ""
        else:
            searchUser, searchPassword, searchScore = Hangman_readone_user.read_item(searchUser)
    return render_template("hangman.html",searchUser = searchUser, searchScore = searchScore, userinfo = userinfo, errormsg = errormsg, user = user, score = score, allwords = allwords, alllevels = alllevels, allhints = allhints)
#>--------------------------ADMIN:   
#>--------------------------ADMIN:     
#>--------------------------ADMIN:    
#>--------------------------ADMIN:    
@app.route("/admin")
def adminpage():
    return render_template("admin.html")
#>-----------------------------CREATE USER ROUTE:
#>-----------------------------CREATE USER ROUTE:
#>-----------------------------CREATE USER ROUTE:
#>-----------------------------CREATE USER ROUTE:
@app.route("/add_user", methods = ['POST','GET'])
def add_user():
    if request.method == 'POST':
        user = request.form['user'].lower()
        if not user:
            errormsg = "Enter a User"
        else:
            errormsg = ""
            password = request.form['password']
            score = 0
            success_code = Hangman_create_user.insert_row(user,password,score)
            if success_code == 0:
                errormsg = "Data added successfully"
                userinfo.append(f"{user} | {password} | {score}")
            else:
                errormsg = "Database error -- user already exists"
        return render_template("add_user.html", userinfo = userinfo, errormsg = errormsg)
    else:
        return render_template("add_user.html")
#>-----------------------------CREATE WORD ROUTE:
#>-----------------------------CREATE WORD ROUTE:
#>-----------------------------CREATE WORD ROUTE:
#>-----------------------------CREATE WORD ROUTE:
@app.route("/add_word/<string:user>", methods = ['POST','GET'])
def add_word(user):
    if request.method == 'POST':
        name = request.form['name'].upper()
        if not name:
            errormsg = "Enter a Word"
        else:
            errormsg = ""
            if len(name) > 10:
                level = "H"
            elif len(name) > 5:
                level = "M"
            else:
                level = "E"
            hint = request.form['hint']
            success_code = Hangman_create.insert_row(name,level,hint)
            if success_code == 0:
                errormsg = "Data added successfully"
                wordinfo.append(f"{name} | {level} | {hint}")
            else:
                errormsg = "Database error -- hiddenword already exists"
        return render_template("add_word.html", wordinfo = wordinfo, errormsg = errormsg, user = user)
    else:
        return render_template("add_word.html", user = user)
#>-----------------------------READ USER ROUTE:
#>-----------------------------READ USER ROUTE:
#>-----------------------------READ USER ROUTE:
#>-----------------------------READ USER ROUTE:
@app.route("/read_user")
def read_user():
    search = "SELECT * FROM users ORDER by score"
    userinfo = ""
    userinfo = Hangman_read.read_data(search)
    return render_template("read_user.html", userinfo = userinfo) 
#>-----------------------------READ WORD ROUTE:
#>-----------------------------READ WORD ROUTE:
#>-----------------------------READ WORD ROUTE:
#>-----------------------------READ WORD ROUTE:
@app.route("/read_word/<string:user>")
def read_word(user):
    search = "SELECT * FROM words ORDER by hiddenword"
    wordinfo = ""
    wordinfo = Hangman_read.read_data(search)
    return render_template("read_word.html", wordinfo = wordinfo, user = user) 
#>-----------------------------READ TOP USER ROUTE:
#>-----------------------------READ TOP USER ROUTE:
#>-----------------------------READ TOP USER ROUTE:
#>-----------------------------READ TOP USER ROUTE:
@app.route("/read_top_users")
def read_top_users():
    search = "SELECT user, score FROM users ORDER BY score DESC LIMIT 3"
    wordinfo = ""
    wordinfo = Hangman_read.read_data(search)
    return render_template("read_word.html", wordinfo = wordinfo) 
#>-----------------------------READ SCORE ROUTE:
#>-----------------------------READ SCORE ROUTE:
#>-----------------------------READ SCORE ROUTE:
#>-----------------------------READ SCORE ROUTE:
@app.route("/read_score", methods = ['POST','GET'])
def read_score():
    if request.method == 'POST':
        user = ""
        password = ""
        score = ""
        user = request.form['user'].lower()
        if not user:
            errormsg = "You must enter a user's name."
        else:
            errormsg = ""
            user, password, score = Hangman_readone_user.read_item(user)
            if not user:
                errormsg = "Database error -- User not found"
            else:
                errormsg = ""
        return render_template("read_score.html", user = user, score = score, errormsg = errormsg)
    else:
        return render_template("read_score.html")
#>-----------------------------UPDATE USER ROUTE:
#>-----------------------------UPDATE USER ROUTE:
#>-----------------------------UPDATE USER ROUTE:
#>-----------------------------UPDATE USER ROUTE:
@app.route("/update_user", methods = ['POST','GET'])
def update_user():
    if request.method == 'POST':
        user = ""
        password = ""
        score = ""
        if request.form['btn_id'] == 'Search':
            user = request.form['user'].lower()
            if not user:
                errormsg = "You must enter a user's name."
            else:
                errormsg = ""
                user, password, score = Hangman_readone_user.read_item(user)
                if not user:
                    errormsg = "Database error -- User not found"
                else:
                    errormsg = ""
            return render_template("update_user.html", user = user, password = password, score = score, errormsg = errormsg)
        elif request.form['btn_id'] == 'Update':
            print("processing update")
            user = request.form['user']
            print(user)
            if not user:
                errormsg = "You must enter and search for a user before you can update the password"
                return render_template("update_user.html", errormsg = errormsg)
            else:
                password = request.form['password']
                score = request.form['score']
                print(password, score)
                num_updated = Hangman_update_user.update_row(user, password, score)
                print(num_updated)
                if num_updated == 0:
                    errormsg = "Database error"
                else:
                    errormsg = "Record Updated"
            return render_template("update_user.html", user = user, password = password, score = score, errormsg = errormsg)
    else:
        return render_template("update_user.html")
#>-----------------------------UPDATE WORD ROUTE:
#>-----------------------------UPDATE WORD ROUTE:
#>-----------------------------UPDATE WORD ROUTE:
#>-----------------------------UPDATE WORD ROUTE:
@app.route("/update_word/<string:user>", methods = ['POST','GET'])
def update_word(user):
    if request.method == 'POST':
        hiddenword = ""
        level = ""
        hint = ""
        if request.form['btn_id'] == 'Search':
            hiddenword = request.form['hiddenword'].upper()
            if not hiddenword:
                errormsg = "You must enter a word."
            else:
                errormsg = ""
                hiddenword, level, hint = Hangman_readone.read_item(hiddenword)
                if not hiddenword:
                    errormsg = "Database error -- Word not found"
                else:
                    errormsg = ""
            return render_template("update_word.html", hiddenword = hiddenword, level = level, hint = hint, errormsg = errormsg, user = user)
        elif request.form['btn_id'] == 'Update':
            print("processing update")
            hiddenword = request.form['hiddenword']
            print(hiddenword)
        if not hiddenword:
            errormsg = "You must enter and search for a word before you can update it"
            return render_template("update_word.html", errormsg = errormsg, user = user)
        else:
            hint = request.form['hint']
            print(hint)
            level = request.form['level'].upper()
            print(level)
            if level != "H" and level != "M" and level !="E":
                errormsg = "Enter E,M, or H for Level"
            else:
                print(level, hint)
                num_updated = Hangman_update.update_row(hiddenword, level, hint)
                print(num_updated)
                if num_updated == 0:
                    errormsg = "Database error"
                else:
                    errormsg = "Record Updated"
            return render_template("update_word.html", hiddenword = hiddenword, level = level, hint = hint, errormsg = errormsg, user = user)
    else:
        return render_template("update_word.html", user = user)
#>-----------------------------READ/DELETE ROUTE:
#>-----------------------------READ/DELETE ROUTE:
#>-----------------------------READ/DELETE ROUTE:
#>-----------------------------READ/DELETE ROUTE:
@app.route('/read_delete/<string:user>')
def read_delete(user):
        search = "SELECT * FROM words ORDER BY hiddenword"
        wordinfo = ""
        wordinfo = Hangman_read.read_data(search)
        return render_template("delete_word.html", wordinfo = wordinfo, user = user)
#>-----------------------------DELETE WORD ROUTE:
#>-----------------------------DELETE WORD ROUTE:
#>-----------------------------DELETE WORD ROUTE:
#>-----------------------------DELETE WORD ROUTE:
@app.route("/delete_word/<string:hiddenword>/<string:user>", methods = ['POST', 'GET'])
def delete(hiddenword, user):
    Hangman_delete.delete_row(hiddenword)
    return redirect('/read_delete/'+user)
#>-----------------------------READ/DELETE USER ROUTE:
#>-----------------------------READ/DELETE USER ROUTE:
#>-----------------------------READ/DELETE USER ROUTE:
#>-----------------------------READ/DELETE USER ROUTE:
@app.route('/read_delete_user')
def read_delete_user():
        search = "SELECT * FROM users ORDER BY user"
        userinfo = ""
        userinfo = Hangman_read.read_data(search)
        return render_template("delete_user.html", userinfo = userinfo)    
#>-----------------------------DELETE USER ROUTE:
#>-----------------------------DELETE USER ROUTE:
#>-----------------------------DELETE USER ROUTE:
#>-----------------------------DELETE USER ROUTE:
@app.route("/delete_user/<string:user>", methods = ['POST', 'GET'])
def delete_user(user):
    Hangman_delete_user.delete_row(user)
    return redirect("/read_delete_user")
