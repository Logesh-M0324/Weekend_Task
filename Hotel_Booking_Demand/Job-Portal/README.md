# Job Portal

A full-stack **Job Portal Web Application** built using **Flask**, **SQLite**, **Bootstrap 5**, and **Pipenv**. The application provides separate portals for **Candidates** and **Employers**, enabling job posting, job applications, profile management, resume uploads, and applicant tracking.

---

# Features

## Candidate

- Register and Login
- Search and browse available jobs
- View complete job details
- Apply for jobs
- Save jobs for later
- Remove saved jobs
- Upload Resume (PDF, DOC, DOCX)
- Upload Profile Picture
- Update Profile
- View application status
- Dashboard showing:
  - Applied Jobs
  - Saved Jobs
  - Profile Completion

---

## Employer

- Register and Login
- Company Profile Management
- Upload Company Logo
- Personal Employer Profile
- Post New Jobs
- Edit Existing Jobs
- Delete Jobs
- View Applicants
- View Candidate Resume inside the website
- Accept or Reject Applications

---

## Security Features

- Password Hashing
- Session Management
- Role-Based Authorization
- Protected Routes
- File Upload Validation
- Secure File Names using `secure_filename()`

---

# Tech Stack

| Technology | Purpose                                     |
|------------|---------------------------------------------|
| Python     | Programming Language                        |
| Flask      | Web Framework                               |
| SQLite     | Database                                    |
| Bootstrap 5| Frontend UI                                 |
| HTML5      | Templates                                   |
| CSS3       | Styling                                     |
| Jinja2     | Template Engine                             |
| Werkzeug   | Password Hashing & File Uploads             |
| Pipenv     | Virtual Environment & Dependency Management |

---

# Project Structure

```
Job-Portal/
│
├── app.py
├── database.py
├── Job_database.db
├── Pipfile
├── Pipfile.lock
├── README.md
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── jobs.html
│   ├── job_details.html
│   ├── candidate_dashboard.html
│   ├── employer_dashboard.html
│   ├── profile.html
│   ├── employer_profile.html
│   ├── company_profile.html
│   ├── post_job.html
│   ├── edit_job.html
│   ├── view_applicants.html
│   └── view_resume.html
│
├── static/
│   └── uploads/
│       ├── resumes/
│       ├── profile_pics/
│       └── company_logos/
│
└── __pycache__/
```

---

# Installation

## Clone the Repository

```bash
git clone <repository-url>
cd Job-Portal
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

## Activate the Virtual Environment

```bash
pipenv shell
```

---

## Run the Application

```bash
python app.py
```

---

## Open the Application

```
http://127.0.0.1:5000
```

---

# Database

The application automatically creates the required tables when it starts.

### Users

Stores:

- Candidate Details
- Employer Details
- Company Information

### Jobs

Stores:

- Employer Jobs
- Salary
- Skills
- Description
- Posted Date

### Applications

Stores:

- Candidate Applications
- Resume
- Applied Date
- Application Status

### Saved Jobs

Stores jobs bookmarked by candidates.

---

# File Uploads

### Resume

Supported Formats

- PDF
- DOC
- DOCX

Location

```
static/uploads/resumes/
```

---

### Profile Picture

Supported Formats

- JPG
- JPEG
- PNG

Location

```
static/uploads/profile_pics/
```

---

### Company Logo

Supported Formats

- JPG
- JPEG
- PNG

Location

```
static/uploads/company_logos/
```

---

# User Roles

## Candidate

Can

- Search Jobs
- Apply Jobs
- Save Jobs
- Update Profile
- Upload Resume
- Upload Profile Picture

---

## Employer

Can

- Create Company Profile
- Update Company Profile
- Post Jobs
- Edit Jobs
- Delete Jobs
- View Applicants
- View Resume
- Accept Candidate
- Reject Candidate

---

# Application Workflow

## Candidate

```
Register
      ↓
Login
      ↓
Browse Jobs
      ↓
View Job Details
      ↓
Upload Resume
      ↓
Apply Job
      ↓
Track Application Status
```

---

## Employer

```
Register
      ↓
Login
      ↓
Create Company Profile
      ↓
Post Job
      ↓
Receive Applications
      ↓
View Resume
      ↓
Accept / Reject Candidate
```

---

# Security

The application implements:

- Password Hashing
- Authentication
- Authorization
- Protected Routes
- Session Handling
- File Validation
- Secure File Uploads

---

# Future Improvements

- Email Notifications
- Forgot Password
- OTP Verification
- Interview Scheduling
- Advanced Search Filters
- Pagination
- Admin Panel
- REST API
- Deployment on Render or AWS

---

# Learning Outcomes

This project demonstrates:

- Flask Routing
- SQLite CRUD Operations
- Authentication & Authorization
- Session Management
- File Upload Handling
- Bootstrap UI Development
- Jinja2 Templates
- Role-Based Access Control
- Database Relationships
- Python Backend Development

---

# Author

**Logesh**

Developed as a full-stack Flask project to demonstrate backend development, authentication, file handling, CRUD operations, and responsive web application development.

---

# License

This project is developed for educational and learning purposes.