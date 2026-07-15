from flask import Blueprint, send_file
from pathlib import Path

downloads_bp = Blueprint(
    "downloads",
    __name__
)

BASE_DIR = Path(
    "/home/aximsoft/Downloads/Weekend_Task/Hotel_Booking_Demand"
)

PROCESSED = BASE_DIR / "data" / "processed"

STATISTICS = BASE_DIR / "data" / "statistics"

PDF_REPORT = BASE_DIR / "reports" / "Hotel_Booking_Analytics_Report.pdf"


@downloads_bp.route("/download-dataset")
def download_dataset():

    return send_file(
        PROCESSED / "final_hotel_bookings.csv",
        as_attachment=True,
        download_name="Hotel_Booking_Cleaned_Dataset.csv"
    )


@downloads_bp.route("/download-pdf")
def download_pdf():

    return send_file(
        PDF_REPORT,
        as_attachment=True,
        download_name="Hotel_Booking_Analytics_Report.pdf"
    )


@downloads_bp.route("/download-normality")
def download_normality():

    return send_file(
        STATISTICS / "normality_summary.csv",
        as_attachment=True
    )


@downloads_bp.route("/download-vif")
def download_vif():

    return send_file(
        STATISTICS / "vif_results.csv",
        as_attachment=True
    )


@downloads_bp.route("/download-correlation")
def download_correlation():

    return send_file(
        STATISTICS / "strong_correlations.csv",
        as_attachment=True
    )


@downloads_bp.route("/download-ttest")
def download_ttest():

    return send_file(
        STATISTICS / "independent_ttest_results.csv",
        as_attachment=True
    )