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

reports_bp = Blueprint(

    "reports",

    __name__

)


@reports_bp.route("/reports")

def reports():

    return render_template(

        "reports.html",

        executive=get_executive_summary(),

        booking=get_booking_report(),

        revenue=get_revenue_report(),

        customer=get_customer_report(),

        cancellation=get_cancellation_report(),

        statistical=get_statistical_report()

    )