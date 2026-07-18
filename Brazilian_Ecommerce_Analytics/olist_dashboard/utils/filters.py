import pandas as pd
from utils.data_loader import master_df

def apply_filters(
    df,
    start_date=None,
    end_date=None,
    customer_state=None,
    seller_state=None,
    category=None,
    payment_type=None,
):
    """
    Apply all selected filters to the dataframe.

    Parameters
    ----------
    df : pandas.DataFrame
        Master dataframe

    Returns
    -------
    pandas.DataFrame
    """

    filtered = df.copy()

    # ----------------------------
    # Date Range
    # ----------------------------

    if start_date:
        filtered = filtered[
            filtered["order_purchase_timestamp"] >= pd.to_datetime(start_date)
        ]

    if end_date:
        filtered = filtered[
            filtered["order_purchase_timestamp"] <= pd.to_datetime(end_date)
        ]

    # ----------------------------
    # Customer State
    # ----------------------------

    if customer_state:
        if customer_state:
            filtered = filtered[
                filtered["customer_state"].str.upper() == customer_state.upper()
            ]
            print(customer_state)

            print(master_df["customer_state"].unique())

    # ----------------------------
    # Seller State
    # ----------------------------

    if seller_state:
        filtered = filtered[
            filtered["seller_state"] == seller_state
        ]

    # ----------------------------
    # Product Category
    # ----------------------------

    if category:
        filtered = filtered[
            filtered["product_category_name_english"] == category
        ]

    # ----------------------------
    # Payment Method
    # ----------------------------

    if payment_type:
        filtered = filtered[
            filtered["payment_type"] == payment_type
        ]

    return filtered