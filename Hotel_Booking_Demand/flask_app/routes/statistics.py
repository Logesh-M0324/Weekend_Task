from flask import Blueprint, render_template

from utils.analytics.statistics import (

    get_statistics_kpis,
    get_normality_results,
    get_vif_results,
    get_correlation_results,
    get_ttest_results

)

statistics_bp = Blueprint(
    "statistics",
    __name__
)


@statistics_bp.route("/statistics")
def statistics():

    return render_template(

        "statistics.html",

        kpis=get_statistics_kpis(),

        normality=get_normality_results(),

        vif=get_vif_results(),

        correlation=get_correlation_results(),

        ttest=get_ttest_results()

    )