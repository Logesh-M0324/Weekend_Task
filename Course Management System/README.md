# Online Course Management System

## Project Overview

The **Online Course Management System** is a web-based application developed using **Flask** and **SQLite**. It enables users to create an account, securely log in, browse available courses, enroll in courses, track their learning progress, and manage their personal profile through a responsive web interface.

The project demonstrates the core concepts of Flask web development, including routing, templates, session management, CRUD operations, database integration, and user authentication.

---

# Features

### User Management

* User Registration
* User Login
* User Logout
* Session-based Authentication
* Duplicate Email Validation

### Course Management

* View Available Courses
* Search Courses
* View Detailed Course Information

### Enrollment

* Enroll in Courses
* Prevent Duplicate Enrollment
* Display Enrolled Status

### Learning Dashboard

* View Enrolled Courses
* Update Course Progress
* Progress Bar Visualization
* Automatic Course Completion Status

### Profile Management

* View User Information
* Edit Profile
* View Learning Statistics

  * Total Enrollments
  * Completed Courses
  * In Progress Courses

---

# Technologies Used

* Python
* Flask
* HTML5
* Bootstrap 5
* Jinja2 Template Engine
* SQLite3
* Pipenv

---

# Flask Concepts Used

* Flask Routing
* Dynamic URL Routing
* Jinja2 Template Inheritance
* Session Management
* Flash Messages
* Form Handling
* CRUD Operations
* SQLite Database Integration
* SQL JOIN Operations
* User Authentication

---

# Project Structure

```
online-course-management/
│
├── app.py
├── database.py
├── course.db
├── Pipfile
├── Pipfile.lock
├── README.md
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── courses.html
│   ├── course_detail.html
│   ├── my_courses.html
│   ├── profile.html
│   └── edit_profile.html
│
└── static/
```

---

# Database Design

## Users Table

| Column   | Type    | Description   |
| -------- | ------- | ------------- |
| id       | INTEGER | Primary Key   |
| name     | TEXT    | User Name     |
| email    | TEXT    | User Email    |
| password | TEXT    | User Password |

---

## Courses Table

| Column      | Type    | Description        |
| ----------- | ------- | ------------------ |
| id          | INTEGER | Primary Key        |
| course_name | TEXT    | Course Name        |
| category    | TEXT    | Course Category    |
| duration    | TEXT    | Course Duration    |
| description | TEXT    | Course Description |

---

## Enrollments Table

| Column          | Type    | Description                  |
| --------------- | ------- | ---------------------------- |
| id              | INTEGER | Primary Key                  |
| user_id         | INTEGER | Foreign Key (Users)          |
| course_id       | INTEGER | Foreign Key (Courses)        |
| progress        | INTEGER | Course Completion Percentage |
| enrollment_date | TEXT    | Enrollment Date              |

---

# Application Workflow

### 1. User Registration

* User enters name, email, and password.
* Email uniqueness is validated.
* User details are stored in the database.
* Success message is displayed.

---

### 2. User Login

* User enters email and password.
* Credentials are verified.
* Session is created for authenticated users.
* User is redirected to the home page.

---

### 3. Browse Courses

* Users can view all available courses.
* Search functionality filters courses by course name.
* Course details can be viewed individually.

---

### 4. Course Enrollment

* Logged-in users can enroll in available courses.
* Duplicate enrollments are prevented.
* Already enrolled courses display an "Enrolled" status.

---

### 5. Learning Progress

* Users can update their course progress.
* Bootstrap progress bars visually represent completion.
* Completed courses are automatically identified when progress reaches 100%.

---

### 6. Profile Management

Users can:

* View personal information
* Update profile details
* View learning statistics

---

# Responsive Design

The application uses **Bootstrap 5** to provide a responsive user interface.

Features include:

* Responsive navigation bar
* Mobile-friendly layouts
* Cards
* Forms
* Progress bars
* Alerts
* Icons
* Dashboard design

---

# Installation

## Clone the Project

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd online-course-management
```

---

## Install Pipenv

```bash
pip install pipenv
```

---

## Install Dependencies

```bash
pipenv install
```

---

## Activate Virtual Environment

```bash
pipenv shell
```

---

## Run the Application

```bash
python app.py
```

or

```bash
flask run
```

---

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# Future Improvements

* Password hashing
* Forgot Password functionality
* Admin Dashboard
* Add/Edit/Delete Courses
* Course Categories
* Upload Course Images
* Pagination
* Email Verification
* User Roles (Admin & Student)
* Certificate Generation
* Course Ratings and Reviews
* File Uploads
* Video Lessons
* REST API Integration

---

# Learning Outcomes

This project demonstrates practical experience with:

* Flask application development
* SQLite database design
* CRUD operations
* Session management
* Authentication
* SQL joins
* Form validation
* Bootstrap responsive UI
* Jinja2 template inheritance
* MVC-style project organization

---