from flask import Blueprint, render_template

from utils.analytics.dashboard import (
    get_dashboard_kpis,
    get_monthly_booking_trend,
    get_booking_status,
    get_executive_cards
)

# Create a Blueprint for the Home Dashboard.
# This blueprint manages the application's landing page.
home_bp = Blueprint(

    "home",

    __name__

)


# Route for the application's home page.
# Displays the dashboard with KPIs, charts,
# and executive summary information.
@home_bp.route("/")
def home():

    # Retrieve the dashboard KPI metrics.
    kpis = get_dashboard_kpis()

    # Render the dashboard template and pass
    # all required analytics data for visualization.
    return render_template(

        "home.html",

        # Dashboard KPI cards.
        kpis=kpis,

        # Monthly booking trend for the line chart.
        monthly=get_monthly_booking_trend(),

        # Executive summary cards.
        executive=get_executive_cards(),

        # Booking status distribution
        # (Completed vs Cancelled).
        booking_status=get_booking_status()

    )