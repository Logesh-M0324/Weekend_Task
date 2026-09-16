from pathlib import Path

from sql_analytics import (
    get_customer_profile
)

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = (
    BASE_DIR /
    "data" /
    "processed" /
    "customer_intelligence.db"
)

