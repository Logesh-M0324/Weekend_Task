# Import the Flask class to create the web application and import
# helper objects/functions required for rendering pages, handling requests,
# managing user sessions, redirects, and flash messages.

from flask import Flask, render_template, request, redirect, session, flash

# Import custom database functions used to create database tables
# and establish a connection with the SQLite database.

from database import create_tables, get_connection

# Create an instance of the Flask application.
# This object is the main entry point of the web application.

app = Flask(__name__)


# Set a secret key used by Flask to securely sign session cookies
# and enable features like session management and flash messages.

app.secret_key = "my_secret_key"

# Create the required database tables when the application starts.
# Existing tables are ignored if they are already present.

create_tables()



# Define the URL endpoint for the home page.
# Display the application's home page.
# This is the first page users see after opening the website.
# This function executes whenever the user visits '/'.

@app.route("/")
def home():
    return render_template("index.html")



# Handle new user registration.
# Displays the registration form for GET requests and stores a new user in the database for POST requests.
# This function executes whenever the user visits 'http://127.0.0.1:5000/register'.

@app.route("/register", methods=["GET", "POST"])
def register():

    # Execute the registration logic only after the user submits the registration form.
    # Skip this block when simply displaying the registration page.

    if request.method == "POST":

        # Retrieve the user's entered name, email, and password from the submitted HTML form.

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        # Get the Database Connection for course.db

        conn = get_connection()

        # Verify whether the entered email already exists in the users table.
        # This prevents multiple accounts from being created with the same email.

        is_existing = conn.execute(
            """
            SELECT *
            FROM users
            WHERE email = ?
            """,
            (email,)
        ).fetchone()

        if is_existing:

            conn.close()

            # Store a temporary success message that will be displayed after the data is alreay existed.

            flash("User Already Existed")

            # Return the generated response to the client's browser.
            # This marks the end of the current request.
            return redirect("/register")

        # Store the newly registered user's details into the users table.

        conn.execute(
            """
            INSERT INTO users(name, email, password)
            VALUES (?, ?, ?)
            """,
            (name, email, password)
        )

        # Save the inserted user permanently in the SQLite database and close the database connection.

        conn.commit()
        conn.close()
        
        # Store a temporary success message that will be displayed after registration.

        flash("Registration Successful")

    # Render the register.html template and pass Python data
    # so it can be displayed using Jinja2 template syntax.

    return render_template("register.html")



# Authenticate an existing user.
# Validate the entered email and password and create a session after successful login.
# This function executes whenever the user visits 'http://127.0.0.1:5000/login'.

@app.route("/login", methods=["GET", "POST"])
def login():

    # Read the email and password entered by the user from the login form is the request method is POST.

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        # Get the Database connection course.db

        conn = get_connection()

        # Search for a user whose email and password match the entered credentials.

        user = conn.execute(
            """
            SELECT *
            FROM users
            WHERE email = ?
            AND password = ?
            """,
            (email, password)
        ).fetchone()

        conn.close()

        if user:
            
            # Store the logged-in user's ID and name in the session.
            # These values identify the user during future requests.

            session["user_id"] = user["id"]
            session["user_name"] = user["name"]

            # After the Login successfully it redirect to the Home page

            return redirect("/")

        # Display an error message if User is Not found as a flash if no matching user account is found.

        flash("User_Id or Password Not Found")

        # Again Redirect to the Login page

        return redirect("/login")
    
    # render the Login.html

    return render_template("login.html")



# Display all available courses.
# Also supports searching courses by their name.
# This function executes whenever the user visits 'http://127.0.0.1:5000/courses'.

