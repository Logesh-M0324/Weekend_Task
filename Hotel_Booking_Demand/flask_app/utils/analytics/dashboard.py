from utils.loader import load_data

df = load_data()


def get_dashboard_kpis():

    return {

        "total_bookings": len(df),

        "cancellation_rate": round(
            df["is_canceled"].mean() * 100,
            2
        ),

        "average_adr": round(
            df["average_daily_rate"].mean(),
            2
        ),

        "average_stay": round(
            df["total_stay_duration"].mean(),
            2
        )

    }