from database import get_connection

conn = get_connection()

courses = [
    (
        "Python Programming",
        "Programming",
        "20 Hours",
        "Learn Python from basics to advanced."
    ),
    (
        "Flask Development",
        "Web Development",
        "15 Hours",
        "Build web applications using Flask."
    ),
    (
        "Data Science",
        "Data Analytics",
        "25 Hours",
        "Learn data analysis and machine learning."
    ),
    # --- 20 New Courses Below ---
    (
        "JavaScript Essentials",
        "Web Development",
        "12 Hours",
        "Master the fundamentals of modern JavaScript programming."
    ),
    (
        "React for Beginners",
        "Web Development",
        "18 Hours",
        "Build dynamic, component-based user interfaces with React."
    ),
    (
        "Django Web Framework",
        "Web Development",
        "22 Hours",
        "Develop robust, secure backends using Python's Django framework."
    ),
    (
        "SQL & Database Design",
        "Data Analytics",
        "10 Hours",
        "Write complex queries and design efficient relational databases."
    ),
    (
        "Machine Learning Deep Dive",
        "Data Analytics",
        "30 Hours",
        "Implement predictive models and algorithms using Scikit-Learn."
    ),
    (
        "Data Visualization with Tableau",
        "Data Analytics",
        "8 Hours",
        "Create interactive dashboards and insightful business reports."
    ),
    (
        "Introduction to Docker",
        "DevOps",
        "6 Hours",
        "Containerize your applications for seamless deployment."
    ),
    (
        "CI/CD Pipelines with GitHub Actions",
        "DevOps",
        "10 Hours",
        "Automate your testing and deployment workflows effortlessly."
    ),
    (
        "AWS Cloud Practitioner",
        "Cloud Computing",
        "15 Hours",
        "Understand foundational AWS services, security, and pricing."
    ),
    (
        "Git and GitHub Mastery",
        "Programming",
        "5 Hours",
        "Learn version control, branching strategies, and collaboration."
    ),
    (
        "Java Core Fundamentals",
        "Programming",
        "25 Hours",
        "Master object-oriented programming concepts using Java."
    ),
    (
        "Data Structures & Algorithms",
        "Programming",
        "35 Hours",
        "Crack coding interviews by mastering stacks, trees, and graphs."
    ),
    (
        "HTML5 & CSS3 Layouts",
        "Web Development",
        "8 Hours",
        "Build responsive, modern web pages using Flexbox and Grid."
    ),
    (
        "Node.js Backend Services",
        "Web Development",
        "16 Hours",
        "Create scalable server-side applications using Express framework."
    ),
    (
        "Deep Learning with PyTorch",
        "Data Analytics",
        "28 Hours",
        "Build neural networks for computer vision and text processing."
    ),
    (
        "Cybersecurity Fundamentals",
        "Information Technology",
        "14 Hours",
        "Learn the basics of network security, cryptography, and defense."
    ),
    (
        "Linux Command Line Basics",
        "Information Technology",
        "7 Hours",
        "Navigate the file system and automate tasks using bash scripting."
    ),
    (
        "Agile & Scrum Methodologies",
        "Project Management",
        "6 Hours",
        "Manage software engineering teams using sprint frameworks."
    ),
    (
        "UI/UX Design Principles",
        "Design",
        "12 Hours",
        "Design user-friendly wireframes and prototypes using Figma."
    ),
    (
        "API Testing with Postman",
        "Programming",
        "5 Hours",
        "Validate and automate endpoint testing for RESTful Web APIs."
    )
]

conn.executemany(
    """
    INSERT INTO courses
    (
        course_name,
        category,
        duration,
        description
    )
    VALUES (?, ?, ?, ?)
    """,
    courses
)

conn.commit()
conn.close()

print("Courses Added Successfully")