@app.route("/courses")
def courses():

    # Retrieve the search keyword from the URL query string.
    # Use an empty string if no search keyword is provided.

    search = request.args.get("search", "")

    # Get the Database connection course.db

    conn = get_connection()

    # Retrieve courses whose names contain the entered search keyword.

    courses = conn.execute(
        """
        SELECT *
        FROM courses
        WHERE course_name LIKE ?
        """,
        (f"%{search}%",)
    ).fetchall()

    # Retrieve the IDs of all courses already enrolled by the logged-in user.
    # These IDs are used to disable the Enroll button.

    enrolled_courses = []

    if "user_id" in session:

        enrolled_courses = conn.execute(
            """
            SELECT course_id
            FROM enrollments
            WHERE user_id = ?
            """,
            (session["user_id"],)
        ).fetchall()

       # Convert database rows into a simple list containing only course IDs.

        enrolled_courses = [
            course["course_id"]
            for course in enrolled_courses
        ]
    
    # Close the Database connection 

    conn.close()

    # render the Course.html

    return render_template(
        "courses.html",
        courses=courses,
        search=search,
        enrolled_courses=enrolled_courses
    )



# Display detailed information for a single selected course.
# The course is identified using its unique ID.
# This function executes whenever the user visits 'http://127.0.0.1:5000/course/[1.....]'.

@app.route("/course/<int:id>")
def course_details(id):

    # Get the Database connection course.db

    conn = get_connection()

    # select the row which has the Id equals course_id

    course = conn.execute(
        """
        SELECT *
        FROM courses
        WHERE id = ?
        """,
        (id,)
    ).fetchone()

    # Close the connection

    conn.close()

    # render the course_detail.html

    return render_template(
        "course_detail.html",
        course=course
    )

# Enroll the currently logged-in user in the selected course.
# Prevent duplicate enrollments for the same course.
# This function executes whenever the user visits 'http://127.0.0.1:5000/enroll/{course_id}'.

@app.route("/enroll/<int:course_id>")
def enroll(course_id):

    if "user_id" not in session:
        return redirect("/login")

    user_id = session["user_id"]

    # Get the Database connection course.db

    conn = get_connection()

    existing = conn.execute(
        """
        SELECT *
        FROM enrollments
        WHERE user_id = ?
        AND course_id = ?
        """,
        (user_id, course_id)
    ).fetchone()

    if existing:

        # Close the connection 

        conn.close()

        # If the Course is Already Enrollec it shows like the following Flash message

        flash("Already enrolled in this course")

        # If the user Existed it re-directed to the 'http://127.0.0.1:5000/my-courses'.

        return redirect("/my-courses")

    # Insert the Datas in the enrollment Table in the course.db

    conn.execute(
        """
        INSERT INTO enrollments
        (
            user_id,
            course_id,
            progress,
            enrollment_date
        )
        VALUES (?, ?, ?, DATE('now'))
        """,
        (
            user_id,
            course_id,
            0
        )
    )

    # Save the inserted user permanently in the SQLite database and close the database connection.

    conn.commit()
    conn.close()

    # After the Successful Enrollment the function re-direct to the  'http://127.0.0.1:5000/enroll/my-courses'

    return redirect("/my-courses")



# Display all courses enrolled by the currently logged-in user.
# Also show each course's learning progress.
# This function executes whenever the user visits 'http://127.0.0.1:5000/my-courses'.

@app.route("/my-courses")
def my_courses():

    if "user_id" not in session:
        return redirect("/login")

    # Get the Database Connection course.db

    conn = get_connection()

    # Combine enrollment and course tables to display complete course information
    # along with the user's progress.

    courses = conn.execute(
        """
        SELECT
            enrollments.id,
            courses.course_name,
            courses.category,
            courses.duration,
            enrollments.progress
        FROM enrollments
        JOIN courses
        ON enrollments.course_id = courses.id
        WHERE enrollments.user_id = ?
        """,
        (session["user_id"],)
    ).fetchall()

    conn.close()

    return render_template(
        "my_courses.html",
        courses=courses
    )



# Update the completion percentage of a selected enrolled course.
# The new progress value is submitted from the dashboard form.
# This function executes whenever the user visits 'http://127.0.0.1:5000/update-progress/<int:enrollment_id>'.

