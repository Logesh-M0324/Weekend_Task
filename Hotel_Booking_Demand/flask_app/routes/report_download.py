from flask import make_response, render_template, Blueprint

from weasyprint import HTML
<<<<<<< HEAD

from utils.analytics.reports import (get_executive_summary,)
=======
from utils.analytics.reports import get_executive_summary
>>>>>>> f1480bbecb5f7f086e6cf32ddca18dd327e95e3b
from utils.analytics.booking import get_booking_kpis
from utils.analytics.revenue import get_revenue_kpis
from utils.analytics.cancellation import (
    get_cancellation_kpis,
    get_cancellation_by_hotel,
    get_cancellation_by_market_segment,
    get_cancellation_status,
    get_lead_time_by_cancellation
)
from utils.analytics.customer import get_customer_kpis
from utils.analytics.statistics import get_decision_report
from datetime import datetime
import os

# -------------------------------------------------------
# Configure paths for report images
# -------------------------------------------------------

# Get the project's base directory.
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Absolute file path for the booking analytics chart.
booking_chart = "file://" + os.path.join(
    BASE_DIR,
    "static",
    "reports",
    "booking_chart.png"
)

# Absolute file path for the customer analytics chart.
customer_chart = "file://" + os.path.join(
    BASE_DIR,
    "static",
    "reports",
    "customer_chart.png"
)

# Absolute file path for the revenue analytics chart.
revenue_chart = "file://" + os.path.join(
    BASE_DIR,
    "static",
    "reports",
    "revenue_chart.png"
)

# Absolute file path for the cancellation analytics chart.
cancellation_chart = "file://" + os.path.join(
    BASE_DIR,
    "static",
    "reports",
    "cancellation_chart.png"
)

# Absolute file path for the statistical analysis chart.
statistics_chart = "file://" + os.path.join(
    BASE_DIR,
    "static",
    "reports",
    "statistical_chart.png"
)

# -------------------------------------------------------
# Create Blueprint
# -------------------------------------------------------

# Blueprint responsible for generating and downloading
# the PDF business report.
report_download = Blueprint(

    "download_report",

    __name__

)

# -------------------------------------------------------
# Collect cancellation metrics required for the report
# -------------------------------------------------------

# Prepare cancellation-related analytical data that
# will be displayed in the PDF report.
def cancellation():

    return {

        "cancellation_rate": get_cancellation_status(),

        "highest_month": get_cancellation_status(),

        "market_segment": get_cancellation_by_market_segment(),

        "average_lead_time": get_lead_time_by_cancellation()

    }


# -------------------------------------------------------
# Download PDF Report
# -------------------------------------------------------

# Generate a complete Hotel Booking Analytics PDF report
# and return it as a downloadable file.
@report_download.route("/reports/download")
def download_report():

    # Render the HTML report template with all required
    # analytics, KPIs, charts, and business insights.
    html = render_template(

        "report_pdf.html",

        # Executive summary KPIs.
        kpis=get_executive_summary(),

        # Booking analytics summary.
        booking_kpis=get_booking_kpis(),

        # Revenue analytics summary.
        revenue_kpis=get_revenue_kpis(),

        # Customer analytics summary.
        customer_kpis=get_customer_kpis(),

        # Cancellation analytics summary.
        cancellation_kpis=cancellation(),

        # Statistical analysis results.
        statistics_summary=get_decision_report(),

        # Current report generation date and time.
        generated_date=datetime.now(),

        # Business insights displayed in the report.
        business_insights=[
            "Peak booking demand occurs during the summer season.",
            "City Hotels contribute the largest share of bookings.",
            "Long lead-time bookings have a higher cancellation probability.",
            "Average Daily Rate increases significantly during peak months.",
            "Most bookings originate from Online Travel Agencies."
        ],

        # Chart images included in the PDF.
        booking_chart=booking_chart,

        customer_chart=customer_chart,

        revenue_chart=revenue_chart,

        cancellation_chart=cancellation_chart,

        statistics_chart=statistics_chart

    )

    # Convert the rendered HTML into PDF format.
    pdf = HTML(string=html).write_pdf()

    # Create a Flask response containing the PDF.
    response = make_response(pdf)

    # Specify the response content type as PDF.
    response.headers["Content-Type"] = "application/pdf"

    # Force the browser to download the generated PDF.
    response.headers["Content-Disposition"] = (
        "attachment; filename=Hotel_Booking_Analytics_Report.pdf"
    )

    # Return the generated PDF file.
    return response