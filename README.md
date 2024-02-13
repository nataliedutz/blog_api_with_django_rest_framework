# BLOG API

In this project, an API for a blog has been created using Django and Django REST Framework.

## Development Setup

Before you begin, ensure you have met the following requirements:

- **Python:** This project is developed using Python 3.10.12. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

- **Integrated Development Environment (IDE):**
This entire application is built using Visual Studio Code.

- **Virtual Environment (Optional, but recommended):** It's a good practice to use a virtual environment for Python projects. You can create one using the `venv` module or `virtualenv`.
Open a terminal and navigate to the project directory. Use the command:
```
On Windows    : python -m venv venv
On macOS/Linux: python3 -m venv venv
```

- **Activate the virtual environment:**
```
On Windows    : .\venv\Scripts\activate
On macOS/Linux: source venv/bin/activate
```

- **Install Dependencies:**
```
On Windows    : pip install -r requirements.txt
On macOS/Linux: pip3 install -r requirements.txt
```

- **Navigate to the outer Django project directory in your terminal and run the project from here.**


## Project Execution

- **Run Migrations for the users and posts models:**
```
On Windows    : python manage.py makemigrations 
                python manage.py migrate
On macOS/Linux: python3 manage.py makemigrations 
                python3 manage.py migrate
```

- **Start the Development Server:**
    
```
On Windows    : python manage.py runserver
On macOS/Linux: python3 manage.py runserver
```

- **Explore the API:**
    The API endpoint is available at http://127.0.0.1:8000/api/v1

- **Run Tests:**
The code for the tests can be seen in the file fee_calculator/tests.
To run the tests, use the following command in your terminal: 
```
On Windows    : python manage.py test
On macOS/Linux: python3 manage.py test
```
