# AI-Based Visitor Management System

## 📌 Project Overview

The AI-Based Visitor Management System is a secure and intelligent visitor tracking application built using FastAPI, SQLite, OpenCV, and JWT Authentication.

This system allows organizations to manage visitor entry and exit digitally with features like:

* Visitor Registration
* Secure User Authentication
* Visitor Check-In / Check-Out
* Photo Upload & Storage
* Visitor Filtering & Tracking
* JWT-Based Login System
* File Handling using FastAPI
* Database Management using SQLAlchemy

The project is designed to simulate a real-world smart gate security and visitor management system.

---

# 🚀 Features

## 🔐 Authentication System

* User Signup
* User Login
* JWT Token Generation
* Password Hashing using bcrypt
* Logout Functionality
* Delete User API

---

## 👤 Visitor Management

* Create Visitor Entry
* Generate Unique Visitor ID
* Visitor Photo Upload
* Store Visitor Details in Database

---

## 🟢 Check-In System

* Upload Check-In Photo
* Store Check-In Time
* Save Check-In Images

---

## 🔴 Check-Out System

* Upload Check-Out Photo
* Store Check-Out Time
* Save Check-Out Images

---

## 🔍 Visitor Filtering APIs

Filter visitors using:

* Name
* Email
* Authority
* Visitor ID
* Check-In Date
* Time Range

---

# 🛠️ Technologies Used

| Technology | Purpose          |
| ---------- | ---------------- |
| Python     | Backend Language |
| FastAPI    | API Framework    |
| SQLite     | Database         |
| SQLAlchemy | ORM              |
| OpenCV     | Image Processing |
| JWT        | Authentication   |
| bcrypt     | Password Hashing |
| Pydantic   | Data Validation  |

---

# 📂 Project Structure

```bash
project/
│
├── main.py
├── users.db
├── visitor_photos/
├── checkin_photos/
├── checkout_photos/
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <your_repository_link>
```

---

## 2️⃣ Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy bcrypt python-jose python-multipart opencv-python
```

---

## 3️⃣ Run Server

```bash
uvicorn main:app --reload
```

---

# 📖 API Documentation

FastAPI automatically provides Swagger UI documentation.

Open in browser:

```bash
http://127.0.0.1:8000/docs
```

---

# 📌 API Endpoints

| Method | Endpoint          | Description         |
| ------ | ----------------- | ------------------- |
| POST   | /signup           | User Signup         |
| POST   | /login            | User Login          |
| POST   | /logout           | User Logout         |
| DELETE | /delete-user      | Delete User         |
| POST   | /create-visitor   | Create Visitor      |
| PUT    | /visitor/checkin  | Visitor Check-In    |
| PUT    | /visitor/checkout | Visitor Check-Out   |
| GET    | /visitors         | Get Visitor Records |

---

# 🔒 Security Features

* Password Hashing using bcrypt
* JWT Authentication
* Input Validation using Pydantic
* File Upload Handling
* Visitor Tracking

---

# 📸 Image Storage

Uploaded images are stored in:

* visitor_photos/
* checkin_photos/
* checkout_photos/

---

# 🔮 Future Improvements

* Face Recognition Verification
* AI-Based Visitor Detection
* Liveness Detection
* QR Code Entry System
* Email Notifications
* Admin Dashboard
* Frontend Integration
* Docker Deployment
* Role-Based Access Control

---

# 🎯 Learning Outcomes

This project helped in learning:

* Backend Development
* REST API Development
* Authentication Systems
* Database Management
* File Handling
* OpenCV Integration
* FastAPI Framework
* Real-Time Visitor Tracking

---

# 👩‍💻 Author

Khushi Agarwal

B.Tech Student | Python Developer | FastAPI & OpenCV Enthusiast

---

# ⭐ Conclusion

This project demonstrates the implementation of a secure and scalable Visitor Management System using modern backend technologies and image processing concepts.

It can be further enhanced into a production-level AI-powered security management solution.
