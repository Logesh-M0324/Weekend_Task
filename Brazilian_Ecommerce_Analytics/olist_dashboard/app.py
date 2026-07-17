from flask import Flask, render_template, request

from utils.analytics import (
    get_dashboard_kpis,
    get_monthly_sales,
    get_category_revenue,
    get_average_order_value,
    get_state_revenue,
    get_customer_distribution,
    get_purchase_frequency,
    get_repeat_customer_summary,
    get_top_customer_lifetime_value,
    get_best_selling_products,
    get_price_distribution,
    get_product_category_sales,
    get_product_popularity,
    get_seller_kpis,
    get_seller_locations,
    get_seller_performance,
    get_seller_revenue,
    get_delivery_kpis,
    get_delivery_status,
    get_monthly_delivery_trend,
    get_shipping_performance,
    get_installment_distribution,
    get_monthly_review_trend,
    get_payment_kpis,
    get_payment_methods,
    get_review_distribution,
    get_review_kpis,
    get_review_sentiment,
    get_dataset_preview,
    get_customer_satisfaction,
    get_review_by_category,
    get_satisfaction_kpis,
    get_filter_options,
    get_customer_kpis,
    get_product_kpis,
    get_seller_kpis,
    get_seller_delivery_performance,
    get_delivery_by_state,
    get_delivery_distribution,
    get_fastest_sellers,
    get_delivery_trend,
    get_explorer_kpis
)

from utils.data_loader import master_df

from utils.filters import apply_filters

from utils.insights import (
        get_dashboard_insights, 
        get_sales_insights, 
        get_customer_insights,
        get_product_insights,
        get_seller_insights,
        get_delivery_insights,
        get_payment_insights,
        get_review_insights,
        get_explorer_insights
    )

app = Flask(__name__)


@app.route("/")
def dashboard():

    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    customer_state = request.args.get("customer_state")
    seller_state = request.args.get("seller_state")
    category = request.args.get("category")
    payment_type = request.args.get("payment_type")

    filtered_df = apply_filters(
        master_df,
        start_date,
        end_date,
        customer_state,
        seller_state,
        category,
        payment_type
    )

    filter_options = get_filter_options()

    kpis = get_dashboard_kpis(filtered_df)

    insights = get_dashboard_insights(
        filtered_df,
        kpis
    )

    return render_template(
        "index.html",
        kpis=kpis,
        monthly_sales=get_monthly_sales(filtered_df),
        category_sales=get_category_revenue(filtered_df),
        filter_options=filter_options,
        dashboard_insights=insights
    )



@app.route("/sales")
def sales():

    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    customer_state = request.args.get("customer_state")
    seller_state = request.args.get("seller_state")
    category = request.args.get("category")
    payment_type = request.args.get("payment_type")

    filtered_df = apply_filters(
        master_df,
        start_date,
        end_date,
        customer_state,
        seller_state,
        category,
        payment_type
    )

    filter_options = get_filter_options()
    sales_kpis = get_dashboard_kpis(filtered_df)
    sales_insights = get_sales_insights(filtered_df, sales_kpis)

    return render_template(
        "sales.html",
        monthly_sales=get_monthly_sales(filtered_df),
        category_sales=get_category_revenue(filtered_df),
        state_sales=get_state_revenue(filtered_df),
        average_order_value=get_average_order_value(filtered_df),
        sales_kpis=sales_kpis,
        filter_options = filter_options,
        sales_insights=sales_insights
    )

@app.route("/customers")
def customers():

    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    customer_state = request.args.get("customer_state")
    seller_state = request.args.get("seller_state")
    category = request.args.get("category")
    payment_type = request.args.get("payment_type")

    filtered_df = apply_filters(
        master_df,
        start_date,
        end_date,
        customer_state,
        seller_state,
        category,
        payment_type
    )

    filter_options = get_filter_options()

    customer_kpis = get_customer_kpis(filtered_df)

    customer_insights = get_customer_insights(
        filtered_df,
        customer_kpis
    )

    return render_template(

        "customers.html",

        customer_distribution=get_customer_distribution(filtered_df),

        purchase_frequency=get_purchase_frequency(filtered_df),

        customer_clv=get_top_customer_lifetime_value(filtered_df),

        repeat_summary=get_repeat_customer_summary(filtered_df),

        customer_kpis=customer_kpis,

        customer_insights=customer_insights,

        filter_options=filter_options
    )

