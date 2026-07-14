from flask import Blueprint, render_template

from utils.analytics.dashboard import get_dashboard_kpis, get_monthly_booking_trend, get_booking_status, get_executive_cards 

home_bp = Blueprint(

    "home",

    __name__

)


@home_bp.route("/")
def home():

    kpis = get_dashboard_kpis()

    return render_template(

        "home.html",

        kpis=get_dashboard_kpis(),

        monthly=get_monthly_booking_trend(),

        executive=get_executive_cards(),

        booking_status=get_booking_status()

    )