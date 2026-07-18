import pandas as pd
from config import EXPORT_FOLDER

master_df = pd.read_csv(
    f"{EXPORT_FOLDER}/final_clean_dataset.csv",
    parse_dates=[
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]
)

kpi_df = pd.read_csv(
    f"{EXPORT_FOLDER}/kpi_summary.csv"
)

quality_df = pd.read_csv(
    f"{EXPORT_FOLDER}/data_quality_report.csv"
)