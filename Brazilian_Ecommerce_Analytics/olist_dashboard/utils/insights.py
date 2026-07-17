import pandas as pd


def safe_mean(series):

    series = series.dropna()

    if series.empty:
        return None

    return round(series.mean(), 2)

def safe_sum(series):

    series = series.dropna()

    if series.empty:
        return 0

    return round(series.sum(), 2)


def safe_max(series):

    series = series.dropna()

    if series.empty:
        return None

    return series.max()


def safe_idxmax(series):

    series = series.dropna()

    if series.empty:
        return None

    return series.idxmax()


def safe_percentage(part,total):

    if total==0:

        return 0

    return round((part/total)*100,2)


def get_dashboard_insights(df, kpis):
    """
    Generate dashboard insights safely.

    Parameters
    ----------
    df : pandas.DataFrame
        Filtered dataframe

    kpis : dict
        KPI dictionary generated from get_dashboard_kpis()

    Returns
    -------
    list[dict]
    """

    insights = []

    # ----------------------------------------------------
    # Empty dataframe
    # ----------------------------------------------------

    if df.empty:
        return [{
            "title": "No Data",
            "icon": "bi-exclamation-circle-fill",
            "text": "No records match the selected filters."
        }]

    # ----------------------------------------------------
    # Revenue
    # ----------------------------------------------------

    insights.append({
        "title": "Revenue",
        "icon": "bi-cash-stack",
        "text": f"Total revenue generated is ₹{kpis['total_revenue']:,.2f}."
    })

    # ----------------------------------------------------
    # Top Customer State
    # ----------------------------------------------------

    if (
        "customer_state" in df.columns
        and "payment_value" in df.columns
    ):

        state_sales = (
            df.groupby("customer_state")["payment_value"]
            .sum()
            .dropna()
        )

        if not state_sales.empty:

            top_state = state_sales.idxmax()
            revenue = state_sales.max()

            insights.append({
                "title": "Top State",
                "icon": "bi-geo-alt-fill",
                "text": f"{top_state} generated the highest revenue (₹{revenue:,.2f})."
            })

    # ----------------------------------------------------
    # Delivery
    # ----------------------------------------------------

    if "total_delivery_days" in df.columns:

        delivery = df["total_delivery_days"].dropna()

        if not delivery.empty:

            insights.append({
                "title": "Delivery",
                "icon": "bi-truck",
                "text": f"Average delivery time is {delivery.mean():.1f} days."
            })

    # ----------------------------------------------------
    # Review Score
    # ----------------------------------------------------

    if "review_score" in df.columns:

        reviews = df["review_score"].dropna()

        if not reviews.empty:

            insights.append({
                "title": "Customer Satisfaction",
                "icon": "bi-star-fill",
                "text": f"Average review score is {reviews.mean():.2f} / 5."
            })

    # ----------------------------------------------------
    # Repeat Customers
    # ----------------------------------------------------

    if (
        "customer_unique_id" in df.columns
        and "order_id" in df.columns
    ):

        repeat_customers = (
            df.groupby("customer_unique_id")["order_id"]
            .nunique()
        )

        if not repeat_customers.empty:

            repeat_rate = (
                (repeat_customers > 1).mean() * 100
            )

            insights.append({
                "title": "Repeat Customers",
                "icon": "bi-arrow-repeat",
                "text": f"{repeat_rate:.1f}% of customers placed more than one order."
            })

    # ----------------------------------------------------
    # Orders
    # ----------------------------------------------------

    if "order_id" in df.columns:

        total_orders = df["order_id"].nunique()

        insights.append({
            "title": "Orders",
            "icon": "bi-bag-check-fill",
            "text": f"{total_orders:,} unique orders are included in the current view."
        })

    return insights


def get_sales_insights(df, kpis):

    insights = []

    if df.empty:
        return [{
            "title": "No Data",
            "icon": "bi-exclamation-circle-fill",
            "text": "No records match the selected filters."
        }]

    insights.append({
        "title": "Revenue Summary",
        "icon": "bi-cash-stack",
        "text": (
            f"The filtered dataset generated "
            f"₹{kpis['total_revenue']:,.2f} "
            f"from {kpis['total_orders']:,} unique orders."
        )
    })

    category_sales = (
        df.groupby("product_category_name_english")["payment_value"]
        .sum()
        .dropna()
    )

    if not category_sales.empty:

        category = category_sales.idxmax()
        revenue = category_sales.max()

        insights.append({
            "title": "Top Category",
            "icon": "bi-box-seam-fill",
            "text": (
                f"{category} generated the highest revenue "
                f"(₹{revenue:,.2f})."
            )
        })

    state_sales = (
            df.groupby("customer_state")["payment_value"]
            .sum()
            .dropna()
        )

    if not state_sales.empty:

            state = state_sales.idxmax()

            revenue = state_sales.max()

            percentage = (
                revenue /
                state_sales.sum()
            ) * 100

            insights.append({
                "title": "Top State",
                "icon": "bi-geo-alt-fill",
                "text": (
                    f"{state} contributed "
                    f"{percentage:.1f}% "
                    f"of total revenue."
                )
            })

    avg_order = (
        df.groupby("order_id")["payment_value"]
        .first()
        .mean()
    )

    if pd.notna(avg_order):

        insights.append({
            "title": "Average Order Value",
            "icon": "bi-receipt",
            "text": (
                f"The average order value is "
                f"₹{avg_order:,.2f}."
            )
        })

    monthly = (
        df.groupby(
            df["order_purchase_timestamp"]
            .dt.to_period("M")
        )["payment_value"]
        .sum()
    )

    if len(monthly) >= 2:

        first = monthly.iloc[0]
        last = monthly.iloc[-1]

        change = (
            (last - first) /
            first * 100
        ) if first != 0 else 0

        insights.append({
            "title": "Revenue Trend",
            "icon": "bi-graph-up-arrow",
            "text": (
                f"Revenue changed by "
                f"{change:.1f}% "
                f"between the first and last month "
                f"of the filtered period."
            )
        })
    return insights


