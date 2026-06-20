from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "interview_ai_secret"

# Create Database
def init_db():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# Home Page
@app.route("/")
def home():
    if "user" in session:
        return render_template("index.html", user=session["user"])
    return redirect(url_for("login"))

# Register Page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        try:
            cur.execute(
                "INSERT INTO users(username,password) VALUES(?,?)",
                (username, password)
            )
            conn.commit()
            conn.close()
            return redirect(url_for("login"))
        except:
            conn.close()
            return "User already exists"

    return render_template("register.html")

# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cur.fetchone()
        conn.close()

        if user:
            session["user"] = username
            return redirect(url_for("home"))

        return "Invalid Username or Password"

    return render_template("login.html")

# Interview Submission
@app.route("/submit", methods=["POST"])
def submit():

    score = 0

    answers = [
        request.form.get("q1", "").lower(),
        request.form.get("q2", "").lower(),
        request.form.get("q3", "").lower(),
        request.form.get("q4", "").lower(),
        request.form.get("q5", "").lower()
    ]

    keywords = [
        "python",
        "strength",
        "team",
        "database",
        "goal"
    ]

    for i in range(len(keywords)):
        if keywords[i] in answers[i]:
            score += 20

    return render_template("result.html", score=score)

# Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)