import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "hotel_booking_secret_key"

DATA_PATH = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "processed",
    "hotel_booking_cleaned.csv"
)