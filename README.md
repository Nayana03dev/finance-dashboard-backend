# Finance Dashboard Backend

A scalable backend system built using **Django** and **Django REST Framework** to manage financial records and provide analytical insights through secure REST APIs.

---

## Highlights

* Role-based access control (Viewer, Analyst, Admin)
* JWT authentication for secure access
* Dashboard analytics with aggregated insights
* Filtering and pagination support
* Swagger API documentation for easy testing

---

## Objective

This project aims to:

* Manage financial transactions efficiently
* Support multiple user roles with controlled access
* Provide meaningful dashboard-level analytics
* Demonstrate scalable and production-ready backend design

---

## User Roles

### Viewer

* Can view only their own dashboard
* Restricted to personal financial data
* No access to other users’ records

### Analyst

* Can view and analyze all users’ financial data
* Can access any user’s dashboard using query parameters
* Designed for data analysis using tools like Postman

### Admin

* Full system access
* Can create, update, and delete records
* Can manage users and access all data

---

## Access Control

* Implemented using Django REST Framework permissions
* `IsAuthenticated` ensures only authenticated users can access APIs
* Role-based permissions control read and write operations
* Admin and Analyst roles can dynamically access any user’s dashboard

Viewers are strictly restricted to their own data, ensuring strong data isolation.

---

## Financial Records

Each financial record contains:

* Amount
* Type (Income / Expense)
* Category
* Date
* Notes

### Supported Operations

* Create → Admin only
* Read → All users
* Update → Admin only
* Delete → Admin only

---

## Filtering & Search

Supports query-based filtering:

```bash
?type=income
?category=Food
?date=2026-04-05
?user_id=2
```

* Available for all users
* Data visibility controlled based on roles
* Enables flexible querying of financial records

---

## Dashboard API

Provides aggregated financial insights:

* Total income
* Total expense
* Net balance
* Category-wise analysis
* Recent transactions
* Monthly trends

### Example Requests

```bash
/api/dashboard/?user_id=2
/api/dashboard/?username=User1
```

---

## System Architecture

The project follows a clean layered architecture:

* Serializer → Handles validation and data formatting
* View → Contains business logic
* Permission → Controls access and security

This separation ensures modularity, maintainability, and scalability.

---

## Additional Enhancements

* JWT-based authentication for secure access
* Pagination support for efficient data handling
* Search and filtering capabilities
* Swagger UI for API documentation and testing
* Accessible at `/swagger/`

---

## Tech Stack

* Python
* Django
* Django REST Framework
* SQLite
* JWT Authentication

---

## Database

* SQLite used for simplicity and ease of setup
* Stored locally as `db.sqlite3`
* Suitable for development environments

---

## API Documentation

Interactive API documentation is available via Swagger:

```bash
/swagger/
```

---

## Setup Instructions

```bash
# Clone repository
git clone https://github.com/<your-username>/finance-dashboard-backend.git
cd finance-dashboard-backend

# Create virtual environment
python -m venv env
env\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

---

## Authentication

### Get Token

```bash
POST /api/token/
```

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

### Use Token

```bash
Authorization: Bearer <your_token>
```

---

## API Endpoints

| Endpoint          | Description              |
| ----------------- | ------------------------ |
| `/api/records/`   | Manage financial records |
| `/api/dashboard/` | Dashboard analytics      |
| `/api/users/`     | User management          |
| `/api/token/`     | JWT authentication       |
| `/swagger/`       | API documentation        |

---

## Assumptions

* Analysts can access and analyze all users’ data
* Admins have full system control
* Viewers are restricted to their own data
* SQLite is sufficient for development purposes

---

## Tradeoffs

* SQLite used instead of PostgreSQL for simplicity
* No soft delete functionality implemented
* No rate limiting included
* Basic filtering instead of advanced search

---

## Why This Project

This project demonstrates:

* Strong backend architecture design
* Role-based access control implementation
* Secure authentication using JWT
* Real-world API design and structuring
* Clean and scalable code organization

---

## Future Improvements

* Soft delete functionality
* PostgreSQL database integration
* Rate limiting and caching
* Unit and integration testing
* Docker-based deployment

---

## Author

Nayana Dev

---

## Conclusion

This project showcases a practical and scalable backend system with a strong focus on:

* Security
* Clean architecture
* Role-based access control
* Real-world API design

---





