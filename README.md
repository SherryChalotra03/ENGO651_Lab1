# ENGO651_Lab1
Lab 1 introduces to Python, Flask, Postgres

# Overview: 
This project is a Book Review Website built using Flask, PostgreSQL, and HTML/CSS. Users can register, log in, search for books, view book details, leave reviews, and browse reviews from other users. The application also integrates session management for authentication and user interaction.

# Features 
**1. User Authentication:** Register, Login, Logout functionality. <br>
**2. Book Search:** Search books by title, author, or ISBN. (Search also works for part of values entered by users) <br>
**3. Book Details Page:** View book details and user reviews. <br>
**4. Review System:** Users can leave and view reviews. (This isn't functional and will be implemented in Lab2) <br>
**5. Session Management:** Secure user sessions with Flask. <br>
**6. Database Integration:** Uses PostgreSQL for storing users, books, and reviews. <br>

# Project Structure
project1-2/ <br>
│── application.py         # Main Flask application file <br>
│── books.csv            # Dataset with book information <br>
│── import.py            # Script to import books.csv into PostgreSQL <br>
│── password.txt         # Stores the database password <br>
│── requirements.txt     # Dependencies required for the project <br>
│── steps.txt            # Step-by-step instructions for setup (you can ignore this) <br>
│── static/              # CSS and static files <br>
│   └── style.css        # Main stylesheet <br>
│── templates/           # HTML templates for Flask <br>
│   ├── book.html        # Book details page <br>
│   ├── index.html       # Home page <br>
│   ├── layout.html      # Base layout for the site <br>
│   ├── login.html       # Login page <br>
│   ├── register.html    # Registration page <br>
│   ├── search.html      # Search form <br>
│   ├── search_results.html  # Search results page <br>
│── flask_session/       # Session storage folder <br>
│── __pycache__/         # Python cache files <br>

# **Setup and Installation**
**1. Clone the Repository:** 
git clone https://github.com/yourusername/project1-2.git
cd project1-2


**2. Install Dependencies:** Create a virtual environment and install the required packages:

-- Activate Virtual Environment: .venv\Scripts\activate

-- **_Note:_** If you encounter an execution policy error, you might need to change the policy for the current session: 
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
Then, try activating again.

-- pip3 install -r requirements.txt

**3. Setup the PostgreSQL Database:** Ensure PostgreSQL is installed and create a new database:
CREATE DATABASE ENGO651;
CREATE SCHEMA lab1;

_Create three tables books, users and reviews under schema lab1_

Set the Environment Variable in PowerShell
$env:DATABASE_URL = "postgresql://postgres:123456@localhost/ENGO651"

After running that, verify it's set by typing:
echo $env:DATABASE_URL
You should see: postgresql://postgres:123456@localhost/ENGO651

**4. Import Books Data**

Run the following command to populate the database:
python import.py

**5. Set the Flask App (if not already set)**
If your file is named application.py, you should also set the FLASK_APP variable:
$env:FLASK_APP = "application.py"
Again, verify it with: echo $env:FLASK_APP

**6. Run Your Flask App**
Now, start your application by running: flask run

Start the development server and Open the website in a browser at: http://127.0.0.1:5000/









