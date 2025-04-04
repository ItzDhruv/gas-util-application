# Gas Utility Customer Service - Django Application

## Overview
A gas utility company is experiencing a high volume of customer service requests. The company's current system cannot handle the volume, leading to long wait times and poor customer service.

This **Django-based web application** provides an efficient solution for managing service requests, allowing customers to submit requests online, track their status, and view their account information. It also provides customer support representatives with a tool to manage and resolve requests efficiently.

## Features

### Customer Features
- **Service Request Submission** - Customers can submit service requests, specify the issue type, and attach files.
- **Request Tracking** - Customers can track the status of their requests.
- **Account Management** - Customers can log in and view their service history.

### Admin/Support Features
- **Manage Service Requests** - View, update, and resolve customer requests.
- **Customer Support Dashboard** - View pending and resolved requests.

## Tech Stack
- **Backend**: Django, Django REST Framework (DRF)
- **Frontend**: Django Templates / React
- **Database**: SQLite (Can be replaced with PostgreSQL/MySQL)
- **Authentication**: Django's built-in user system / JWT authentication

## Project Structure
```
gas_utility_project/          # Main Django Project
│── customer_service/         # Customer service app
│   │── migrations/           # Database migrations
│   │── templates/            # HTML templates
│   │── __init__.py
│   │── admin.py              # Admin panel customization
│   │── apps.py               # App configuration
│   │── forms.py              # Django forms for service requests
│   │── models.py             # Database models for requests & users
│   │── tests.py              # Unit tests
│   │── urls.py               # Routes for customer service
│   │── views.py              # Logic for handling service requests
│
│── gas_utility_project/      # Core Django project settings
│   │── __init__.py
│   │── asgi.py
│   │── settings.py           # Project configurations
│   │── urls.py               # Main URL routing
│   │── wsgi.py
│
│── manage.py                 # Django management script
│── db.sqlite3                 # SQLite database (Replaceable)
│── README.md                 # Project documentation
│── requirements.txt          # Dependencies
```

## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/ItzDhruv/Gas_Utility_Customer_Service.git
cd Gas_Utility_Customer_Service
```

### 2. Create & Activate Virtual Environment
```sh
python -m venv env
source env/bin/activate  # For Linux/macOS
env\Scripts\activate      # For Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Apply Migrations
```sh
python manage.py migrate
```

### 5. Run the Development Server
```sh
python manage.py runserver
```
🚀 The app will be available at **http://127.0.0.1:8000/**

## API Endpoints
| Method | Endpoint               | Description |
|--------|------------------------|-------------|
| POST   | `/customer/submit/`     | Submit a new service request |
| GET    | `/customer/track/<id>/` | Get the status of a request |
| GET    | `/admin/`               | Admin panel for support representatives |

## Future Improvements
- Implement JWT authentication for API-based login
- Add notifications for request updates
- Build a React-based frontend for better user experience

## Contributors
- **ItzDhruv** - *Backend Development*

## License
This project is licensed under the **MIT License**.

---
Feel free to contribute by submitting issues or pull requests! 🚀