from flask import Blueprint, render_template

from utils.analytics.cancellation import (

    get_cancellation_kpis,

    get_cancellation_status,

    get_cancellation_by_hotel,

    get_cancellation_by_market_segment,

    get_cancellation_by_deposit,

    get_lead_time_by_cancellation

)

cancellation_bp = Blueprint(

    "cancellation",

    __name__

)


@cancellation_bp.route("/cancellation")
def cancellation():

    return render_template(

        "cancellation.html",

        kpis=get_cancellation_kpis(),

        status=get_cancellation_status(),

        hotels=get_cancellation_by_hotel(),

        markets=get_cancellation_by_market_segment(),

        deposits=get_cancellation_by_deposit(),

        lead_time=get_lead_time_by_cancellation()

    )