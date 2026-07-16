from flask import Blueprint
from flask import render_template

from utils.analytics.reports import (

    get_executive_summary,

    get_booking_report,

    get_revenue_report,

    get_customer_report,

    get_cancellation_report,

    get_statistical_report

)

# Create a Blueprint for the Reports module.
# This blueprint manages routes related to analytical reports.
reports_bp = Blueprint(

    "reports",

    __name__

)


# Route for the Reports page.
# Displays summary tables generated from the
# processed hotel booking dataset.
@reports_bp.route("/reports")
def reports():

    # Render the reports template and pass
    # all analytical report data.
    return render_template(

        "reports.html",

        # Executive summary metrics.
        executive=get_executive_summary(),

        # Booking analysis report.
        booking=get_booking_report(),

        # Revenue analysis report.
        revenue=get_revenue_report(),

        # Customer analysis report.
        customer=get_customer_report(),

        # Cancellation analysis report.
        cancellation=get_cancellation_report(),

        # Statistical analysis report.
        statistical=get_statistical_report()

    )