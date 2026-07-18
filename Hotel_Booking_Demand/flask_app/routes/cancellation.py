from flask import Blueprint, render_template

# Import all analytics functions required for the
# Cancellation Analytics Dashboard.
from utils.analytics.cancellation import (

    # Returns KPI values such as total bookings,
    # cancelled bookings, non-cancelled bookings and cancellation rate.
    get_cancellation_kpis,

    # Returns booking counts grouped by
    # cancellation status (Cancelled / Not Cancelled).
    get_cancellation_status,

    # Returns total cancelled bookings
    # for each hotel type.
    get_cancellation_by_hotel,

    # Returns cancellation counts
    # grouped by market segment.
    get_cancellation_by_market_segment,

    # Returns cancellation counts
    # grouped by deposit type.
    get_cancellation_by_deposit,

    # Returns the average lead time for
    # cancelled and non-cancelled bookings.
    get_lead_time_by_cancellation

)

# Create a Blueprint for all
# Cancellation-related routes.
cancellation_bp = Blueprint(

    "cancellation",

    __name__

)


# Route to display the
# Cancellation Analytics Dashboard.
@cancellation_bp.route("/cancellation")
def cancellation():

    # Render the cancellation dashboard template
    # and pass all required analytical datasets.
    return render_template(

        "cancellation.html",

        # KPI summary cards
        kpis=get_cancellation_kpis(),

        # Cancellation status distribution
        status=get_cancellation_status(),

        # Cancellation count by hotel type
        hotels=get_cancellation_by_hotel(),

        # Cancellation count by market segment
        markets=get_cancellation_by_market_segment(),

        # Cancellation count by deposit type
        deposits=get_cancellation_by_deposit(),

        # Average lead time comparison
        # for cancelled vs non-cancelled bookings
        lead_time=get_lead_time_by_cancellation()

    )