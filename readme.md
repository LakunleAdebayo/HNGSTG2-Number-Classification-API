# Number Classification API

This Django REST API provides mathematical properties and fun facts about numbers.

## Features

- Classifies numbers based on various mathematical properties
- Provides fun facts about numbers using the Numbers API
- Handles CORS for cross-origin requests
- Returns responses in JSON format

## API Endpoint

GET `/api/classify-number?number={number}`

Example Request:
GET 'http://127.0.0.1:8000/api/classify-number?number=777' 

Success Response (200 OK):
{
    "number": 777,
    "is_prime": false,
    "is_perfect": false,
    "properties": [
        "odd"
    ],
    "digit_sum": 21,
    "fun_fact": "777 is a repdigit in base 6 and in base 10."
}

Error Response (400 Bad Request):
{
    "number": "invalid_input",
    "error": true
}

## Installation

1. Clone the repository:
git clone https://github.com/LakunleAdebayo/HNGSTG2-Number-Classification-API.git
cd number-classify

2. Create and activate a virtual environment:
h
python -m venv venv
source activate virtual environment

3. Install dependencies:
pip install -r requirements.txt

4. Run migrations:
python manage.py migrate

5. Start the development server:
python manage.py runserver

### Deployment
This project is deployed on Render

### Technologies Used
. Django (Backend framework)
. Django REST Framework (API handling)
. Requests (Fetching fun facts from the Numbers API)
. CORS Headers (Handling cross-origin requests)

### Contributing
Feel free to fork this repository and submit pull requests with improvements!

