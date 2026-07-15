from flask import Blueprint, render_template, request
import pandas as pd

explorer_bp = Blueprint(
    "explorer",
    __name__
)

DATA_PATH = "/home/aximsoft/Downloads/Weekend_Task/Hotel_Booking_Demand/data/processed/final_hotel_bookings.csv"

df = pd.read_csv(DATA_PATH)


@explorer_bp.route("/explorer")
def explorer():

    filtered_df = df.copy()

    # -----------------------------------------
    # Request Parameters
    # -----------------------------------------

    search = request.args.get("search", "").strip()

    hotel = request.args.get("hotel", "")

    country = request.args.get("country", "")

    month = request.args.get("month", "")

    sort_by = request.args.get("sort_by", "")

    order = request.args.get("order", "asc")

    page = request.args.get(
        "page",
        1,
        type=int
    )

    # -----------------------------------------
    # Search
    # -----------------------------------------

    if search:

        filtered_df = filtered_df[
            filtered_df.astype(str)
            .apply(
                lambda col: col.str.contains(
                    search,
                    case=False,
                    na=False
                )
            )
            .any(axis=1)
        ]

    # -----------------------------------------
    # Hotel Filter
    # -----------------------------------------

    if hotel:

        filtered_df = filtered_df[
            filtered_df["hotel"] == hotel
        ]

    # -----------------------------------------
    # Country Filter
    # -----------------------------------------

    if country:

        filtered_df = filtered_df[
            filtered_df["country"] == country
        ]

    # -----------------------------------------
    # Month Filter
    # -----------------------------------------

    if month:

        filtered_df = filtered_df[
            filtered_df["arrival_date_month"] == month
        ]

    # -----------------------------------------
    # Sorting
    # -----------------------------------------

    if sort_by and sort_by in filtered_df.columns:

        filtered_df = filtered_df.sort_values(

            by=sort_by,

            ascending=(order == "asc"),

            na_position="last"

        )


    # -----------------------------------------
    # Pagination
    # -----------------------------------------

    per_page = 20

    total_records = len(filtered_df)

    total_pages = (

        total_records + per_page - 1

    ) // per_page

    start = (page - 1) * per_page

    end = start + per_page

    records = filtered_df.iloc[
        start:end
    ].to_dict(
        orient="records"
    )

    columns = filtered_df.columns.tolist()

    hotels = sorted(
        df["hotel"].dropna().unique()
    )

    countries = sorted(
        df["country"].dropna().unique()
    )

    months = [

        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"

    ]

    # -----------------------------------------
    # Render Template
    # -----------------------------------------

    return render_template(

        "explorer.html",

        records=records,

        columns=columns,

        hotels=hotels,

        countries=countries,

        months=months,

        search=search,

        hotel=hotel,

        country=country,

        month=month,

        sort_by=sort_by,

        order=order,

        page=page,

        per_page=per_page,

        total_pages=total_pages,

        total_records=total_records

    )