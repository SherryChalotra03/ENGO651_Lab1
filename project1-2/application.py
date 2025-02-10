from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import json
import os
import urllib.parse

app = Flask(__name__)
# setup application context
app.app_context().push()

# Database configuration
#with open('password.txt') as f:
 #   password = f.readline().strip()

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:123456@localhost:5432/ENGO651'
app.secret_key = "your_secret_key"

db = SQLAlchemy(app)

def get_db_connection():
    """Establish a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            dbname="ENGO651", 
            user="postgres", 
            password="123456", 
            host="localhost", 
            port="5432"
        )
        print("DEBUG: Database connection successful!")
        return conn
    except Exception as e:
        print(f"DEBUG: Database connection error: {e}")
        return None

# Check database connection
try:
    db.engine.connect()
    print('Connection to the database is successful')
except Exception as e:
    print(f'Error: {e}')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        print(f"DEBUG: Username received: {username}")
        print(f"DEBUG: Password received: {password}")

        if not username or not password:
            return "Error: Missing username or password"

        hashed_password = generate_password_hash(password)
        conn = get_db_connection()
        if conn is None:
            print("DEBUG: Could not establish database connection!")
            return "Error: Could not connect to database."

        cur = conn.cursor()
        try:
            cur.execute('INSERT INTO lab1.users (username, password) VALUES (%s, %s)', (username, hashed_password))
            conn.commit()
            return redirect(url_for("login"))
        except psycopg2.IntegrityError:
            conn.rollback()
            return "Error: User already exists"
        finally:
            cur.close()
            conn.close()

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, password FROM lab1.users WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            print(f"DEBUG: User found in database: {user}")  # Check if user exists
            stored_password = user[1]

            if check_password_hash(stored_password, password):
                print("DEBUG: Password matched successfully!")
                session["user_id"] = user[0]
                return redirect(url_for("search"))
            else:
                print("DEBUG: Password did NOT match!")
                return "Invalid credentials"

        print("DEBUG: User not found in database!")
        return "Invalid credentials"

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query")
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM lab1.books WHERE isbn ILIKE %s OR title ILIKE %s OR author ILIKE %s", 
                    (f"%{query}%", f"%{query}%", f"%{query}%"))
        books = cur.fetchall()
        cur.close()
        conn.close()
        return render_template("search_results.html", books=books)
    return render_template("search.html")

@app.route("/book/<int:book_id>", methods=["GET", "POST"])
def book(book_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM lab1.books WHERE id = %s", (book_id,))
    book = cur.fetchone()
    cur.execute("SELECT reviews.rating, reviews.review, users.username FROM lab1.reviews JOIN lab1.users ON reviews.user_id = users.id WHERE book_id = %s", (book_id,))
    reviews = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("book.html", book=book, reviews=reviews)

@app.route("/api/<isbn>")
def book_api(isbn):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE isbn = %s", (isbn,))
    book = cur.fetchone()
    cur.close()
    conn.close()
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify({
        "title": book[2],
        "author": book[3],
        "year": book[4],
        "isbn": book[1]
    })

if __name__ == "__main__":
    conn = get_db_connection()
    if conn:
        print("Database connection successful!")
        conn.close()
    else:
        print("Database connection failed.")
    app.run(debug=True)