@app.route("/update-progress/<int:enrollment_id>",
           methods=["POST"])
def update_progress(enrollment_id):

    if "user_id" not in session:
        return redirect("/login")
    
    # Read the newly selected progress percentage from the submitted form.

    progress = int(request.form["progress"])

    # Get the Database Connection course.db

    conn = get_connection()
    
    # Update the Progress using the id in the enrollment table

    conn.execute(
        """
        UPDATE enrollments
        SET progress = ?
        WHERE id = ?
        """,
        (
            progress,
            enrollment_id
        )
    )

    # Save the inserted user permanently in the SQLite database and close the database connection.

    conn.commit()
    conn.close()

    # After the Updation it's re-direct to the 'http://127.0.0.1:5000/my-courses'.

    return redirect("/my-courses")



# Display the logged-in user's profile information.
# Also calculate and display learning statistics.
# This function executes whenever the user visits 'http://127.0.0.1:5000/profile'.

@app.route("/profile")
def profile():

    if "user_id" not in session:
        return redirect("/login")

    # Get the Database connection course.db

    conn = get_connection()

    # Retrieve the logged-in user's personal information from the database.

    user = conn.execute(
        """
        SELECT *
        FROM users
        WHERE id = ?
        """,
        (session["user_id"],)
    ).fetchone()

    # Count the total number of courses enrolled by the current user. 

    total_enrollments = conn.execute(
        """
        SELECT COUNT(*)
        FROM enrollments
        WHERE user_id = ?
        """,
        (session["user_id"],)
    ).fetchone()[0]

    # Count the number of courses whose progress has reached 100%.

    completed_courses = conn.execute(
        """
        SELECT COUNT(*)
        FROM enrollments
        WHERE user_id = ?
        AND progress = 100
        """,
        (session["user_id"],)
    ).fetchone()[0]


    # Calculate how many enrolled courses are still incomplete.

    in_progress_courses = total_enrollments - completed_courses

    # Connection Close

    conn.close()

    # Render the profile.html template

    return render_template(
        "profile.html",
        user=user,
        total_enrollments=total_enrollments,
        completed_courses=completed_courses,
        in_progress_courses=in_progress_courses
    )

# Allow the logged-in user to update their name and email address.
# Display the current profile details before editing.
# This function executes whenever the user visits 'http://127.0.0.1:5000/edit-profile'.

@app.route("/edit-profile",
           methods=["GET", "POST"])
def edit_profile():

    # If user is not Login with their Credentials It re-direct to the Login Page

    if "user_id" not in session:
        return redirect("/login")
    
    # Get the Database Connection

    conn = get_connection()

    # Select the User from the User Table Using ID

    user = conn.execute(
        """
        SELECT *
        FROM users
        WHERE id = ?
        """,
        (session["user_id"],)
    ).fetchone()

    if request.method == "POST":

        # Retrieve the user's entered name, email from the submitted HTML form.

        name = request.form["name"]
        email = request.form["email"]

        # Update the User Details using the ID 

        conn.execute(
            """
            UPDATE users
            SET
                name = ?,
                email = ?
            WHERE id = ?
            """,
            (
                name,
                email,
                session["user_id"]
            )
        )

        # Save the inserted user permanently in the SQLite database and close the database connection.

        conn.commit()
        conn.close()

        # Set the session name as the newly updated name 

        session["user_name"] = name

        # Redirect to the Profile page

        return redirect("/profile")

    # Close the Database Connection

    conn.close()

    # render the edit_profile.html template 

    return render_template(
        "edit_profile.html",
        user=user
    )



# Remove all data stored in the user's session.
# This effectively logs the user out of the application.
# This function executes whenever the user visits 'http://127.0.0.1:5000/logout'.

@app.route("/logout")
def logout():

    # Clear the Session and redirect to the Home Page

    session.clear()
    return redirect("/")



# Start Flask's built-in development server.
# The application begins listening for incoming HTTP requests.

if __name__ == "__main__":
    app.run(debug=True)
