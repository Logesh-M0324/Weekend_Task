from flask import Blueprint, render_template

from utils.analytics.statistics import (

    get_statistics_kpis,
    get_normality_results,
    get_vif_results,
    get_correlation_results,
    get_ttest_results,
    get_pearson_results,
    get_spearman_results,
    get_paired_ttest_results,
    get_anova_results,
    get_chi_square_results,
    get_mann_whitney_results,
    get_kruskal_results,
    get_decision_report

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

        ttest=get_ttest_results(),

        pearson=get_pearson_results(),

        spearman=get_spearman_results(),

        paired_ttest=get_paired_ttest_results(),

        anova=get_anova_results(),

        chi_square=get_chi_square_results(),

        mann_whitney=get_mann_whitney_results(),

        kruskal=get_kruskal_results(),

        decision=get_decision_report()

    )