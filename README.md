# ENGO651_Lab1
Lab 1 introduces to Python, Flask, Postgres

**Overview:** <br>
This project is a Book Review Website built using Flask, PostgreSQL, and HTML/CSS. Users can register, log in, search for books, view book details, leave reviews, and browse reviews from other users. The application also integrates session management for authentication and user interaction.

**Features** <br>
**1. User Authentication:** Register, Login, Logout functionality. <br>
**2. Book Search:** Search books by title, author, or ISBN. (Search also works for part of values entered by users) <br>
**3. Book Details Page:** View book details and user reviews. <br>
**4. Review System:** Users can leave and view reviews. (This isn't functional and will be implemented in Lab2) <br>
**5. Session Management:** Secure user sessions with Flask. <br>
**6. Database Integration:** Uses PostgreSQL for storing users, books, and reviews. <br>

**Project Structure** <br>
project1-2/
│── application.py       # Main Flask application file <br>
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


**2. Install Dependencies:** Create a virtual environment and install the required packages:

If you encounter with an Policy set up issues, follow the instructions and reactive the virtual environment
**3. Setup the PostgreSQL Database:** Ensure PostgreSQL is installed and create a new database:









