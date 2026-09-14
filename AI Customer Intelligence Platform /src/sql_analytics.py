import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "customer_intelligence.db"
)


def get_connection():
    return sqlite3.connect(DB_PATH)


def get_customer_profile(customer_id):

    query = """
    SELECT *
    FROM customers
    WHERE customerID = ?;
    """

    with get_connection() as connection:

        result = pd.read_sql_query(
            query,
            connection,
            params=(customer_id,)
        )

    return result


def get_churn_summary():

    query = """
    SELECT
        COUNT(*) AS total_customers,

        SUM(
            CASE
                WHEN Churn = 'Yes'
                THEN 1
                ELSE 0
            END
        ) AS churned_customers,

        ROUND(
            100.0 *
            SUM(
                CASE
                    WHEN Churn = 'Yes'
                    THEN 1
                    ELSE 0
                END
            ) / COUNT(*),
            2
        ) AS churn_rate

    FROM customers;
    """

    with get_connection() as connection:

        result = pd.read_sql_query(
            query,
            connection
        )

    return result