@app.route("/products")
def products():

    # -----------------------------
    # Get Filter Values
    # -----------------------------

    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    customer_state = request.args.get("customer_state")
    seller_state = request.args.get("seller_state")
    category = request.args.get("category")
    payment_type = request.args.get("payment_type")

    # -----------------------------
    # Apply Filters
    # -----------------------------

    filtered_df = apply_filters(
        master_df,
        start_date,
        end_date,
        customer_state,
        seller_state,
        category,
        payment_type
    )

    # -----------------------------
    # Filter Options
    # -----------------------------

    filter_options = get_filter_options()

    # -----------------------------
    # Product KPIs
    # -----------------------------

    product_kpis = get_product_kpis(filtered_df)

    # -----------------------------
    # Product Insights
    # -----------------------------

    product_insights = get_product_insights(
        filtered_df,
        product_kpis
    )

    # -----------------------------
    # Render Template
    # -----------------------------

    return render_template(

        "products.html",

        # Charts
        category_sales=get_product_category_sales(filtered_df),

        best_products=get_best_selling_products(filtered_df),

        price_distribution=get_price_distribution(filtered_df),

        popularity=get_product_popularity(filtered_df),

        # KPI Cards
        product_kpis=product_kpis,

        # Insights
        product_insights=product_insights,

        # Filters
        filter_options=filter_options

    )

@app.route("/sellers")
def sellers():

    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    customer_state = request.args.get("customer_state")
    seller_state = request.args.get("seller_state")
    category = request.args.get("category")
    payment_type = request.args.get("payment_type")

    filtered_df = apply_filters(
        master_df,
        start_date,
        end_date,
        customer_state,
        seller_state,
        category,
        payment_type
    )

    filter_options = get_filter_options()

    seller_kpis = get_seller_kpis(filtered_df)

    seller_insights = get_seller_insights(
        filtered_df,
        seller_kpis
    )

    return render_template(

        "sellers.html",

        seller_performance=get_seller_performance(filtered_df),

        seller_revenue=get_seller_revenue(filtered_df),

        seller_locations=get_seller_locations(filtered_df),

        delivery_performance=get_seller_delivery_performance(filtered_df),

        seller_kpis=seller_kpis,

        seller_insights=seller_insights,

        filter_options=filter_options

    )


@app.route("/delivery")
def delivery():

    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    customer_state = request.args.get("customer_state")
    seller_state = request.args.get("seller_state")
    category = request.args.get("category")
    payment_type = request.args.get("payment_type")

    filtered_df = apply_filters(
        master_df,
        start_date,
        end_date,
        customer_state,
        seller_state,
        category,
        payment_type
    )

    filter_options = get_filter_options()

    delivery_kpis = get_delivery_kpis(filtered_df)

    delivery_insights = get_delivery_insights(
        filtered_df,
        delivery_kpis
    )

    delivery_trend=get_delivery_trend(filtered_df)
    shipping_performance = get_shipping_performance(filtered_df)

    return render_template(

        "delivery.html",

        delivery_distribution=get_delivery_distribution(filtered_df),

        delivery_state=get_delivery_by_state(filtered_df),

        fastest_sellers=get_fastest_sellers(filtered_df),

        delivery_status=get_delivery_status(filtered_df),

        delivery_kpis=delivery_kpis,

        delivery_insights=delivery_insights,

        filter_options=filter_options,

        delivery_trend = delivery_trend,

        shipping_performance=shipping_performance

    )

@app.route("/payments")
def payments():

    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    customer_state = request.args.get("customer_state")
    seller_state = request.args.get("seller_state")
    category = request.args.get("category")
    payment_type = request.args.get("payment_type")

    filtered_df = apply_filters(
        master_df,
        start_date,
        end_date,
        customer_state,
        seller_state,
        category,
        payment_type
    )

    filter_options = get_filter_options()

    payment_kpis = get_payment_kpis(filtered_df)

    review_kpis = get_review_kpis(filtered_df)

    payment_insights = get_payment_insights(
        filtered_df,
        payment_kpis
    )

    review_insights = get_review_insights(
        filtered_df,
        review_kpis
    )

    return render_template(

        "payments.html",

        payment_kpis=payment_kpis,

        payment_methods=get_payment_methods(filtered_df),

        installments=get_installment_distribution(filtered_df),

        payment_insights=payment_insights,

        review_kpis=review_kpis,

        review_distribution=get_review_distribution(filtered_df),

        review_sentiment=get_review_sentiment(filtered_df),

        review_trend=get_monthly_review_trend(filtered_df),

        review_category=get_review_by_category(filtered_df),

        satisfaction=get_customer_satisfaction(filtered_df),

        review_insights=review_insights,

        filter_options=filter_options
        
    )

@app.route("/explorer")
def explorer():

    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    customer_state = request.args.get("customer_state")
    seller_state = request.args.get("seller_state")
    category = request.args.get("category")
    payment_type = request.args.get("payment_type")

    filtered_df = apply_filters(
        master_df,
        start_date,
        end_date,
        customer_state,
        seller_state,
        category,
        payment_type
    )

    filter_options = get_filter_options()

    explorer_kpis = get_explorer_kpis(filtered_df)

    explorer_insights = get_explorer_insights(
        filtered_df,
        explorer_kpis
    )

    return render_template(

        "explorer.html",

        filter_options=filter_options,

        explorer_kpis=explorer_kpis,

        explorer_insights=explorer_insights,

        preview=filtered_df.head(100).to_dict(orient="records"),

        columns=filtered_df.columns.tolist()

    )
    

if __name__ == "__main__":
    app.run(debug=True)