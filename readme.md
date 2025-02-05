# Number Classification API

## Overview
The **Number Classification API** is a Django-based API that classifies numbers based on mathematical properties and returns interesting facts about them. It determines whether a number is prime, an Armstrong number, odd or even, and provides the sum of its digits along with a fun fact.

## Features
- Classifies numbers as **prime**, **Armstrong**, **odd**, or **even**.
- Computes the **sum of the digits**.
- Fetches a **fun fact** from the Numbers API.
- Returns results in **JSON format**.

## API Endpoint
### **GET /api/classify-number?number={number}**

#### Example Request:
```
GET http://127.0.0.1:8000/api/classify-number?number=371
```

#### Success Response (200 OK):
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### Error Response (400 Bad Request):
```json
{
    "number": "invalid_input",
    "error": true
}
```

## Installation

### **1. Clone the repository**
```bash
git clone https://github.com/yourusername/number-classification-api.git
cd number-classification-api
```

### **2. Create a virtual environment** (Optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### **3. Install dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the server**
```bash
python manage.py runserver
```

## Deployment
To deploy the project, use services like **Render, Railway, or Heroku**.

## Technologies Used
- **Django** (Backend framework)
- **Django REST Framework** (API handling)
- **Requests** (Fetching fun facts from the Numbers API)
- **CORS Headers** (Handling cross-origin requests)

## Contributing
Feel free to fork this repository and submit pull requests with improvements!

## License
This project is licensed under the MIT License.