def get_customer_insights(df, kpis):

    insights = []

    if df.empty:

        return [{
            "title": "No Data",
            "icon": "bi-exclamation-circle-fill",
            "text": "No records match the selected filters."
        }]

    insights.append({

        "title": "Customer Base",

        "icon": "bi-people-fill",

        "text": f"There are {kpis['total_customers']:,} unique customers."

    })

    insights.append({

        "title": "Repeat Customers",

        "icon": "bi-arrow-repeat",

        "text": f"{kpis['repeat_rate']:.2f}% of customers placed multiple orders."

    })

    # ------------------------------
    # Highest Spending State
    # ------------------------------

    if (
        "customer_state" in df.columns and
        "payment_value" in df.columns
    ):

        state_sales = (

            df.groupby("customer_state")["payment_value"]

            .sum()

            .dropna()

        )

        if not state_sales.empty:

            state = state_sales.idxmax()

            revenue = state_sales.max()

            insights.append({

                "title": "Highest Spending State",

                "icon": "bi-geo-alt-fill",

                "text": f"{state} generated ₹{revenue:,.2f} in revenue."

            })

    # ------------------------------
    # Top Customer
    # ------------------------------

    if (
        "customer_unique_id" in df.columns and
        "payment_value" in df.columns
    ):

        customer_clv = (

            df.groupby("customer_unique_id")["payment_value"]

            .sum()

            .dropna()

        )

        if not customer_clv.empty:

            customer = customer_clv.idxmax()

            value = customer_clv.max()

            insights.append({

                "title": "Top Customer",

                "icon": "bi-trophy-fill",

                "text": f"Customer {customer[:8]}... spent ₹{value:,.2f}."

            })

    insights.append({

        "title": "Average Spend",

        "icon": "bi-wallet2",

        "text": f"Average customer spending is ₹{kpis['average_spend']:,.2f}."

    })

    return insights

def get_product_insights(df, kpis):
    insights = []

    if df.empty:

        return [{
            "title": "No Data",
            "icon": "bi-exclamation-circle-fill",
            "text": "No records match the selected filters."
        }]
    
    insights.append({

        "title":"Product Catalog",

        "icon":"bi-box-seam-fill",

        "text":

        f"{kpis['total_products']:,} products are available across {kpis['total_categories']} categories."

        })

    insights.append({

        "title":"Top Category",

        "icon":"bi-award-fill",

        "text":

        f"{kpis['top_category']} is the most frequently ordered category."

        })

    insights.append({

        "title":"Average Product Price",

        "icon":"bi-currency-dollar",

        "text":

        f"The average product price is ₹{kpis['avg_product_price']:,.2f}."

        })
    category_revenue = (

        df.groupby(
            "product_category_name_english"
        )["payment_value"]

        .sum()

    )
    if not category_revenue.empty:

        category = category_revenue.idxmax()

        revenue = category_revenue.max()

        insights.append({

            "title":"Revenue Leader",

            "icon":"bi-graph-up-arrow",

            "text":

            f"{category} generated ₹{revenue:,.2f} revenue."

        })

    category_rating = (

        df.groupby(
            "product_category_name_english"
        )["review_score"]

        .mean()

    )
    if not category_rating.empty:

        category = category_rating.idxmax()

        rating = category_rating.max()

        insights.append({

            "title":"Highest Rated Category",

            "icon":"bi-star-fill",

            "text":

            f"{category} has the highest rating ({rating:.2f}/5)."

        })

    return insights


