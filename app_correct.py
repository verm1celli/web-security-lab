
from flask import Flask, render_template, request 
import sqlite3


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/hello")
def hello():
    return "Hello from Python!"

@app.route("/about")
def about():
    return "This is my cybersecurity lab"



@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")

    elif request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        query = """
        SELECT * FROM users
        WHERE username = ?
        AND password = ?
        """

        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        connection.close()

        if user:
            return f"Добро пожаловать, {username}!"

        else:
            return "Неверный логин или пароль!"


@app.route("/search")
def search():

    query = request.args.get("q", "")

    return render_template("search.html", query=query)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
