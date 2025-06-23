from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__, template_folder=('template'))

if not os.path.exists("gust.db"):
    con = sqlite3.connect("gust.db")
    con.execute("""CREATE TABLE IF NOT EXISTS Guste (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL)""")
    con.close()

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register')
def registr():
    return render_template('register.html')

@app.route('/cloth')
def cloth():
    return render_template('clothe.html')

@app.route('/sports')
def sport():
    return render_template('sports.html')

@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/phones')
def phone():
    return render_template('phones.html')

@app.route('/buy')
def buy():
    return render_template('buy.html')

@app.route('/bought')
def bought():
    return render_template('scs.html')

@app.route("/savedetails", methods=["POST", "GET"])
def savedetails():
    msg = ''
    if request.method == "POST":
        try:
            name = request.form["name"]
            password = request.form["password"]
            email = request.form["email"]
            with sqlite3.connect("gust.db") as con:
                cur = con.cursor()
                cur.execute('INSERT INTO Guste (name, email, password) VALUES (?, ?, ?)', (name, email, password))
                con.commit()
                msg = "User successfully registered"
        except:
            con.rollback()
            msg = "Registration failed"
        return render_template("success.html", msg=msg)

if __name__ == '__main__':
    app.run(debug=True)