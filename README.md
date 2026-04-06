Finance Dashboard Backend

A scalable backend system built using Django and Django REST Framework to manage financial records and provide analytical insights through secure REST APIs. The project focuses on clean architecture, role-based access control, and real-world backend design practices.

Objective
Manage financial transactions efficiently
Support multiple user roles with secure access
Provide dashboard-level analytics
Demonstrate scalable backend design
Features
Authentication
JWT-based authentication
Secure API access using tokens
Only authenticated users can access endpoints
User Roles
Viewer
Can view only their own dashboard
Restricted to personal financial data
Analyst
Can view and analyze all users’ financial records
Can access any user’s dashboard using query parameters
Acts as a data analyst using APIs (e.g., Postman)
Admin
Full access to the system
Can create, update, delete records
Can manage users and access any data
Access Control
Implemented using Django REST Framework permissions
IsAuthenticated ensures only logged-in users can access APIs
Role-based permissions control read/write access
Dynamic access allows Admins and Analysts to view any user’s dashboard

Viewers are strictly limited to their own data, ensuring strong data isolation.

Financial Records

Each record includes:

Amount
Type (Income / Expense)
Category
Date
Notes
Operations
Create (Admin only)
Read (All roles)
Update (Admin only)
Delete (Admin only)
Filtering

Filtering is supported via query parameters:

?type=income
?category=Food
?date=2026-04-05
?user_id=2
Filtering is available to all users
Data visibility is controlled based on role
Dashboard API

Provides aggregated financial insights:

Total income
Total expense
Net balance
Category-wise analysis
Recent transactions
Monthly trends
Example
/api/dashboard/?user_id=2
/api/dashboard/?username=User1
Backend Architecture

The project follows a clean separation of concerns:

Serializer → Data validation
View → Business logic
Permissions → Access control

This ensures modular, maintainable, and scalable code.

Additional Enhancements
Authentication implemented using JWT tokens for secure API access
Pagination added to record listing endpoints to efficiently handle large datasets
Search and filtering support for querying financial records
API documentation provided using Swagger UI
Swagger accessible at /swagger/
Tech Stack
Python
Django
Django REST Framework
SQLite
JWT Authentication
Database
Uses SQLite for simplicity
Stored locally as db.sqlite3
Suitable for development environments
API Documentation

Swagger UI is available for testing APIs:

/swagger/
Setup Instructions
# Clone repository
git clone https://github.com/<your-username>/finance-dashboard-backend.git
cd finance-dashboard-backend

# Create virtual environment
python -m venv env
env\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
Authentication
Get Token
POST /api/token/
{
  "username": "your_username",
  "password": "your_password"
}
Use Token
Authorization: Bearer <your_token>
API Endpoints
Endpoint	Description
/api/records/	Manage financial records
/api/dashboard/	Dashboard analytics
/api/users/	User management
/api/token/	JWT authentication
/swagger/	API documentation
Assumptions
Analysts can access and analyze all users’ data
Admins have full system control
Viewers are restricted to their own data
SQLite is sufficient for development purposes
Tradeoffs
SQLite used instead of PostgreSQL for simplicity
No soft delete implemented
No rate limiting included
Basic filtering instead of advanced search
Future Improvements
Soft delete functionality
PostgreSQL integration
Rate limiting and caching
Unit and integration testing
Docker-based deployment
Author

Nayana Dev

Conclusion

This project demonstrates:

Strong understanding of backend architecture
Role-based access control implementation
Secure authentication mechanisms
Clean and scalable API design

It reflects a practical approach to building real-world backend systems.
