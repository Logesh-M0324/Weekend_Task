from utils.loader import load_data

df = load_data()


def get_cancellation_kpis():

    total = len(df)

    cancelled = int(df["is_canceled"].sum())

    not_cancelled = total - cancelled

    cancellation_rate = round((cancelled / total) * 100, 2)

    return {

        "total_bookings": total,

        "cancelled": cancelled,

        "not_cancelled": not_cancelled,

        "cancellation_rate": cancellation_rate

    }


def get_cancellation_status():

    status = (

        df["is_canceled"]

        .value_counts()

        .sort_index()

        .reset_index()

    )

    status.columns = [

        "status",

        "count"

    ]

    return status


def get_cancellation_by_hotel():

    return (

        df.groupby("hotel")["is_canceled"]

        .sum()

        .reset_index(name="cancelled")

    )


def get_cancellation_by_market_segment():

    return (

        df.groupby("market_segment")["is_canceled"]

        .sum()

        .reset_index(name="cancelled")

    )


def get_cancellation_by_deposit():

    return (

        df.groupby("deposit_type")["is_canceled"]

        .sum()

        .reset_index(name="cancelled")

    )


def get_lead_time_by_cancellation():

    return (

        df.groupby("is_canceled")["lead_time"]

        .mean()

        .reset_index()

    )