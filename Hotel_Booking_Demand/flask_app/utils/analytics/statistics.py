from pathlib import Path
import pandas as pd

# Define the location where all statistical analysis
# result files are stored.
statistics_path = Path(
    "/home/aximsoft/Downloads/Weekend_Task/Hotel_Booking_Demand/data/statistics"
)

# Print the statistics directory path to verify
# that the correct folder is being accessed.
print(statistics_path)


# ---------------------------------------------------------
# Helper Function
# ---------------------------------------------------------
def load_csv(file_name):

    # Load a CSV file from the statistics folder
    # and return it as a pandas DataFrame.
    return pd.read_csv(statistics_path / file_name)


# ---------------------------------------------------------
# Statistics Dashboard KPIs
# ---------------------------------------------------------
def get_statistics_kpis():

    # Load all required statistical summary files.
    normality = load_csv("normality_summary.csv")
    vif = load_csv("vif_summary.csv")
    correlation = load_csv("correlation_summary.csv")
    ttest = load_csv("independent_ttest_results.csv")

    # Return the number of statistical analyses
    # performed in each category.
    return {

        "normality_tests": len(normality),

        "vif_variables": len(vif),

        "correlations": len(correlation),

        "hypothesis_tests": len(ttest)

    }


# ---------------------------------------------------------
# Normality Test Results
# ---------------------------------------------------------
def get_normality_results():

    # Load the summary of normality tests
    # performed on numerical variables.
    return load_csv("normality_summary.csv")


# ---------------------------------------------------------
# Variance Inflation Factor (VIF)
# ---------------------------------------------------------
def get_vif_results():

    # Load the VIF analysis used to detect
    # multicollinearity among variables.
    return load_csv("vif_results.csv")


# ---------------------------------------------------------
# Strong Correlation Results
# ---------------------------------------------------------
def get_correlation_results():

    # Load all strong Pearson correlations
    # identified during correlation analysis.
    return load_csv("strong_correlations.csv")


# ---------------------------------------------------------
# Independent t-Test Results
# ---------------------------------------------------------
def get_ttest_results():

    # Load the Independent t-Test output
    # used for comparing two independent groups.
    return load_csv("independent_ttest_results.csv")


# ---------------------------------------------------------
# Pearson Correlation Results
# ---------------------------------------------------------
def get_pearson_results():

    # Load the Pearson correlation analysis
    # between numerical variables.
    return load_csv("pearson_correlation_results.csv")


# ---------------------------------------------------------
# Spearman Correlation Results
# ---------------------------------------------------------
def get_spearman_results():

    # Load the Spearman rank correlation
    # analysis results.
    return load_csv("spearman_correlation_results.csv")


# ---------------------------------------------------------
# Paired t-Test Results
# ---------------------------------------------------------
def get_paired_ttest_results():

    # Load the paired t-Test results used
    # for comparing paired observations.
    return load_csv("paired_ttest_results.csv")


# ---------------------------------------------------------
# ANOVA Test Results
# ---------------------------------------------------------
def get_anova_results():

    # Load the ANOVA test results used
    # for comparing multiple group means.
    return load_csv("anova_test_results.csv")


# ---------------------------------------------------------
# Chi-Square Test Results
# ---------------------------------------------------------
def get_chi_square_results():

    # Load the Chi-Square test results
    # for categorical variable analysis.
    return load_csv("chi_square_results.csv")


# ---------------------------------------------------------
# Mann-Whitney U Test Results
# ---------------------------------------------------------
def get_mann_whitney_results():

    # Load the Mann-Whitney U test results
    # for non-parametric group comparison.
    return load_csv("mann_whitney_results.csv")


# ---------------------------------------------------------
# Kruskal-Wallis Test Results
# ---------------------------------------------------------
def get_kruskal_results():

    # Load the Kruskal-Wallis test results
    # for comparing multiple independent groups.
    return load_csv("kruskal_results.csv")


# ---------------------------------------------------------
# Executive Statistical Summary
# ---------------------------------------------------------
def get_decision_report():

    # Load the required statistical reports
    # used for executive-level reporting.
    normality = load_csv("normality_summary.csv")
    vif = load_csv("vif_results.csv")
    correlation = load_csv("strong_correlations.csv")
    ttest = load_csv("independent_ttest_results.csv")

    # Find the highest VIF value after replacing
    # missing values with zero.
    max_vif = round(vif["VIF"].fillna(0).max(), 2)

    # Return the key statistical findings
    # for the downloadable PDF report.
    return {

        # Decision from the normality test.
        "normality": normality.iloc[0]["Decision"],

        # Highest Variance Inflation Factor.
        "max_vif": max_vif,

        # Number of strong correlations detected.
        "strong_correlations": len(correlation),

        # Extract the Independent t-Test statistic.
        "t_statistic": round(
            float(
                ttest.loc[
                    ttest["Statistic"] == "T Statistic",
                    "Value"
                ].iloc[0]
            ),
            2
        ),

        # Extract the p-value of the Independent t-Test.
        "p_value": float(
            ttest.loc[
                ttest["Statistic"] == "P-value",
                "Value"
            ].iloc[0]
        )

    }