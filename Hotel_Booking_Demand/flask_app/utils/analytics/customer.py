from utils.loader import load_data

# Load the cleaned hotel booking dataset once when the module is imported.
# This DataFrame is reused by all customer analytics functions.
df = load_data()


# ---------------------------------------------------------
# Customer KPI Metrics
# ---------------------------------------------------------
def get_customer_kpis():

    # Calculate key customer-related metrics including
    # total customers, repeat guests, new guests, and countries.
    return {

        # Total number of booking records (customers) in the dataset.
        "total_customers": len(df),

        # Count the total number of repeat guests.
        "repeat_guests": int(df["is_repeated_guest"].sum()),

        # Count the total number of first-time (new) guests.
        "new_guests": int((df["is_repeated_guest"] == 0).sum()),

        # Calculate the number of unique countries
        # from which customers have made bookings.
        "countries": df["country"].nunique()

    }


# ---------------------------------------------------------
# Customer Type Distribution
# ---------------------------------------------------------
def get_customer_type_distribution():

    # Group booking records by customer type and calculate
    # the total number of customers in each category.
    return (

        df.groupby("customer_type")

        .size()

        .reset_index(name="count")

    )


# ---------------------------------------------------------
# Market Segment Distribution
# ---------------------------------------------------------
def get_market_segment_distribution():

    # Count the number of bookings received from each
    # market segment such as Online TA, Direct, and Groups.
    return (

        df.groupby("market_segment")

        .size()

        .reset_index(name="count")

    )


# ---------------------------------------------------------
# Top 10 Customer Countries
# ---------------------------------------------------------
def get_country_distribution():

    # Calculate booking counts for every country,
    # sort them in descending order, and return the top 10.
    return (

        df.groupby("country")

        .size()

        .sort_values(ascending=False)

        .head(10)

        .reset_index(name="count")

    )


# ---------------------------------------------------------
# Repeat Guest Distribution
# ---------------------------------------------------------
def get_repeat_guest_distribution():

    # Count repeat and non-repeat guests and convert
    # the result into a DataFrame for visualization.
    repeat = (

        df["is_repeated_guest"]

        .value_counts()

        .sort_index()

        .reset_index()

    )

    # Rename the columns to improve readability
    # in charts and dashboard tables.
    repeat.columns = [

        "is_repeated_guest",

        "count"

    ]

    return repeat