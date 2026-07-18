from utils.loader import load_data

# Load the cleaned hotel booking dataset once when the module is imported.
# This DataFrame will be shared across all cancellation analytics functions.
df = load_data()


# ---------------------------------------------------------
# Cancellation KPI Metrics
# ---------------------------------------------------------
def get_cancellation_kpis():

    # Calculate the total number of bookings available
    # in the dataset.
    total = len(df)

    # Count the total number of cancelled bookings.
    # The is_canceled column contains 1 for cancelled bookings.
    cancelled = int(df["is_canceled"].sum())

    # Calculate the number of bookings that were not cancelled.
    not_cancelled = total - cancelled

    # Compute the cancellation percentage and round
    # the result to two decimal places.
    cancellation_rate = round((cancelled / total) * 100, 2)

    # Return all cancellation KPIs as a dictionary
    # for displaying summary cards on the dashboard.
    return {

        "total_bookings": total,

        "cancelled": cancelled,

        "not_cancelled": not_cancelled,

        "cancellation_rate": cancellation_rate

    }


# ---------------------------------------------------------
# Cancellation Status Distribution
# ---------------------------------------------------------
def get_cancellation_status():

    # Count the number of cancelled and non-cancelled
    # bookings and convert the result into a DataFrame.
    status = (

        df["is_canceled"]

        .value_counts()

        .sort_index()

        .reset_index()

    )

    # Rename the columns to make them more readable
    # when used in charts and tables.
    status.columns = [

        "status",

        "count"

    ]

    return status


# ---------------------------------------------------------
# Cancellation by Hotel Type
# ---------------------------------------------------------
def get_cancellation_by_hotel():

    # Group bookings by hotel type and calculate
    # the total number of cancelled bookings.
    return (

        df.groupby("hotel")["is_canceled"]

        .sum()

        .reset_index(name="cancelled")

    )


# ---------------------------------------------------------
# Cancellation by Market Segment
# ---------------------------------------------------------
def get_cancellation_by_market_segment():

    # Analyze cancellations across different booking
    # market segments such as Online TA, Direct, and Groups.
    return (

        df.groupby("market_segment")["is_canceled"]

        .sum()

        .reset_index(name="cancelled")

    )


# ---------------------------------------------------------
# Cancellation by Deposit Type
# ---------------------------------------------------------
def get_cancellation_by_deposit():

    # Calculate the number of cancelled bookings for
    # each deposit type category.
    return (

        df.groupby("deposit_type")["is_canceled"]

        .sum()

        .reset_index(name="cancelled")

    )


# ---------------------------------------------------------
# Lead Time by Cancellation Status
# ---------------------------------------------------------
def get_lead_time_by_cancellation():

    # Compute the average booking lead time separately
    # for cancelled and non-cancelled bookings.
    return (

        df.groupby("is_canceled")["lead_time"]

        .mean()

        .reset_index()

    )