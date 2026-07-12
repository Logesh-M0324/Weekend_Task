import sqlite3

# Database Name

DATABASE_NAME = "Job_database.db"

# Get Database Connection Job_database.db

def get_connection():
    """
    Creates and returns a connection to the SQLite database.
    The row_factory allows accessing columns by their names.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# Create a Table Users, Jobs, Application, Saved_job in the Job_database.db

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

        profile_picture TEXT,

        company_name TEXT,

        company_location TEXT,

        company_website TEXT,

        company_description TEXT,

        company_logo TEXT
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


# Registers a new user in the database.

def register_user(name, email, password, role, company_name, company_website, company_location, company_description):
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
        role,
        company_name,
        company_website,
        company_location,
        company_description
    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        name,
        email,
        password,
        role,
        company_name,
        company_website,
        company_location,
        company_description
    ))

    conn.commit()

    conn.close()


    
# Get User By Email from the User table

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

# Get User by User_id from the User Table

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

# Inserts a new job posted by an employer.

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

# Retrieves all jobs posted by a specific employer.

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

# Retrieves a job using its unique ID.

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

# Updates the details of an existing job.

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


# Deletes a job from the database.

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


# Retrieves all available jobs ordered by newest first.

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

# Searches jobs by title, company name or location.

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

# Stores a candidate's job application.

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

# Saves a job for future reference.

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


# Retrieves all jobs saved by a candidate.

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

# Checks whether a candidate has already applied a specific job.

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

# Checks whether a candidate has already saved a specific job.

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


# Retrieves all jobs applied by a candidate.

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


# Returns the total number of jobs saved by a candidate.

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

# Returns the total number of jobs applied by a candidate.

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

# Removes a saved job from the candidate's saved jobs list.

def delete_saved_job(user_id, job_id):

    conn = get_connection()

    conn.execute(
        """
        DELETE FROM saved_jobs
        WHERE user_id = ?
        AND job_id = ?
        """,
        (
            user_id,
            job_id
        )
    )

    conn.commit()

    conn.close()

# Updates the candidate's profile information.

def update_profile(
    user_id,
    name,
    skills,
    experience,
    resume,
    profile_picture
):
    """
    Updates candidate's profile information.
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

# Retrieves all applicants for a particular job.

def get_job_applicants(job_id):

    """
    Returns all applicants for a particular job.
    """

    conn = get_connection()

    applicants = conn.execute("""
    SELECT

        applications.id,
        applications.applied_date,
        applications.status,

        users.name,
        users.email,
        users.skills,
        users.experience,
        users.resume

    FROM applications

    JOIN users

    ON applications.user_id = users.id

    WHERE applications.job_id = ?

    ORDER BY applications.applied_date DESC
    """,
    (job_id,)
    ).fetchall()

    conn.close()

    return applicants

# Updates the application status (Applied, Accepted or Rejected).

def update_application_status(application_id, status):

    conn = get_connection()

    conn.execute(
        """
        UPDATE applications

        SET status = ?

        WHERE id = ?
        """,
        (
            status,
            application_id
        )
    )

    conn.commit()

    conn.close()

# Updates the employer's company information.

def update_company_profile(
    user_id,
    company_name,
    company_location,
    company_website,
    company_description,
    company_logo
):
    """
    Updates employer company details.
    """

    conn = get_connection()

    conn.execute("""
    UPDATE users

    SET

        company_name = ?,
        company_location = ?,
        company_website = ?,
        company_description = ?,
        company_logo = ?

    WHERE id = ?
    """,
    (
        company_name,
        company_location,
        company_website,
        company_description,
        company_logo,
        user_id
    ))

    conn.commit()
    conn.close()

# Updates the employer's personal profile details.

def update_employer_profile(
    user_id,
    name,
    company_name,
    company_location,
    company_description,
    profile_picture
):
    """
    Updates employer profile information.
    """

    conn = get_connection()

    conn.execute("""
    UPDATE users

    SET
        name = ?,
        company_name = ?,
        company_location = ?,
        company_description = ?,
        profile_picture = ?

    WHERE id = ?
    """,
    (
        name,
        company_name,
        company_location,
        company_description,
        profile_picture,
        user_id
    ))

    conn.commit()

    conn.close()