import csv
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

# Load environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set. Please set it before running this script.")

# Set up database connection
engine = create_engine(DATABASE_URL)
db = scoped_session(sessionmaker(bind=engine))

def import_books():
    """Reads books.csv and inserts data into the lab1.books table."""
    with open("books.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        with engine.connect() as conn:
            for isbn, title, author, year in reader:
                try:
                    conn.execute(
                        text("INSERT INTO lab1.books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)"),
                        {"isbn": isbn, "title": title, "author": author, "year": int(year)}
                    )
                except Exception as e:
                    print(f"Error inserting {isbn}: {e}")

            conn.commit()  # Commit all inserts at once

    print("Books successfully imported!")

if __name__ == "__main__":
    import_books()
