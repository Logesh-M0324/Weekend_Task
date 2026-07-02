# Flask modules for routing, templates, sessions and request handling
from flask import Flask, render_template, request, redirect, flash, url_for, session

# Password hashing utilities
from werkzeug.security import generate_password_hash, check_password_hash

# Used to create custom decorators
from functools import wraps

# File and directory operations
import os

# Secures uploaded filenames
from werkzeug.utils import secure_filename

# Database helper functions
from database import (
    create_tables,
    register_user,
    get_user_by_email,
    get_user_by_id,
    get_jobs_by_employer,
    add_job, get_job_by_id,
    update_job, delete_job,
    get_all_jobs,
    search_jobs,
    apply_job,
    save_job,
    get_saved_jobs,
    has_applied,
    has_saved_job,
    get_applied_jobs,
    count_saved_jobs,
    count_applied_jobs,
    delete_saved_job,
    get_job_applicants,
    update_profile,
    update_application_status,
    update_company_profile,
    update_employer_profile
)

# Used for storing job posted and application dates
from datetime import datetime

# Create the Flask application
app = Flask(__name__)

# Upload folder for candidate resumes
app.config["RESUME_UPLOAD_FOLDER"] = "static/uploads/resumes"

# Upload folder for user profile pictures
app.config["PROFILE_UPLOAD_FOLDER"] = "static/uploads/profile_pics"

# Upload folder for company logos
app.config["COMPANY_LOGO_UPLOAD_FOLDER"] = "static/uploads/company_logos"

# Secret key used for session management
app.secret_key = "my_secret_key"

# Allowed file formats for resume uploads
ALLOWED_RESUME_EXTENSIONS = {
    "pdf",
    "doc",
    "docx"
}

# Allowed image formats for profile pictures and company logos
ALLOWED_IMAGE_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg"
}

# Create all required database tables (runs only if tables do not exist)
create_tables()


# Custom decorator to restrict access to authenticated users.
# It can also restrict access based on the user's role.
def login_required(role=None):
    """
    Restricts access to authenticated users.
    Optionally restricts access based on the user's role.
    """

    def decorator(view_function):
        
        @wraps(view_function)
        def wrapper(*args, **kwargs):

            # Redirect unauthenticated users to the login page.
            if "user_id" not in session:
                flash("Please login to continue.", "warning")
                return redirect(url_for("login"))

            # Prevent users from accessing pages that belong to another role.
            if role and session.get("role") != role:
                flash("You are not authorized to access this page.", "danger")
                return redirect(url_for("home"))

            # Allow the requested view to execute.
            return view_function(*args, **kwargs)

        return wrapper

    return decorator

# Checks whether the uploaded file has a valid extension.
def allowed_file(filename, allowed_extensions):

    return (
        "." in filename
        and
        filename.rsplit(".", 1)[1].lower()
        in allowed_extensions
    )


# Displays the home page with the latest job postings.

@app.route("/")
def home():

    latest_jobs = get_all_jobs()[:6]

    return render_template(
        "index.html",
        latest_jobs=latest_jobs
    )


# Handles user registration for both Candidates and Employers.

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        # Retrieve user details from the registration form.
        name = request.form["name"].strip()
        email = request.form["email"].strip().lower()
        password = request.form["password"]
        role = request.form["role"]

        # Handles user registration for both Candidates and Employers.
        company_name = request.form.get("company_name", "").strip()
        company_website = request.form.get("company_website", "").strip()
        company_location = request.form.get("company_location", "").strip()
        company_description = request.form.get("company_description", "").strip()

        # Validate mandatory fields.
        if not name or not email or not password or not role:

            flash(
                "All fields are required.",
                "danger"
            )

            return redirect(url_for("register"))

        # Additional validation for employer registration.
        if role == "Employer":

            if (
                not company_name
                or
                not company_location
            ):

                flash(
                    "Company Name and Company Location are required for Employers.",
                    "danger"
                )

                return redirect(url_for("register"))

        else:

            company_name = None
            company_website = None
            company_location = None
            company_description = None

        # Ensure the email address is unique.
        user = get_user_by_email(email)

        if user:

            flash(
                "Email already registered.",
                "danger"
            )

            return redirect(url_for("register"))

        # Encrypt the password before storing it.
        hashed_password = generate_password_hash(password)

        # Store the new user in the database.
        register_user(
            name,
            email,
            hashed_password,
            role,
            company_name,
            company_website,
            company_location,
            company_description
        )

        flash(
            "Registration successful. Please login.",
            "success"
        )

        return redirect(url_for("login"))

    return render_template("register.html")

