from flask import Blueprint, render_template

# Import all customer analytics functions
# used to generate dashboard data.
from utils.analytics.customer import (

    # Returns KPI values such as total customers,
    # repeat guests, new guests and countries.
    get_customer_kpis,

    # Returns the distribution of bookings
    # by customer type.
    get_customer_type_distribution,

    # Returns the distribution of bookings
    # across different market segments.
    get_market_segment_distribution,

    # Returns the top countries based
    # on customer bookings.
    get_country_distribution,

    # Returns the distribution of
    # repeat and new guests.
    get_repeat_guest_distribution

)

# Create a Blueprint for all
# Customer Analytics routes.
customer_bp = Blueprint(

    "customer",

    __name__

)


# Route to display the
# Customer Analytics Dashboard.
@customer_bp.route("/customer")
def customer():

    # Render the customer dashboard template
    # with all required analytical datasets.
    return render_template(

        "customer.html",

        # KPI summary cards
        kpis=get_customer_kpis(),

        # Customer type distribution chart
        customer_types=get_customer_type_distribution(),

        # Market segment distribution chart
        market_segments=get_market_segment_distribution(),

        # Top customer countries chart
        countries=get_country_distribution(),

        # Repeat guest analysis chart
        repeat_guests=get_repeat_guest_distribution()

    )