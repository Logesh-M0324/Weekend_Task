from flask import Blueprint, render_template

from utils.analytics.booking import (

    get_monthly_bookings,

    get_hotel_type_bookings,

    get_season_bookings,

    get_lead_time_distribution,

    get_booking_kpis

)

booking_bp = Blueprint(

    "booking",

    __name__

)


@booking_bp.route("/booking")
def booking():

    return render_template(

        "booking.html",

        monthly=get_monthly_bookings(),

        hotels=get_hotel_type_bookings(),

        booking_kpis=get_booking_kpis(),

        seasons=get_season_bookings(),

        lead_time=get_lead_time_distribution()

    )