def get_seller_insights(df, kpis):

    insights = []

    if df.empty:

        return [{
            "title":"No Data",
            "icon":"bi-exclamation-circle-fill",
            "text":"No records match the selected filters."
        }]

    insights.append({

        "title":"Seller Network",

        "icon":"bi-shop",

        "text":

        f"{kpis['total_sellers']:,} sellers are included in the current dataset."

    })

    insights.append({

        "title": "Best Seller",

        "icon": "bi-trophy-fill",

        "text": (
            f"Seller {str(kpis['best_seller'])[:8]}... "
            f"generated ₹{kpis['best_seller_revenue']:,.2f} in revenue."
        )

    })

    insights.append({

        "title":"Average Seller Revenue",

        "icon":"bi-cash-stack",

        "text":

        f"The average revenue per seller is ₹{kpis['average_revenue']:,.2f}."

    })

    insights.append({

        "title":"Top Seller State",

        "icon":"bi-geo-alt-fill",

        "text":

        f"{kpis['top_state']} has the largest seller network."

    })

    if (
        "seller_id" in df.columns
        and
        "review_score" in df.columns
    ):

        ratings = (
            df.groupby("seller_id")["review_score"]
            .mean()
            .dropna()
        )

        if not ratings.empty:

            seller = ratings.idxmax()

            score = ratings.max()

            insights.append({

                "title":"Highest Rated Seller",

                "icon":"bi-star-fill",

                "text":

                f"Seller {str(seller)[:8]}... has the highest average rating ({score:.2f}/5)."

            })

    return insights


def get_delivery_insights(df, kpis):

    insights = []

    if df.empty:

        return [{

            "title":"No Data",

            "icon":"bi-exclamation-circle-fill",

            "text":"No records match the selected filters."

        }]

    insights.append({

        "title":"Delivery Performance",

        "icon":"bi-truck",

        "text":

        f"{kpis['total_deliveries']:,} orders were delivered."

    })

    insights.append({

        "title":"Average Delivery Time",

        "icon":"bi-clock",

        "text":

        f"Orders took {kpis['average_delivery_days']} days on average."

    })

    insights.append({

        "title":"Fastest State",

        "icon":"bi-geo-alt-fill",

        "text":

        f"{kpis['fastest_state']} has the quickest deliveries."

    })

    insights.append({

        "title":"On-Time Deliveries",

        "icon":"bi-check-circle-fill",

        "text":

        f"{kpis['on_time_rate']}% of deliveries arrived on or before the estimated date."

    })

    insights.append({

        "title":"Average Delay",

        "icon":"bi-exclamation-triangle-fill",

        "text":

        f"Average delivery delay is {kpis['average_delay']} days."

    })

    return insights

def get_payment_insights(df, kpis):

    insights = []

    if df.empty:
        return [{
            "title": "No Data",
            "icon": "bi-exclamation-circle-fill",
            "text": "No records match the selected filters."
        }]

    insights.append({

        "title": "Payment Volume",

        "icon": "bi-cash-stack",

        "text":
        f"The filtered orders generated ₹{kpis['total_payment']:,.2f}."

    })

    insights.append({

        "title": "Preferred Payment",

        "icon": "bi-credit-card-fill",

        "text":
        f"{kpis['top_payment_method']} is the most frequently used payment method."

    })

    insights.append({

        "title": "Average Payment",

        "icon": "bi-wallet2",

        "text":
        f"The average payment amount is ₹{kpis['average_payment']:,.2f}."

    })

    insights.append({

        "title": "Installments",

        "icon": "bi-calendar-check",

        "text":
        f"Customers used up to {kpis['max_installment']} installments."

    })

    return insights 

def get_review_insights(df, kpis):

    insights = []

    if df.empty:
        return [{
            "title": "No Data",
            "icon": "bi-exclamation-circle-fill",
            "text": "No records match the selected filters."
        }]

    insights.append({

        "title": "Average Rating",

        "icon": "bi-star-fill",

        "text":
        f"The average customer rating is {kpis['average_review']:.2f}/5."

    })

    insights.append({

        "title": "Highest Rated Category",

        "icon": "bi-award-fill",

        "text":
        f"{kpis['top_category']} received the highest average customer rating."

    })

    insights.append({

        "title": "Positive Reviews",

        "icon": "bi-emoji-smile-fill",

        "text":
        f"{kpis['positive_review_rate']:.1f}% of reviews are positive."

    })

    insights.append({

        "title": "Customer Feedback",

        "icon": "bi-chat-left-text-fill",

        "text":
        f"The filtered dataset contains {kpis['total_reviews']:,} customer reviews."

    })

    return insights

def get_explorer_insights(df, kpis):

    insights = []

    if df.empty:

        return [{

            "title": "No Data",

            "icon": "bi-exclamation-circle-fill",

            "text": "No records match the selected filters."

        }]

    insights.append({

        "title": "Dataset Size",

        "icon": "bi-table",

        "text":

        f"The current filtered dataset contains {kpis['rows']:,} records and {kpis['columns']} columns."

    })

    insights.append({

        "title": "Orders",

        "icon": "bi-cart-fill",

        "text":

        f"{kpis['orders']:,} unique orders are included."

    })

    insights.append({

        "title": "Customers",

        "icon": "bi-people-fill",

        "text":

        f"{kpis['customers']:,} unique customers match the selected filters."

    })

    insights.append({

        "title": "Revenue",

        "icon": "bi-cash-stack",

        "text":

        f"The filtered dataset generated ₹{kpis['revenue']:,.2f}."

    })

    return insights