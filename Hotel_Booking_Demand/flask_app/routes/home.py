from flask import Blueprint, render_template

from utils.analytics.dashboard import get_dashboard_kpis

home_bp = Blueprint(

    "home",

    __name__

)


@home_bp.route("/")
def home():

    kpis = get_dashboard_kpis()

    return render_template(

        "home.html",

        kpis=kpis

    )