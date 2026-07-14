from pathlib import Path
import pandas as pd

statistics_path = Path("E:\Weekend_Task\Hotel_Booking_Demand\data\statistics")
print(statistics_path)

def load_csv(file_name):
    return pd.read_csv(statistics_path / file_name)


def get_statistics_kpis():

    normality = load_csv("normality_summary.csv")
    vif = load_csv("vif_summary.csv")
    correlation = load_csv("correlation_summary.csv")
    ttest = load_csv("independent_ttest_results.csv")

    return {

        "normality_tests": len(normality),

        "vif_variables": len(vif),

        "correlations": len(correlation),

        "hypothesis_tests": len(ttest)

    }


def get_normality_results():
    return load_csv("normality_summary.csv")


def get_vif_results():
    return load_csv("vif_results.csv")


def get_correlation_results():
    return load_csv("strong_correlations.csv")


def get_ttest_results():
    return load_csv("independent_ttest_results.csv")

def get_pearson_results():
    return load_csv("pearson_correlation_results.csv")


def get_spearman_results():
    return load_csv("spearman_correlation_results.csv")

def get_paired_ttest_results():
    return load_csv("paired_ttest_results.csv")


def get_anova_results():
    return load_csv("anova_test_results.csv")


def get_chi_square_results():
    return load_csv("chi_square_results.csv")


def get_mann_whitney_results():
    return load_csv("mann_whitney_results.csv")


def get_kruskal_results():
    return load_csv("kruskal_results.csv")

def get_decision_report():

    normality = load_csv("normality_summary.csv")
    vif = load_csv("vif_results.csv")
    correlation = load_csv("strong_correlations.csv")
    ttest = load_csv("independent_ttest_results.csv")

    max_vif = round(vif["VIF"].fillna(0).max(), 2)

    return {

        "normality": normality.iloc[0]["Decision"],

        "max_vif": max_vif,

        "strong_correlations": len(correlation),

        "t_statistic": round(
            float(ttest.loc[ttest["Statistic"] == "T Statistic", "Value"].iloc[0]),
            2
        ),

        "p_value": float(
            ttest.loc[ttest["Statistic"] == "P-value", "Value"].iloc[0]
        )

    }