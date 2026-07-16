from flask import make_response, render_template, Blueprint
from weasyprint import HTML
from utils.analytics.reports import (get_executive_summary,)
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

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

booking_chart = "file://" + os.path.join(
    BASE_DIR,
    "static",
    "reports",
    "booking_chart.png"
)

customer_chart = "file://" + os.path.join(
    BASE_DIR,
    "static",
    "reports",
    "customer_chart.png"
)

revenue_chart = "file://" + os.path.join(
    BASE_DIR,
    "static",
    "reports",
    "revenue_chart.png"
)

cancellation_chart = "file://" + os.path.join(
    BASE_DIR,
    "static",
    "reports",
    "cancellation_chart.png"
)

statistics_chart = "file://" + os.path.join(
    BASE_DIR,
    "static",
    "reports",
    "statistical_chart.png"
)


report_download = Blueprint(

    "download_report",

    __name__

)

def cancellation():
    return {
        "cancellation_rate" : get_cancellation_status(),
        "highest_month" : get_cancellation_status(),
        "market_segment" : get_cancellation_by_market_segment(),
        "average_lead_time" : get_lead_time_by_cancellation()
    }

@report_download.route("/reports/download")
def download_report():

    html = render_template(

        "report_pdf.html",

        kpis=get_executive_summary(),

        booking_kpis=get_booking_kpis(),

        revenue_kpis=get_revenue_kpis(),

        customer_kpis=get_customer_kpis(),

        cancellation_kpis=cancellation(),

        statistics_summary=get_decision_report(),

        generated_date = datetime.now(),

        business_insights = [
            "Peak booking demand occurs during the summer season.",
            "City Hotels contribute the largest share of bookings.",
            "Long lead-time bookings have a higher cancellation probability.",
            "Average Daily Rate increases significantly during peak months.",
            "Most bookings originate from Online Travel Agencies."
        ],

        booking_chart=booking_chart,
        customer_chart=customer_chart,
        revenue_chart=revenue_chart,
        cancellation_chart=cancellation_chart,
        statistics_chart=statistics_chart

    )

    pdf = HTML(string=html).write_pdf()

    response = make_response(pdf)

    response.headers["Content-Type"] = "application/pdf"

    response.headers["Content-Disposition"] = (
        "attachment; filename=Hotel_Booking_Analytics_Report.pdf"
    )

    return response

print("=========================summary================================")
print(get_executive_summary())
print("=========================Booking================================")
print(get_booking_kpis())
print("=========================revenue================================")
print(get_revenue_kpis())
print("=========================customer================================")
print(get_customer_kpis())
print("=========================cancel================================")
print(cancellation())
print("=========================report================================")
print(get_decision_report())