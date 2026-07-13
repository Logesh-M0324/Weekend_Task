from flask import Flask, render_template, request, redirect, flash, url_for, session

from werkzeug.security import generate_password_hash, check_password_hash

from functools import wraps

import os

from werkzeug.utils import secure_filename

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
    update_profile
)

from datetime import datetime

app = Flask(__name__)

app.config["RESUME_UPLOAD_FOLDER"] = "static/uploads/resumes"

app.config["PROFILE_UPLOAD_FOLDER"] = "static/uploads/profile_pics"

app.secret_key = "my_secret_key"

ALLOWED_RESUME_EXTENSIONS = {
    "pdf",
    "doc",
    "docx"
}

ALLOWED_IMAGE_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg"
}


create_tables()

def login_required(role=None):
    """
    Restricts access to authenticated users.
    Optionally restricts access based on the user's role.
    """

    def decorator(view_function):

        @wraps(view_function)
        def wrapper(*args, **kwargs):

            if "user_id" not in session:
                flash("Please login to continue.", "warning")
                return redirect(url_for("login"))

            if role and session.get("role") != role:
                flash("You are not authorized to access this page.", "danger")
                return redirect(url_for("home"))

            return view_function(*args, **kwargs)

        return wrapper

    return decorator


def allowed_file(filename, allowed_extensions):

    return (
        "." in filename
        and
        filename.rsplit(".", 1)[1].lower()
        in allowed_extensions
    )


# Home route

@app.route("/")
def home():

    latest_jobs = get_all_jobs()[:6]

    return render_template(
        "index.html",
        latest_jobs=latest_jobs
    )


# REGISTRATION route

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"].strip()
        email = request.form["email"].strip().lower()
        password = request.form["password"]
        role = request.form["role"]

        # Server-side validation
        if not name or not email or not password or not role:
            flash("All fields are required.", "danger")
            return redirect(url_for("register"))
        
        # Check if email already exists
        user = get_user_by_email(email)

        if user:
            flash("Email already registered.", "danger")
            return redirect(url_for("register"))

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Save the user
        register_user(
            name,
            email,
            hashed_password,
            role
        )

        flash("Registration successful. Please login.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


# Login route

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

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

        # Create user session
        session["user_id"] = user["id"]
        session["user_name"] = user["name"]
        session["role"] = user["role"]

        flash(f"Welcome, {user['name']}!", "success")

        # Redirect based on role
        if user["role"] == "Employer":
            return redirect(url_for("employer_dashboard"))

        return redirect(url_for("candidate_dashboard"))

    return render_template("login.html")



# Candidate Dashboard route

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


# Employer Dashboard route

@app.route("/employer_dashboard")
@login_required(role="Employer")
def employer_dashboard():

    jobs = get_jobs_by_employer(session["user_id"])

    return render_template(
        "employer_dashboard.html",
        jobs=jobs,
        total_jobs=len(jobs)
    )


# Post employer job route

@app.route("/post_job", methods=["GET", "POST"])
@login_required(role="Employer")
def post_job():

    if request.method == "POST":

        company_name = request.form["company_name"].strip()
        job_title = request.form["job_title"].strip()
        location = request.form["location"].strip()
        experience = request.form["experience"].strip()
        salary = request.form["salary"].strip()
        skills = request.form["skills"].strip()
        description = request.form["description"].strip()

        # Server-side validation
        if not all([
            company_name,
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

    return render_template("post_job.html")

# edit employer job route

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

        company_name = request.form["company_name"].strip()
        job_title = request.form["job_title"].strip()
        location = request.form["location"].strip()
        experience = request.form["experience"].strip()
        salary = request.form["salary"].strip()
        skills = request.form["skills"].strip()
        description = request.form["description"].strip()

        # Server-side validation
        if not all([
            company_name,
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


# Delete employer job route

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


# CANDIDATE JOBS

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


#Candidate job details route

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



# Apply for a job route

@app.route("/apply_job/<int:job_id>")
@login_required(role="Candidate")
def apply_job_route(job_id):

    job = get_job_by_id(job_id)

    if not job:
        flash("Job not found.", "danger")
        return redirect(url_for("jobs"))

    # Prevent duplicate applications
    if has_applied(session["user_id"], job_id):
        flash("You have already applied for this job.", "warning")
        return redirect(url_for("job_details", job_id=job_id))

    # Get candidate details
    user = get_user_by_id(session["user_id"])

    # Resume not uploaded
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


# Save a job route

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



@app.route("/profile", methods=["GET", "POST"])
@login_required(role="Candidate")
def profile():

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


#Logout route
@app.route("/logout")
@login_required()
def logout():

    session.clear()

    flash("You have logged out successfully.", "success")

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)