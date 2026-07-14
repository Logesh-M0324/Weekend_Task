from flask import Blueprint, render_template

from utils.analytics.customer import (

    get_customer_kpis,

    get_customer_type_distribution,

    get_market_segment_distribution,

    get_country_distribution,

    get_repeat_guest_distribution

)

customer_bp = Blueprint(

    "customer",

    __name__

)


@customer_bp.route("/customer")
def customer():

    return render_template(

        "customer.html",

        kpis=get_customer_kpis(),

        customer_types=get_customer_type_distribution(),

        market_segments=get_market_segment_distribution(),

        countries=get_country_distribution(),

        repeat_guests=get_repeat_guest_distribution()

    )