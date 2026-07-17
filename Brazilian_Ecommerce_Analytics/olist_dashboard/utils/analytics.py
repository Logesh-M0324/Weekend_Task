from utils.data_loader import master_df
import pandas as pd

def get_dashboard_kpis(df):
    """Return key business metrics for the dashboard."""

    total_revenue = round(
        df.groupby("order_id")["total_order_value"].first().sum(),
        2
    )

    total_orders = df["order_id"].nunique()

    total_customers = df["customer_unique_id"].nunique()

    total_sellers = df["seller_id"].nunique()

    return {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "total_customers": total_customers,
        "total_sellers": total_sellers
    }

# Add Monthly Sales Function

def get_monthly_sales(df):

    monthly_sales = (
        df
        .groupby(
            df["order_purchase_timestamp"].dt.to_period("M")
        )["total_order_value"]
        .sum()
    )

    return {
        "labels": monthly_sales.index.astype(str).tolist(),
        "values": monthly_sales.values.tolist()
    }

# Add Revenue by Category

def get_category_revenue(df):

    category = (
        df
        .groupby("product_category_name_english")
        ["total_order_value"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    return {
        "labels": category.index.tolist(),
        "values": category.values.tolist()
    }

# add analytics function

def get_state_revenue(df):

    revenue = (
        df
        .groupby("customer_state")
        ["total_order_value"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    return {
        "labels": revenue.index.tolist(),
        "values": revenue.values.tolist()
    }


def get_average_order_value(df):

    return round(
        df
        .groupby("order_id")["total_order_value"]
        .first()
        .mean(),
        2
    )

# Customer Distribution by State

def get_customer_distribution(df):

    customer_distribution = (
        df.groupby("customer_state")
        ["customer_unique_id"]
        .nunique()
        .sort_values(ascending=False)
    )

    return {
        "labels": customer_distribution.index.tolist(),
        "values": customer_distribution.values.tolist()
    }

# Purchase Frequency

def get_purchase_frequency(df):

    purchase_frequency = (
        df.groupby("customer_unique_id")
        ["order_id"]
        .nunique()
        .value_counts()
        .sort_index()
    )

    return {
        "labels": purchase_frequency.index.astype(str).tolist(),
        "values": purchase_frequency.values.tolist()
    }

# Customer Lifetime Value
def get_top_customer_lifetime_value(df):

    clv = (
        df.groupby("customer_unique_id")
        ["customer_lifetime_value"]
        .max()
        .sort_values(ascending=False)
        .head(10)
    )

    return {
        "labels": clv.index.tolist(),
        "values": clv.values.tolist()
    }

# Repeat Customers

def get_repeat_customer_summary(df):

    repeat = (
        df["repeat_customer"]
        .value_counts()
    )

    return {
        "labels": repeat.index.tolist(),
        "values": repeat.values.tolist()
    }

# Top Product Category

def get_product_category_sales(df):
    """
    Returns the top 10 product categories by revenue.
    """

    category_sales = (
        df.groupby("product_category_name_english")["total_order_value"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    return {
        "labels": category_sales.index.tolist(),
        "values": category_sales.values.tolist()
    }

# Best Selling Product

def get_best_selling_products(df):
    """
    Returns the top 10 products by quantity sold.
    """

    products = (
        df.groupby("product_id")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )

    return {
        "labels": products.index.tolist(),
        "values": products.values.tolist()
    }

# Product Price Distribution

def get_price_distribution(df):

    return df["price"].dropna().tolist()

# Product Popularity

def get_product_popularity(df):

    popularity = (
        df.groupby("product_category_name_english")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )

    return {
        "labels": popularity.index.tolist(),
        "values": popularity.values.tolist()
    }

# Seller revenue

def get_seller_revenue(df):

    seller_revenue = (
        df.groupby("seller_id")["total_order_value"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    return {
        "labels": seller_revenue.index.tolist(),
        "values": seller_revenue.values.tolist()
    }

# Seller Performance

def get_seller_performance(df):

    performance = (
        df
        .groupby("seller_id")
        .agg(
            revenue=("total_order_value", "sum"),
            orders=("order_id", "nunique"),
            average_review=("review_score", "mean")
        )
        .sort_values("revenue", ascending=False)
        .head(10)
    )

    return {
        "labels": performance.index.tolist(),
        "values": performance["revenue"].round(2).tolist()
    }

# seller Locations

def get_seller_locations(df):

    locations = (
        df.groupby("seller_state")["seller_id"]
        .nunique()
        .sort_values(ascending=False)
    )

    return {
        "labels": locations.index.tolist(),
        "values": locations.values.tolist()
    }

# Seller Kpi

def get_seller_kpis(df):

    seller_summary = (
        df
        .groupby("seller_id")
        .agg(
            revenue=("total_order_value", "sum"),
            review=("review_score", "mean")
        )
    )

    return {

        "total_sellers":
            df["seller_id"].nunique(),

        "average_revenue":
            round(seller_summary["revenue"].mean(), 2),

        "best_seller":
            seller_summary["revenue"].idxmax(),

        "average_score":
            round(seller_summary["review"].mean(), 2)

    }

# Delivery KPIs

def get_delivery_kpis(df):

    total_orders = df["order_id"].nunique()

    delayed_orders = (
        df[df["delivery_delay_days"] > 0]["order_id"]
        .nunique()
    )

    return {
        "average_delivery_days": round(df["total_delivery_days"].mean(), 2),
        "average_shipping_days": round(df["shipping_days"].mean(), 2),
        "on_time_rate": round(
            ((total_orders - delayed_orders) / total_orders) * 100,
            2
        ),
        "delayed_orders": delayed_orders
    }

# Monthly Delivery Trend

def get_monthly_delivery_trend(df):

    trend = (
        df
        .groupby(df["order_purchase_timestamp"].dt.to_period("M"))
        ["total_delivery_days"]
        .mean()
    )

    return {
        "labels": trend.index.astype(str).tolist(),
        "values": trend.round(2).tolist()
    }

# Shipping Performance

def get_shipping_performance(df):

    performance = (
        df
        .groupby("seller_state")["shipping_days"]
        .mean()
        .sort_values()
    )

    return {
        "labels": performance.index.tolist(),
        "values": performance.round(2).tolist()
    }

# Delivery Status

def get_delivery_status(df):

    status = (
        df["on_time_delivery"]
        .value_counts()
    )

    return {
        "labels": status.index.astype(str).tolist(),
        "values": status.tolist()
    }

# Payment KPIs

def get_payment_kpis(df):

    if df.empty:
        return {
            "total_payment": 0,
            "average_payment": 0,
            "payment_methods": 0,
            "max_installment": 0,
            "top_payment_method": "N/A"
        }

    total_payment = df["payment_value"].sum()

    average_payment = df["payment_value"].mean()

    payment_methods = df["payment_type"].nunique()

    max_installment = df["payment_installments"].max()

    payment_counts = (
        df["payment_type"]
        .value_counts()
    )

    if not payment_counts.empty:
        top_payment_method = payment_counts.idxmax()
    else:
        top_payment_method = "N/A"

    return {

        "total_payment": round(total_payment, 2),

        "average_payment": round(average_payment, 2),

        "payment_methods": payment_methods,

        "max_installment": int(max_installment),

        "top_payment_method": top_payment_method

    }

# Payment Methods

def get_payment_methods(df):

    methods = (
        df["payment_type"]
        .value_counts()
    )

    return {
        "labels": methods.index.tolist(),
        "values": methods.values.tolist()
    }

# Installment Distribution

def get_installment_distribution(df):

    installments = (
        df["payment_installments"]
        .value_counts()
        .sort_index()
    )

    return {
        "labels": installments.index.astype(str).tolist(),
        "values": installments.values.tolist()
    }

# Review KPIs

def get_review_kpis(df):

    if df.empty:
        return {
            "average_review": 0,
            "highest_review": 0,
            "lowest_review": 0,
            "total_reviews": 0,
            "positive_review_rate": 0,
            "top_category": "N/A"
        }

    average_review = df["review_score"].mean()

    highest_review = df["review_score"].max()

    lowest_review = df["review_score"].min()

    total_reviews = df["review_score"].count()

    positive_review_rate = (
        (df["review_score"] >= 4).mean() * 100
    )

    category_rating = (
        df.groupby("product_category_name_english")["review_score"]
        .mean()
        .dropna()
    )

    if not category_rating.empty:
        top_category = category_rating.idxmax()
    else:
        top_category = "N/A"

    return {

        "average_review": round(average_review, 2),

        "highest_review": int(highest_review),

        "lowest_review": int(lowest_review),

        "total_reviews": int(total_reviews),

        "positive_review_rate": round(positive_review_rate, 2),

        "top_category": top_category

    }

# Review Distribution

def get_review_distribution(df):

    reviews = (
        df["review_score"]
        .value_counts()
        .sort_index()
    )

    return {
        "labels": reviews.index.astype(str).tolist(),
        "values": reviews.values.tolist()
    }

# Positive vs Negative Reviews

def get_review_sentiment(df):

    sentiment = df["review_score"].apply(
        lambda x: "Positive" if x >= 4 else "Negative"
    )

    summary = sentiment.value_counts()

    return {
        "labels": summary.index.tolist(),
        "values": summary.values.tolist()
    }


# Monthly Review Trend

def get_monthly_review_trend(df):

    trend = (
        df.groupby(
            df["order_purchase_timestamp"].dt.to_period("M")
        )["review_score"]
        .mean()
    )

    return {
        "labels": trend.index.astype(str).tolist(),
        "values": trend.round(2).tolist()
    }

def get_explorer_kpis(df):

    if df.empty:
        return {

            "rows": 0,

            "columns": 0,

            "customers": 0,

            "orders": 0,

            "revenue": 0

        }

    return {

        "rows": len(df),

        "columns": len(df.columns),

        "customers": df["customer_unique_id"].nunique(),

        "orders": df["order_id"].nunique(),

        "revenue": round(df["payment_value"].sum(), 2)

    }

def get_dataset_preview(rows=1000):
    """
    Returns the first N rows of the master dataset
    for display in the Dataset Explorer.
    """

    preview = df.head(rows)

    return {
        "columns": preview.columns.tolist(),
        "rows": preview.fillna("").values.tolist()
    }

def get_customer_satisfaction(df):

    positive = (df["review_score"] >= 4).sum()

    neutral = (df["review_score"] == 3).sum()

    negative = (df["review_score"] <= 2).sum()

    return {

        "labels": [
            "Satisfied",
            "Neutral",
            "Unsatisfied"
        ],

        "values": [
            int(positive),
            int(neutral),
            int(negative)
        ]

    }

def get_satisfaction_kpis(df):

    total = len(df)

    satisfied = (
        df["review_score"] >= 4
    ).sum()

    unsatisfied = (
        df["review_score"] <= 2
    ).sum()

    return {

        "satisfaction_rate":
            round((satisfied / total) * 100, 2),

        "positive_reviews":
            int(satisfied),

        "negative_reviews":
            int(unsatisfied)

    }

def get_review_by_category(df):

    review = (

        df

        .groupby(
            "product_category_name_english"
        )["review_score"]

        .mean()

        .sort_values(
            ascending=False
        )

        .head(10)

    )

    return {

        "labels":
            review.index.tolist(),

        "values":
            review.round(2).tolist()

    }

def get_filter_options():

    return {

        "customer_states": sorted(
            master_df["customer_state"]
            .dropna()
            .unique()
            .tolist()
        ),

        "seller_states": sorted(
            master_df["seller_state"]
            .dropna()
            .unique()
            .tolist()
        ),

        "categories": sorted(
            master_df["product_category_name_english"]
            .dropna()
            .unique()
            .tolist()
        ),

        "payment_types": sorted(
            master_df["payment_type"]
            .dropna()
            .unique()
            .tolist()
        )

    }

def get_customer_kpis(df):

    total_customers = df["customer_unique_id"].nunique()

    orders_per_customer = (
        df.groupby("customer_unique_id")["order_id"]
        .nunique()
    )

    repeat_customers = (orders_per_customer > 1).sum()

    repeat_rate = (
        repeat_customers / total_customers * 100
        if total_customers else 0
    )

    customer_revenue = (
        df.groupby("customer_unique_id")["payment_value"]
        .sum()
    )

    average_spend = customer_revenue.mean()

    average_orders = orders_per_customer.mean()

    return {

        "total_customers": total_customers,

        "repeat_customers": repeat_customers,

        "repeat_rate": round(repeat_rate,2),

        "average_spend": round(average_spend,2),

        "average_orders": round(average_orders,2)

    }

def get_product_kpis(df):

    total_products = df["product_id"].nunique()

    total_categories = (
        df["product_category_name_english"]
        .nunique()
    )

    avg_product_price = (
        df["price"]
        .mean()
    )

    category_orders = (
        df.groupby("product_category_name_english")["order_id"]
        .nunique()
    )

    top_category = (
        category_orders.idxmax()
        if not category_orders.empty
        else "N/A"
    )

    top_product_orders = (
        df.groupby("product_id")["order_id"]
        .nunique()
        .max()
    )

    return {

        "total_products": total_products,

        "total_categories": total_categories,

        "avg_product_price": round(avg_product_price,2),

        "top_category": top_category,

        "top_product_orders": int(top_product_orders)
        if pd.notna(top_product_orders)
        else 0
    }


def get_seller_kpis(df):

    if df.empty:
        return {
            "total_sellers": 0,
            "best_seller": "N/A",
            "best_seller_revenue": 0,
            "average_revenue": 0,
            "average_rating": 0,
            "average_orders": 0,
            "top_state": "N/A"
        }

    total_sellers = df["seller_id"].nunique()

    # Revenue by seller
    seller_revenue = (
        df.groupby("seller_id")["payment_value"]
        .sum()
        .dropna()
    )

    if not seller_revenue.empty:

        best_seller = seller_revenue.idxmax()
        best_seller_revenue = seller_revenue.max()
        average_revenue = seller_revenue.mean()

    else:

        best_seller = "N/A"
        best_seller_revenue = 0
        average_revenue = 0

    # Average Rating
    seller_rating = (
        df.groupby("seller_id")["review_score"]
        .mean()
        .dropna()
    )

    average_rating = (
        seller_rating.mean()
        if not seller_rating.empty
        else 0
    )

    # Orders per Seller
    seller_orders = (
        df.groupby("seller_id")["order_id"]
        .nunique()
    )

    average_orders = (
        seller_orders.mean()
        if not seller_orders.empty
        else 0
    )

    # Seller State
    seller_state = (
        df.groupby("seller_state")["seller_id"]
        .nunique()
        .dropna()
    )

    top_state = (
        seller_state.idxmax()
        if not seller_state.empty
        else "N/A"
    )

    return {

        "total_sellers": total_sellers,

        "best_seller": best_seller,

        "best_seller_revenue": round(best_seller_revenue, 2),

        "average_revenue": round(average_revenue, 2),

        "average_rating": round(average_rating, 2),

        "average_orders": round(average_orders, 2),

        "top_state": top_state

    }

def get_seller_delivery_performance(df):

    delivery = (

        df.groupby("seller_id")["total_delivery_days"]

        .mean()

        .sort_values()

        .head(10)

    )

    return {

        "labels": delivery.index.tolist(),

        "values": delivery.values.tolist()

    }

def get_delivery_kpis(df):

    if df.empty:
        return {
            "total_deliveries": 0,
            "average_delivery_days": 0,
            "average_shipping_days": 0,
            "fastest_state": "N/A",
            "on_time_rate": 0,
            "average_delay": 0,
            "delayed_orders": 0
        }

    total_deliveries = df["order_id"].nunique()

    average_delivery_days = (
        df["total_delivery_days"]
        .mean()
    )

    average_shipping_days = (
        df["shipping_days"]
        .mean()
        if "shipping_days" in df.columns
        else 0
    )


    # Fastest customer state
    state_delivery = (
        df.groupby("customer_state")["total_delivery_days"]
        .mean()
        .dropna()
    )

    fastest_state = (
        state_delivery.idxmin()
        if not state_delivery.empty
        else "N/A"
    )

    # Delivered on or before estimated date
    on_time = (
        df["order_delivered_customer_date"]
        <= df["order_estimated_delivery_date"]
    )

    on_time_rate = (
        on_time.mean() * 100
        if len(on_time) else 0
    )

    # Delay (positive means late)
    delay_days = (
        df["order_delivered_customer_date"]
        -
        df["order_estimated_delivery_date"]
    ).dt.days

    average_delay = (
        delay_days.mean()
        if not delay_days.empty
        else 0
    )

    delayed_orders = (
        delay_days > 0
    ).sum()


    return {

        "total_deliveries": total_deliveries,

        "average_delivery_days": round(average_delivery_days,2),

        "average_shipping_days": round(average_shipping_days, 2),

        "fastest_state": fastest_state,

        "on_time_rate": round(on_time_rate,2),

        "average_delay": round(average_delay,2),

        "delayed_orders": int(delayed_orders)

    }

def get_delivery_distribution(df):

    delivery = (
        df["total_delivery_days"]
        .dropna()
    )

    counts = (
        delivery.value_counts()
        .sort_index()
    )

    return {

        "labels": counts.index.astype(str).tolist(),

        "values": counts.values.tolist()

    }

def get_delivery_by_state(df):

    state = (

        df.groupby("customer_state")["total_delivery_days"]

        .mean()

        .sort_values()

    )

    return {

        "labels": state.index.tolist(),

        "values": state.values.round(2).tolist()

    }


def get_fastest_sellers(df):

    sellers = (

        df.groupby("seller_id")["total_delivery_days"]

        .mean()

        .sort_values()

        .head(10)

    )

    return {

        "labels": sellers.index.tolist(),

        "values": sellers.values.round(2).tolist()

    }

def get_delivery_status(df):

    on_time = (
        df["order_delivered_customer_date"]
        <=
        df["order_estimated_delivery_date"]
    )

    return {

        "labels": [

            "On Time",

            "Late"

        ],

        "values": [

            int(on_time.sum()),

            int((~on_time).sum())

        ]

    }

def get_delivery_trend(df):

    trend = (
        df.groupby(
            df["order_purchase_timestamp"]
            .dt.to_period("M")
        )["total_delivery_days"]
        .mean()
    )

    return {

        "labels": trend.index.astype(str).tolist(),

        "values": trend.values.round(2).tolist()

    }