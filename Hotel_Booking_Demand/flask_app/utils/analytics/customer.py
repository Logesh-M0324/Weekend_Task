from utils.loader import load_data

df = load_data()


def get_customer_kpis():

    return {

        "total_customers": len(df),

        "repeat_guests": int(df["is_repeated_guest"].sum()),

        "new_guests": int((df["is_repeated_guest"] == 0).sum()),

        "countries": df["country"].nunique()

    }


def get_customer_type_distribution():

    return (

        df.groupby("customer_type")

        .size()

        .reset_index(name="count")

    )


def get_market_segment_distribution():

    return (

        df.groupby("market_segment")

        .size()

        .reset_index(name="count")

    )


def get_country_distribution():

    return (

        df.groupby("country")

        .size()

        .sort_values(ascending=False)

        .head(10)

        .reset_index(name="count")

    )


def get_repeat_guest_distribution():

    repeat = (

        df["is_repeated_guest"]

        .value_counts()

        .sort_index()

        .reset_index()

    )

    repeat.columns = [

        "is_repeated_guest",

        "count"

    ]

    return repeat