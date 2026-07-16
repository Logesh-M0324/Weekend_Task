from flask import Blueprint, render_template, request
import pandas as pd

# Create a Blueprint for the Data Explorer module.
# This blueprint manages routes related to dataset exploration.
explorer_bp = Blueprint(
    "explorer",
    __name__
)

# Path to the cleaned hotel booking dataset.
DATA_PATH = "/home/aximsoft/Downloads/Weekend_Task/Hotel_Booking_Demand/data/processed/final_hotel_bookings.csv"

# Load the dataset once when the application starts.
# This avoids reading the CSV file on every request.
df = pd.read_csv(DATA_PATH)


# Route to display the interactive Data Explorer page.
# Supports searching, filtering, sorting, and pagination.
@explorer_bp.route("/explorer")
def explorer():

    # Create a copy of the original dataset so that
    # filtering operations do not modify the source data.
    filtered_df = df.copy()

    # -----------------------------------------
    # Retrieve Query Parameters
    # -----------------------------------------

    # Search keyword entered by the user.
    search = request.args.get("search", "").strip()

    # Selected hotel type filter.
    hotel = request.args.get("hotel", "")

    # Selected country filter.
    country = request.args.get("country", "")

    # Selected arrival month filter.
    month = request.args.get("month", "")

    # Selected column used for sorting.
    sort_by = request.args.get("sort_by", "")

    # Sorting order (Ascending or Descending).
    order = request.args.get("order", "asc")

    # Current page number for pagination.
    page = request.args.get(
        "page",
        1,
        type=int
    )

    # -----------------------------------------
    # Global Search
    # -----------------------------------------

    # Search the entered keyword across every column
    # and return rows containing a matching value.
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
    # Hotel Type Filter
    # -----------------------------------------

    # Display records matching the selected hotel type.
    if hotel:

        filtered_df = filtered_df[
            filtered_df["hotel"] == hotel
        ]

    # -----------------------------------------
    # Country Filter
    # -----------------------------------------

    # Display records belonging to the selected country.
    if country:

        filtered_df = filtered_df[
            filtered_df["country"] == country
        ]

    # -----------------------------------------
    # Arrival Month Filter
    # -----------------------------------------

    # Display records for the selected arrival month.
    if month:

        filtered_df = filtered_df[
            filtered_df["arrival_date_month"] == month
        ]

    # -----------------------------------------
    # Sorting
    # -----------------------------------------

    # Sort the filtered dataset based on the selected
    # column and sorting order.
    if sort_by and sort_by in filtered_df.columns:

        filtered_df = filtered_df.sort_values(

            by=sort_by,

            ascending=(order == "asc"),

            na_position="last"

        )

    # -----------------------------------------
    # Pagination
    # -----------------------------------------

    # Number of records displayed on each page.
    per_page = 20

    # Total records after applying filters.
    total_records = len(filtered_df)

    # Calculate the total number of pages.
    total_pages = (

        total_records + per_page - 1

    ) // per_page

    # Calculate the starting row index.
    start = (page - 1) * per_page

    # Calculate the ending row index.
    end = start + per_page

    # Convert the current page records into
    # dictionary format for Jinja rendering.
    records = filtered_df.iloc[
        start:end
    ].to_dict(
        orient="records"
    )

    # Retrieve all column names for the table header.
    columns = filtered_df.columns.tolist()

    # Retrieve unique hotel types for the filter dropdown.
    hotels = sorted(
        df["hotel"].dropna().unique()
    )

    # Retrieve unique countries for the filter dropdown.
    countries = sorted(
        df["country"].dropna().unique()
    )

    # Define the arrival month list used in the filter.
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
    # Render Explorer Page
    # -----------------------------------------

    # Pass all filtered data, pagination details,
    # and filter options to the HTML template.
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