import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

print(BASE_DIR)

BASE_DIR = BASE_DIR.replace("/flask_app", "")

print(BASE_DIR)

SECRET_KEY = "hotel_booking_secret_key"

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "final_hotel_bookings.csv"
)

print(DATA_PATH)