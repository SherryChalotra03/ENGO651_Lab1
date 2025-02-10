# ENGO651_Lab1
Lab 1 introduces to Python, Flask, Postgres

**Overview**
This project is a Book Review Website built using Flask, PostgreSQL, and HTML/CSS. Users can register, log in, search for books, view book details, leave reviews, and browse reviews from other users. The application also integrates session management for authentication and user interaction.

**Features** <br>
**1. User Authentication:** Register, Login, Logout functionality.
**2. Book Search:** Search books by title, author, or ISBN. (Search also works for part of values entered by users)
**3. Book Details Page:** View book details and user reviews.
**4. Review System:** Users can leave and view reviews. (This isn't functional and will be implemented in Lab2)
**5. Session Management:** Secure user sessions with Flask.
**6. Database Integration:** Uses PostgreSQL for storing users, books, and reviews.

**Project Structure**
project1-2/
│── application.py       # Main Flask application file
│── books.csv            # Dataset with book information
│── import.py            # Script to import books.csv into PostgreSQL
│── password.txt         # Stores the database password
│── requirements.txt     # Dependencies required for the project
│── steps.txt            # Step-by-step instructions for setup (you can ignore this)
│── static/              # CSS and static files
│   └── style.css        # Main stylesheet
│── templates/           # HTML templates for Flask
│   ├── book.html        # Book details page
│   ├── index.html       # Home page
│   ├── layout.html      # Base layout for the site
│   ├── login.html       # Login page
│   ├── register.html    # Registration page
│   ├── search.html      # Search form
│   ├── search_results.html  # Search results page
│── flask_session/       # Session storage folder
│── __pycache__/         # Python cache files

**Setup and Installation**
**1. Clone the Repository:** 


**2. Install Dependencies:** Create a virtual environment and install the required packages:

If you encounter with an Policy set up issues, follow the instructions and reactive the virtual environment
**3. Setup the PostgreSQL Database:** Ensure PostgreSQL is installed and create a new database:









