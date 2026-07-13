import sqlite3

DATABASE_NAME = "Job_database.db"


def get_connection():
    """
    Creates and returns a connection to the SQLite database.
    The row_factory allows accessing columns by their names.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    """
    Creates the Users table if it does not already exist.
    """
    conn = get_connection()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS users
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        email TEXT NOT NULL UNIQUE,

        password TEXT NOT NULL,

        role TEXT NOT NULL,

        skills TEXT,

        experience TEXT,

        resume TEXT,

        profile_picture TEXT
        )
    """)
    
        # Jobs Table
    conn.execute("""
    CREATE TABLE IF NOT EXISTS jobs
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        employer_id INTEGER NOT NULL,

        company_name TEXT NOT NULL,

        job_title TEXT NOT NULL,

        location TEXT NOT NULL,

        experience TEXT NOT NULL,

        salary TEXT NOT NULL,

        skills TEXT NOT NULL,

        description TEXT NOT NULL,

        posted_date TEXT NOT NULL,

        FOREIGN KEY (employer_id)
        REFERENCES users(id)
    )
    """)

    # Applications Table
    conn.execute("""
    CREATE TABLE IF NOT EXISTS applications
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER NOT NULL,

        job_id INTEGER NOT NULL,

        resume_file TEXT NOT NULL,

        applied_date TEXT NOT NULL,

        status TEXT NOT NULL DEFAULT 'Applied',

        FOREIGN KEY (user_id)
        REFERENCES users(id),

        FOREIGN KEY (job_id)
        REFERENCES jobs(id)
    )
    """)

    # Saved Jobs Table
    conn.execute("""
    CREATE TABLE IF NOT EXISTS saved_jobs
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER NOT NULL,

        job_id INTEGER NOT NULL,

        FOREIGN KEY (user_id)
        REFERENCES users(id),

        FOREIGN KEY (job_id)
        REFERENCES jobs(id),

        UNIQUE(user_id, job_id)
    )
    """)

    conn.commit()
    conn.close()


# -------------------
# Users
# -------------------

def register_user(name, email, password, role):
    """
    Inserts a new user into the Users table.
    """
    conn = get_connection()

    conn.execute("""
    INSERT INTO users
    (
        name,
        email,
        password,
        role
    )
    VALUES (?, ?, ?, ?)
    """, (name, email, password, role))

    conn.commit()
    conn.close()


def get_user_by_email(email):
    """
    Returns a user record using the email address.
    Used during login and duplicate email checking.
    """
    conn = get_connection()

    user = conn.execute("""
    SELECT *
    FROM users
    WHERE email = ?
    """, (email,)).fetchone()

    conn.close()

    return user

def get_user_by_id(user_id):
    """
    Returns a user using their ID.
    """

    conn = get_connection()

    user = conn.execute("""
    SELECT *
    FROM users
    WHERE id = ?
    """,
    (user_id,)
    ).fetchone()

    conn.close()

    return user

# -------------------
# Employer
# -------------------

