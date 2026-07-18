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

# Create a Blueprint for the Statistics module.
# This blueprint manages routes related to statistical analysis.
statistics_bp = Blueprint(
    "statistics",
    __name__
)


# Route for the Statistics Dashboard.
# Displays statistical test results and summary metrics
# generated from the hotel booking dataset.
@statistics_bp.route("/statistics")
def statistics():

    # Render the statistics dashboard template and pass
    # all statistical analysis results.
    return render_template(

        "statistics.html",

        # KPI cards showing statistical analysis summary.
        kpis=get_statistics_kpis(),

        # Normality test results.
        normality=get_normality_results(),

        # Variance Inflation Factor (VIF) results.
        vif=get_vif_results(),

        # Strong correlation summary.
        correlation=get_correlation_results(),

        # Independent t-test results.
        ttest=get_ttest_results(),

        # Pearson correlation results.
        pearson=get_pearson_results(),

        # Spearman correlation results.
        spearman=get_spearman_results(),

        # Paired t-test results.
        paired_ttest=get_paired_ttest_results(),

        # One-way ANOVA test results.
        anova=get_anova_results(),

        # Chi-Square test results.
        chi_square=get_chi_square_results(),

        # Mann-Whitney U test results.
        mann_whitney=get_mann_whitney_results(),

        # Kruskal-Wallis test results.
        kruskal=get_kruskal_results(),

        # Final statistical decision summary.
        decision=get_decision_report()

    )