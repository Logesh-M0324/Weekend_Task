from flask import Blueprint, send_file
from pathlib import Path

# Create a Blueprint to manage all
# file download related routes.
downloads_bp = Blueprint(
    "downloads",
    __name__
)

# Define the project's root directory.
# This path is used to locate datasets,
# statistical reports, and generated PDFs.
BASE_DIR = Path(
    "/home/aximsoft/Downloads/Weekend_Task/Hotel_Booking_Demand"
)

# Path to the processed dataset folder.
PROCESSED = BASE_DIR / "data" / "processed"

# Path to the statistical analysis results folder.
STATISTICS = BASE_DIR / "data" / "statistics"

# Path to the generated PDF analytics report.
PDF_REPORT = BASE_DIR / "reports" / "Hotel_Booking_Analytics_Report.pdf"


# Route to download the cleaned
# hotel booking dataset.
@downloads_bp.route("/download-dataset")
def download_dataset():

    return send_file(
        PROCESSED / "final_hotel_bookings.csv",
        as_attachment=True,
        download_name="Hotel_Booking_Cleaned_Dataset.csv"
    )


# Route to download the generated
# Hotel Booking Analytics PDF report.
@downloads_bp.route("/download-pdf")
def download_pdf():

    return send_file(
        PDF_REPORT,
        as_attachment=True,
        download_name="Hotel_Booking_Analytics_Report.pdf"
    )


# Route to download the
# Normality Test summary results.
@downloads_bp.route("/download-normality")
def download_normality():

    return send_file(
        STATISTICS / "normality_summary.csv",
        as_attachment=True
    )


# Route to download the
# Variance Inflation Factor (VIF) results.
@downloads_bp.route("/download-vif")
def download_vif():

    return send_file(
        STATISTICS / "vif_results.csv",
        as_attachment=True
    )


# Route to download the
# Strong Correlation analysis results.
@downloads_bp.route("/download-correlation")
def download_correlation():

    return send_file(
        STATISTICS / "strong_correlations.csv",
        as_attachment=True
    )


# Route to download the
# Independent T-Test statistical results.
@downloads_bp.route("/download-ttest")
def download_ttest():

    return send_file(
        STATISTICS / "independent_ttest_results.csv",
        as_attachment=True
    )