# Authenticates the user and creates a login session.

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        # Get the email and password from user form

        email = request.form["email"].strip().lower()
        password = request.form["password"]

        if not email or not password:
            flash("All fields are required.", "danger")
            return redirect(url_for("login"))

        user = get_user_by_email(email)

        if not user:
            flash("Invalid email or password.", "danger")
            return redirect(url_for("login"))

        if not check_password_hash(user["password"], password):
            flash("Invalid email or password.", "danger")
            return redirect(url_for("login"))

        # Store user information in the session after successful login.

        session["user_id"] = user["id"]
        session["user_name"] = user["name"]
        session["role"] = user["role"]

        flash(f"Welcome, {user['name']}!", "success")

        # Redirect users based on their role.

        if user["role"] == "Employer":
            return redirect(url_for("employer_dashboard"))

        return redirect(url_for("candidate_dashboard"))

    return render_template("login.html")


# Displays candidate statistics, applications and saved jobs.

@app.route("/candidate_dashboard")
@login_required(role="Candidate")
def candidate_dashboard():

    applied_jobs = get_applied_jobs(session["user_id"])

    saved_jobs = get_saved_jobs(session["user_id"])

    applied_count = count_applied_jobs(session["user_id"])

    saved_count = count_saved_jobs(session["user_id"])

    user = get_user_by_id(session["user_id"])

    return render_template(
        "candidate_dashboard.html",
        applied_jobs=applied_jobs,
        saved_jobs=saved_jobs,
        applied_count=applied_count,
        saved_count=saved_count,
        user=user
    )


# Displays all jobs posted by the logged-in employer.

@app.route("/employer_dashboard")
@login_required(role="Employer")
def employer_dashboard():

    jobs = get_jobs_by_employer(session["user_id"])

    return render_template(
        "employer_dashboard.html",
        jobs=jobs,
        total_jobs=len(jobs)
    )


# Allows an employer to create a new job posting.

@app.route("/post_job", methods=["GET", "POST"])
@login_required(role="Employer")
def post_job():

    # Get the employer details using the current login session

    employer = get_user_by_id(session["user_id"])

    if request.method == "POST":

        # Automatically use the employer's registered company name.
        company_name = employer["company_name"]

        job_title = request.form["job_title"].strip()
        location = request.form["location"].strip()
        experience = request.form["experience"].strip()
        salary = request.form["salary"].strip()
        skills = request.form["skills"].strip()
        description = request.form["description"].strip()

        # Server-side validation
        if not all([
            job_title,
            location,
            experience,
            salary,
            skills,
            description
        ]):
            flash("All fields are required.", "danger")
            return redirect(url_for("post_job"))

        # Automatically generate today's date
        posted_date = datetime.now().strftime("%d-%m-%Y")

        add_job(
            session["user_id"],
            company_name,
            job_title,
            location,
            experience,
            salary,
            skills,
            description,
            posted_date
        )

        flash("Job posted successfully.", "success")
        return redirect(url_for("employer_dashboard"))

    employer = get_user_by_id(session["user_id"])

    return render_template(
        "post_job.html",
        employer=employer
    )

# Allows employers to update one of their existing job postings.

@app.route("/edit_job/<int:job_id>", methods=["GET", "POST"])
@login_required(role="Employer")
def edit_job(job_id):

    # Fetch the selected job
    job = get_job_by_id(job_id)

    # Check whether the job exists
    if not job:
        flash("Job not found.", "danger")
        return redirect(url_for("employer_dashboard"))

    # Security Check
    # Ensure the logged-in employer owns this job
    if job["employer_id"] != session["user_id"]:
        flash("You are not authorized to edit this job.", "danger")
        return redirect(url_for("employer_dashboard"))

    if request.method == "POST":

        employer = get_user_by_id(session["user_id"])
        company_name = employer["company_name"]
        job_title = request.form["job_title"].strip()
        location = request.form["location"].strip()
        experience = request.form["experience"].strip()
        salary = request.form["salary"].strip()
        skills = request.form["skills"].strip()
        description = request.form["description"].strip()

        # Server-side validation
        if not all([
            job_title,
            location,
            experience,
            salary,
            skills,
            description
        ]):
            flash("All fields are required.", "danger")
            return redirect(url_for("edit_job", job_id=job_id))

        update_job(
            company_name,
            job_title,
            location,
            experience,
            salary,
            skills,
            description,
            job_id
        )

        flash("Job updated successfully.", "success")
        return redirect(url_for("employer_dashboard"))

    return render_template(
        "edit_job.html",
        job=job
    )


