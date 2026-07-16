from flask import Blueprint, render_template

# Import all booking analytics functions required for the Booking Dashboard.
from utils.analytics.booking import (

    # Returns monthly booking counts for the booking trend chart.
    get_monthly_bookings,

    # Returns booking counts grouped by hotel type.
    get_hotel_type_bookings,

    # Returns booking counts grouped by booking season.
    get_season_bookings,

    # Returns lead time values for plotting the lead time distribution.
    get_lead_time_distribution,

    # Returns booking KPI metrics displayed as dashboard cards.
    get_booking_kpis

)

# Create a Blueprint to organize all booking-related routes.
booking_bp = Blueprint(

    "booking",

    __name__

)


# Route for displaying the Booking Analytics Dashboard.
@booking_bp.route("/booking")
def booking():

    # Render the booking dashboard template and pass all
    # booking KPIs and chart datasets to the HTML page.
    return render_template(

        "booking.html",

        # Monthly booking trend data.
        monthly=get_monthly_bookings(),

        # Hotel type comparison data.
        hotels=get_hotel_type_bookings(),

        # KPI card values.
        booking_kpis=get_booking_kpis(),

        # Seasonal booking distribution data.
        seasons=get_season_bookings(),

        # Lead time distribution data.
        lead_time=get_lead_time_distribution()

    )