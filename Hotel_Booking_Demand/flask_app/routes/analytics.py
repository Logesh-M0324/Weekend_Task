from flask import Blueprint, render_template

# Import all customer analytics functions required for the dashboard
from utils.analytics.customer import (
    get_customer_kpis,
    get_customer_type_distribution,
    get_market_segment_distribution,
    get_country_distribution,
    get_repeat_guest_distribution
)

# Create a Blueprint for Customer Analytics routes.
# This helps organize customer-related URLs separately from other modules.
customer_bp = Blueprint(
    "customer",
    __name__
)


@customer_bp.route("/customer")
def customer():
    """
    Customer Analytics Dashboard

    This route loads all customer-related analytics including:
    - Customer KPI cards
    - Customer type distribution
    - Market segment distribution
    - Top customer countries
    - Repeat guest distribution

    The collected data is passed to the customer.html template
    where interactive charts and KPI cards are displayed.
    """

    return render_template(

        "customer.html",

        # Customer KPI metrics
        kpis=get_customer_kpis(),

        # Distribution of different customer types
        customer_types=get_customer_type_distribution(),

        # Distribution of bookings across market segments
        market_segments=get_market_segment_distribution(),

        # Top 10 countries based on customer bookings
        countries=get_country_distribution(),

        # Repeat vs New guest distribution
        repeat_guests=get_repeat_guest_distribution()

    )