# Deletes a job posted by the logged-in employer.

@app.route("/delete_job/<int:job_id>")
@login_required(role="Employer")
def delete_job_route(job_id):

    # Get the job
    job = get_job_by_id(job_id)

    # Check if the job exists
    if not job:
        flash("Job not found.", "danger")
        return redirect(url_for("employer_dashboard"))

    # Security check
    if job["employer_id"] != session["user_id"]:
        flash("You are not authorized to delete this job.", "danger")
        return redirect(url_for("employer_dashboard"))

    # Delete the job
    delete_job(job_id)

    flash("Job deleted successfully.", "success")

    return redirect(url_for("employer_dashboard"))


# Displays all available jobs with optional search functionality.

@app.route("/jobs")
def jobs():

    search = request.args.get("search", "").strip()

    if search:
        jobs = search_jobs(search)
    else:
        jobs = get_all_jobs()

    return render_template(
        "jobs.html",
        jobs=jobs,
        search=search
    )


# Displays detailed information about a selected job.

@app.route("/job/<int:job_id>")
def job_details(job_id):

    job = get_job_by_id(job_id)

    if not job:
        flash("Job not found.", "danger")
        return redirect(url_for("jobs"))

    return render_template(
        "job_details.html",
        job=job
    )



# Displays detailed information about a selected job.

@app.route("/apply_job/<int:job_id>")
@login_required(role="Candidate")
def apply_job_route(job_id):

    job = get_job_by_id(job_id)

   # Prevent duplicate applications.

    if not job:
        flash("Job not found.", "danger")
        return redirect(url_for("jobs"))

    # Prevent duplicate applications
    if has_applied(session["user_id"], job_id):
        flash("You have already applied for this job.", "warning")
        return redirect(url_for("job_details", job_id=job_id))

    # Get candidate details
    user = get_user_by_id(session["user_id"])

    # Ensure the candidate has uploaded a resume before applying.
    if not user["resume"]:
        flash(
            "Please upload your resume in your profile before applying.",
            "warning"
        )
        return redirect(url_for("job_details", job_id=job_id))

    applied_date = datetime.now().strftime("%d-%m-%Y")

    apply_job(
        session["user_id"],
        job_id,
        user["resume"],
        applied_date
    )

    flash("Application submitted successfully.", "success")

    return redirect(url_for("job_details", job_id=job_id))


# Saves a job to the candidate's saved jobs list.

@app.route("/save_job/<int:job_id>")
@login_required(role="Candidate")
def save_job_route(job_id):

    # Check whether the job exists
    job = get_job_by_id(job_id)

    if not job:
        flash("Job not found.", "danger")
        return redirect(url_for("jobs"))

    # Prevent duplicate saved jobs
    if has_saved_job(session["user_id"], job_id):
        flash("Job already saved.", "warning")
        return redirect(url_for("job_details", job_id=job_id))

    # Save the job
    save_job(
        session["user_id"],
        job_id
    )

    flash("Job saved successfully.", "success")

    return redirect(url_for("job_details", job_id=job_id))

# Allows candidates to update their personal profile and resume.

