from flask import Blueprint, render_template

from utils.analytics.revenue import (

    get_revenue_kpis,

    get_monthly_adr,

    get_hotel_revenue,

    get_market_segment_adr,

    get_weekend_weekday_adr,

    get_customer_type_adr

)

revenue_bp = Blueprint(

    "revenue",

    __name__

)


@revenue_bp.route("/revenue")
def revenue():

    return render_template(

        "revenue.html",

        kpis=get_revenue_kpis(),

        monthly=get_monthly_adr(),

        hotels=get_hotel_revenue(),

        segments=get_market_segment_adr(),

        stay=get_weekend_weekday_adr(),

        customers=get_customer_type_adr()

    )