def add_job(
    employer_id,
    company_name,
    job_title,
    location,
    experience,
    salary,
    skills,
    description,
    posted_date
):
    """
    Inserts a new job into the jobs table.
    """

    conn = get_connection()

    conn.execute("""
    INSERT INTO jobs
    (
        employer_id,
        company_name,
        job_title,
        location,
        experience,
        salary,
        skills,
        description,
        posted_date
    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        employer_id,
        company_name,
        job_title,
        location,
        experience,
        salary,
        skills,
        description,
        posted_date
    ))

    conn.commit()
    conn.close()


def get_jobs_by_employer(employer_id):
    """
    Returns all jobs posted by a specific employer.
    """

    conn = get_connection()

    jobs = conn.execute("""
    SELECT *
    FROM jobs
    WHERE employer_id = ?
    ORDER BY id DESC
    """,
    (employer_id,)
    ).fetchall()

    conn.close()

    return jobs

def get_job_by_id(job_id):
    """
    Returns a single job using its ID.
    """

    conn = get_connection()

    job = conn.execute("""
    SELECT *
    FROM jobs
    WHERE id = ?
    """,
    (job_id,)
    ).fetchone()

    conn.close()

    return job

def update_job(
    company_name,
    job_title,
    location,
    experience,
    salary,
    skills,
    description,
    job_id
):
    """
    Updates an existing job.
    """

    conn = get_connection()

    conn.execute("""
    UPDATE jobs

    SET

        company_name = ?,
        job_title = ?,
        location = ?,
        experience = ?,
        salary = ?,
        skills = ?,
        description = ?

    WHERE id = ?
    """,
    (
        company_name,
        job_title,
        location,
        experience,
        salary,
        skills,
        description,
        job_id
    ))

    conn.commit()
    conn.close()


def delete_job(job_id):
    """
    Deletes a job using its ID.
    """

    conn = get_connection()

    conn.execute("""
    DELETE
    FROM jobs
    WHERE id = ?
    """,
    (job_id,)
    )

    conn.commit()
    conn.close()


# -------------------
# Candidate
# -------------------

def get_all_jobs():
    """
    Returns all available jobs ordered by newest first.
    """

    conn = get_connection()

    jobs = conn.execute("""
    SELECT *
    FROM jobs
    ORDER BY id DESC
    """).fetchall()

    conn.close()

    return jobs

def search_jobs(search_text):
    """
    Searches jobs by title, company name or location.
    """

    conn = get_connection()

    jobs = conn.execute("""
    SELECT *
    FROM jobs

    WHERE

        job_title LIKE ?
        OR company_name LIKE ?
        OR location LIKE ?

    ORDER BY id DESC
    """,
    (
        f"%{search_text}%",
        f"%{search_text}%",
        f"%{search_text}%"
    )
    ).fetchall()

    conn.close()

    return jobs

def apply_job(
    user_id,
    job_id,
    resume_file,
    applied_date
):
    """
    Stores a new job application.
    """

    conn = get_connection()

    conn.execute("""
    INSERT INTO applications
    (
        user_id,
        job_id,
        resume_file,
        applied_date
    )

    VALUES (?, ?, ?, ?)
    """,
    (
        user_id,
        job_id,
        resume_file,
        applied_date
    ))

    conn.commit()

    conn.close()


def save_job(
    user_id,
    job_id
):
    """
    Saves a job for a candidate.
    """

    conn = get_connection()

    conn.execute("""
    INSERT INTO saved_jobs
    (
        user_id,
        job_id
    )

    VALUES (?, ?)
    """,
    (
        user_id,
        job_id
    ))

    conn.commit()

    conn.close()


def get_saved_jobs(user_id):
    """
    Returns all saved jobs for a candidate.
    """

    conn = get_connection()

    jobs = conn.execute("""
    SELECT jobs.*

    FROM saved_jobs

    JOIN jobs

    ON jobs.id = saved_jobs.job_id

    WHERE saved_jobs.user_id = ?

    ORDER BY saved_jobs.id DESC
    """,
    (user_id,)
    ).fetchall()

    conn.close()

    return jobs

def has_applied(
    user_id,
    job_id
):
    """
    Checks whether the candidate has already applied for a job.
    """

    conn = get_connection()

    application = conn.execute("""
    SELECT *

    FROM applications

    WHERE user_id = ?

    AND job_id = ?
    """,
    (
        user_id,
        job_id
    )
    ).fetchone()

    conn.close()

    return application

def has_saved_job(
    user_id,
    job_id
):
    """
    Checks whether a candidate has already saved a job.
    """

    conn = get_connection()

    saved_job = conn.execute("""
    SELECT *

    FROM saved_jobs

    WHERE user_id = ?

    AND job_id = ?
    """,
    (
        user_id,
        job_id
    )
    ).fetchone()

    conn.close()

    return saved_job


def get_applied_jobs(user_id):
    """
    Returns all jobs the candidate has applied for.
    """

    conn = get_connection()

    jobs = conn.execute("""
    SELECT
        jobs.*,
        applications.applied_date,
        applications.status

    FROM applications

    JOIN jobs

    ON applications.job_id = jobs.id

    WHERE applications.user_id = ?

    ORDER BY applications.id DESC
    """, (user_id,)).fetchall()

    conn.close()

    return jobs


def count_saved_jobs(user_id):
    """
    Returns the number of saved jobs.
    """

    conn = get_connection()

    count = conn.execute("""
    SELECT COUNT(*) AS total
    FROM saved_jobs
    WHERE user_id = ?
    """, (user_id,)).fetchone()

    conn.close()

    return count["total"]


def count_applied_jobs(user_id):
    """
    Returns the number of applied jobs.
    """

    conn = get_connection()

    count = conn.execute("""
    SELECT COUNT(*) AS total
    FROM applications
    WHERE user_id = ?
    """, (user_id,)).fetchone()

    conn.close()

    return count["total"]



def update_profile(
    user_id,
    name,
    skills,
    experience,
    resume,
    profile_picture
):
    """
    Updates a candidate's profile information.
    """

    conn = get_connection()

    conn.execute("""
    UPDATE users

    SET
        name = ?,
        skills = ?,
        experience = ?,
        resume = ?,
        profile_picture = ?

    WHERE id = ?
    """,
    (
        name,
        skills,
        experience,
        resume,
        profile_picture,
        user_id
    ))

    conn.commit()

    conn.close()