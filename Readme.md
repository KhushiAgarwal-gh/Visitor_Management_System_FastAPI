# Visitor Management System API

A secure and scalable backend system built using **FastAPI** for managing users and visitors with authentication, visitor tracking, and advanced filtering capabilities.


## 📌 Overview

The Visitor Management System is a RESTful API that handles:

- User authentication (Signup/Login/Logout)
- Visitor registration with document details and photo upload
- Check-in and Check-out tracking
- Advanced visitor search and filtering (date & time-based)

This project demonstrates backend development using modern Python frameworks with database integration and secure authentication practices.

---

## 🚀 Features

### 👤 User Management
- User registration with validation
- Secure password hashing (bcrypt)
- JWT-based authentication
- Login using email or user ID
- User deletion and logout functionality

---

### 🧑‍💼 Visitor Management
- Visitor creation with form-data input
- File upload support (photo)
- Check-in and Check-out system
- Visitor status tracking

---

### 🔍 Filtering System
Supports advanced query filtering:

- Name
- Email
- Authority level (intern / employee / manager)
- Visitor ID
- Check-in date filtering
- Time range filtering

---

## 🛠 Tech Stack

- FastAPI
- SQLAlchemy (ORM)
- SQLite Database
- Pydantic (Data validation)
- bcrypt (Password hashing)
- python-jose (JWT Authentication)
- OpenCV (optional image processing)

---

## 📦 Installation

```bash
git clone https://github.com/your-username/visitor-management-system.git
cd visitor-management-system
pip install fastapi uvicorn sqlalchemy bcrypt python-jose opencv-python
▶️ Run the Application
uvicorn main:app --reload
📡 API Endpoints
🔐 Authentication
POST /signup
POST /login
POST /logout
DELETE /delete-user
🧑‍💼 Visitor Management
POST /create-visitor
PUT /visitor/checkin
PUT /visitor/checkout
GET /visitors
📊 Example API Usage
Signup
POST /signup
Content-Type: multipart/form-data

name: John Doe
email: john@gmail.com
password: StrongPass@123
Login
POST /login
Content-Type: multipart/form-data

email_or_user_id: john@gmail.com
password: StrongPass@123
Create Visitor
POST /create-visitor
Content-Type: multipart/form-data

name:
email:
phone_number:
address:
authority:
id_type:
id_number:
photo: (file)
Filter Visitors
GET /visitors?check_in_date=2026-06-05
GET /visitors?time_range=09:00:00-18:00:00
GET /visitors?email=john@gmail.com
🔐 Security Implementation
Password hashing using bcrypt
JWT token authentication
Role-based access control (intern, employee, manager)
Input validation using regex patterns
Safe database query handling with SQLAlchemy
📁 Project Structure
main.py
SQLite Database (users.db)
📈 Future Enhancements
Frontend dashboard (React / Angular)
Role-based admin panel
Email notification system
Face recognition check-in (OpenCV integration)
PostgreSQL migration for scalability
👨‍💻 Author

Khushi Agarwal
B.Tech Computer Science & Engineering

⭐ Repository Goal

This project demonstrates:

Backend API development
Authentication & authorization
Real-world visitor tracking system
Clean and scalable API design

---

Agar chaho to main next step me tumhare liye:
- 🔥 :contentReference[oaicite:0]{index=0}
- 🔥 :contentReference[oaicite:1]{index=1}
- 🔥 :contentReference[oaicite:2]{index=2}
- 🔥 :contentReference[oaicite:3]{index=3}

sab bana dunga 👍
pura ek sath de jo m copy paste kr pau sidha

Here is your complete professional README.md in one single copy-paste block 👇

# Visitor Management System API

A secure and scalable backend system built using **FastAPI** for managing users and visitors with authentication, visitor tracking, and advanced filtering capabilities.

---

## 📌 Overview

The Visitor Management System is a RESTful API that handles:

- User authentication (Signup/Login/Logout)
- Visitor registration with details and photo upload
- Check-in and Check-out tracking
- Advanced filtering based on date and time

This project demonstrates backend development using FastAPI, SQLAlchemy, and secure authentication practices.

---

## 🚀 Features

### 👤 User Management
- User Signup with validation
- Secure password hashing using bcrypt
- JWT authentication system
- Login using email or user ID
- Logout and user deletion

### 🧑‍💼 Visitor Management
- Visitor registration with form data
- Photo upload support
- Check-in system
- Check-out system
- Visitor tracking

### 🔍 Filtering System
Supports advanced filtering:
- Name
- Email
- Authority (intern / employee / manager)
- Visitor ID
- Check-in date
- Time range (HH:MM:SS - HH:MM:SS)

---

## 🛠 Tech Stack

- FastAPI
- SQLAlchemy ORM
- SQLite Database
- Pydantic Validation
- bcrypt (Password Hashing)
- python-jose (JWT Authentication)
- OpenCV (optional image handling)

---

## 📦 Installation

git clone https://github.com/your-username/visitor-management-system.git
cd visitor-management-system
pip install fastapi uvicorn sqlalchemy bcrypt python-jose opencv-python
▶️ Run Project
uvicorn main:app --reload
📡 API Endpoints
Authentication
POST /signup
POST /login
POST /logout
DELETE /delete-user
Visitor Management
POST /create-visitor
PUT /visitor/checkin
PUT /visitor/checkout
GET /visitors
📊 Example Requests
Signup
POST /signup
Content-Type: multipart/form-data

name: John Doe
email: john@gmail.com
password: StrongPass@123
Login
POST /login
Content-Type: multipart/form-data

email_or_user_id: john@gmail.com
password: StrongPass@123
Create Visitor
POST /create-visitor
Content-Type: multipart/form-data

name:
email:
phone_number:
address:
authority:
id_type:
id_number:
photo: file
Filter Visitors
GET /visitors?check_in_date=2026-06-05
GET /visitors?time_range=09:00:00-18:00:00
GET /visitors?email=john@gmail.com
🔐 Security Features
Password hashing using bcrypt
JWT token authentication
Input validation using regex
Role-based access (intern, employee, manager)
Secure database queries using SQLAlchemy
📁 Project Structure
main.py
users.db
📈 Future Improvements
Frontend dashboard (React)
Admin panel with roles
Email notifications
Face recognition check-in system
PostgreSQL migration for scalability
👨‍💻 Author

Khushi Agarwal
B.Tech Computer Science Student

⭐ Project Highlights

This project demonstrates:

REST API development
Authentication & Authorization
Real-world visitor tracking system
Clean backend architecture