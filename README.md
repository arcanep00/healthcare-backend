# Healthcare Backend API

A production-style Healthcare Backend built with Django REST Framework.

## Features

* JWT Authentication (Login & Refresh Tokens)
* Patient Management APIs
* Doctor Management APIs
* Patient-Doctor Mapping APIs
* Search & Ordering Support
* Pagination
* Custom Exception Handling
* PostgreSQL Database Integration
* Environment Variable Configuration
* RESTful API Design

---

## Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
* Simple JWT
* Python Dotenv

---

## Project Structure

```text
healthcare_backend/
│
├── accounts/
├── patient/
├── doctors/
├── mappings/
├── healthcare_backend/
│   ├── settings.py
│   ├── urls.py
│   ├── exceptions.py
│
├── .env.example
├── requirements.txt
├── manage.py
└── README.md
```

---

## Setup Instructions

### Clone Repository

```bash
git clone <repository-url>
cd healthcare_backend
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key

DEBUG=True

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

### Run Migrations

```bash
python manage.py migrate
```

### Start Development Server

```bash
python manage.py runserver
```

Server will start at:

```text
http://127.0.0.1:8000/
```

---

## Authentication APIs

### Register

```http
POST /api/auth/register/
```

### Login

```http
POST /api/auth/login/
```

### Refresh Token

```http
POST /api/auth/token/refresh/
```

---

## Patient APIs

### Create Patient

```http
POST /api/patient/
```

### Get Patients

```http
GET /api/patient/
```

### Retrieve Patient

```http
GET /api/patient/{id}/
```

### Update Patient

```http
PUT /api/patient/{id}/
```

### Delete Patient

```http
DELETE /api/patient/{id}/
```

---

## Doctor APIs

### Create Doctor

```http
POST /api/doctors/
```

### Get Doctors

```http
GET /api/doctors/
```

### Retrieve Doctor

```http
GET /api/doctors/{id}/
```

### Update Doctor

```http
PUT /api/doctors/{id}/
```

### Delete Doctor

```http
DELETE /api/doctors/{id}/
```

---

## Patient-Doctor Mapping APIs

### Assign Doctor To Patient

```http
POST /api/mappings/
```

Example Request:

```json
{
    "patient": 1,
    "doctor": 2
}
```

### Get Assigned Doctors For Patient

```http
GET /api/mappings/patient/{patient_id}/
```

Example Response:

```json
{
    "patient_id": "1",
    "doctors": [
        {
            "id": 2,
            "name": "Dr Sharma",
            "specialization": "Cardiology"
        }
    ]
}
```

---

## Pagination

Default page size:

```text
10 records per page
```

Example:

```http
GET /api/patient/?page=2
```

---

## Security

* JWT-based authentication
* Environment variables for sensitive settings
* PostgreSQL database support
* Custom API exception handling

---

## Author

Abhinav Pandey

Backend Developer | Django REST Framework | PostgreSQL

```
```
