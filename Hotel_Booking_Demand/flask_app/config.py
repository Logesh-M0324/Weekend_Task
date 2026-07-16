import os

# Get the absolute path of the current Flask application directory.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Remove the '/flask_app' folder to obtain the project's root directory.
BASE_DIR = BASE_DIR.replace("/flask_app", "")


# Secret key used by Flask to securely manage sessions and flash messages.
SECRET_KEY = "hotel_booking_secret_key"

# Construct the absolute path to the processed hotel booking dataset.
DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "final_hotel_bookings.csv"
)
