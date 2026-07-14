from pathlib import Path
import pandas as pd

statistics_path = Path("/home/aximsoft/Downloads/Weekend_Task/Hotel_Booking_Demand/data/statistics")
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