@app.route("/profile", methods=["GET", "POST"])
@login_required(role="Candidate")
def profile():

    # Preserve existing uploaded files unless new ones are uploaded.

    user = get_user_by_id(session["user_id"])

    if request.method == "POST":

        name = request.form["name"].strip()
        skills = request.form["skills"].strip()
        experience = request.form["experience"].strip()

        # Keep existing filenames
        resume = user["resume"]
        profile_picture = user["profile_picture"]

        # Resume Upload
        resume_file = request.files.get("resume")

        if resume_file and resume_file.filename:

            if not allowed_file(
                resume_file.filename,
                ALLOWED_RESUME_EXTENSIONS
            ):

                flash(
                    "Only PDF, DOC and DOCX files are allowed.",
                    "danger"
                )

                return redirect(url_for("profile"))

            filename = secure_filename(resume_file.filename)

            resume_file.save(
                os.path.join(
                    app.config["RESUME_UPLOAD_FOLDER"],
                    filename
                )
            )

            resume = filename

        # Profile Picture Upload
        picture = request.files.get("profile_picture")

        if picture and picture.filename:


            if not allowed_file(
                picture.filename,
                ALLOWED_IMAGE_EXTENSIONS
            ):

                flash(
                    "Only JPG, JPEG and PNG images are allowed.",
                    "danger"
                )

                return redirect(url_for("profile"))

            filename = secure_filename(picture.filename)

            picture.save(
                os.path.join(
                    app.config["PROFILE_UPLOAD_FOLDER"],
                    filename
                )
            )

            profile_picture = filename

        update_profile(
            session["user_id"],
            name,
            skills,
            experience,
            resume,
            profile_picture
        )

        session["name"] = name

        flash(
            "Profile updated successfully.",
            "success"
        )

        return redirect(url_for("profile"))

    return render_template(
        "profile.html",
        user=user
    )

# Removes a saved job from the candidate's saved list.

@app.route("/remove_saved_job/<int:job_id>")
@login_required(role="Candidate")
def remove_saved_job( job_id):

    delete_saved_job(
        session["user_id"],
        job_id
    )

    flash(
        "Job removed from saved jobs.",
        "success"
    )

    return redirect(
        url_for("candidate_dashboard")
    )

# Allows employers to view all applicants for one of their jobs.

@app.route("/job/<int:job_id>/applicants")
@login_required(role="Employer")
def view_applicants(job_id):

    job = get_job_by_id(job_id)

    # Ensure the logged-in employer owns the selected job.

    if job["employer_id"] != session["user_id"]:

        flash(
            "You are not authorized to view applicants.",
            "danger"
        )

        return redirect(
            url_for("employer_dashboard")
        )

    applicants = get_job_applicants(job_id)

    return render_template(
        "view_applicants.html",
        applicants=applicants,
        job=job
    )

# Update the company profile in the database.

@app.route("/application/<int:application_id>/<status>")
@login_required(role="Employer")
def update_application(application_id, status):

    # Allow only valid application statuses.
    if status not in ["Accepted", "Rejected"]:

        flash(
            "Invalid status.",
            "danger"
        )

        return redirect(url_for("employer_dashboard"))

    update_application_status(
        application_id,
        status
    )

    flash(
        f"Application {status.lower()} successfully.",
        "success"
    )

    return redirect(request.referrer)

# Allows employers to manage their company profile information.

@app.route("/employer_profile", methods=["GET", "POST"])
@login_required(role="Employer")
def employer_profile():

    employer = get_user_by_id(session["user_id"])

    if request.method == "POST":

        company_name = request.form["company_name"].strip()

        company_location = request.form["company_location"].strip()

        company_website = request.form["company_website"].strip()

        company_description = request.form["company_description"].strip()

        logo = employer["company_logo"]


        # Validate and upload the company logo.

        if "company_logo" in request.files:

            file = request.files["company_logo"]

            if file.filename:

                if allowed_file(
                    file.filename,
                    ALLOWED_IMAGE_EXTENSIONS
                ):

                    filename = secure_filename(file.filename)

                    file.save(
                        os.path.join(
                            app.config["COMPANY_LOGO_UPLOAD_FOLDER"],
                            filename
                        )
                    )

                    logo = filename

                else:

                    flash(
                        "Invalid logo format.",
                        "danger"
                    )

                    return redirect(
                        url_for("employer_profile")
                    )

        # Update the company profile in the database.

        update_company_profile(
            session["user_id"],
            company_name,
            company_location,
            company_website,
            company_description,
            logo
        )

        flash(
            "Company profile updated successfully.",
            "success"
        )

        return redirect(
            url_for("employer_profile")
        )

    return render_template(
        "employer_profile.html",
        employer=employer
    )

# Employer View the Applicants Resume 

@app.route("/view_resume/<filename>")
@login_required(role="Employer")
def view_resume(filename):

    return render_template(
        "view_resume.html",
        filename=filename
    )

# Ends the user session and redirects to the login page.

@app.route("/logout")
@login_required()
def logout():

    session.clear()

    flash(
        "Logged out successfully.",
        "success"
    )

    return redirect(
        url_for("login")
    )

if __name__ == "__main__":
    app.run(debug=True)