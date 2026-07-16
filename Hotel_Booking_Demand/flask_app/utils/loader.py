import pandas as pd
from config import DATA_PATH


def load_data():
    """
    Load the processed Hotel Booking dataset from the configured file path.

    Reads the cleaned CSV dataset into a Pandas DataFrame and returns it so
    that other analytics modules can use the same centralized dataset.
    """

    df = pd.read_csv(DATA_PATH)

    return df