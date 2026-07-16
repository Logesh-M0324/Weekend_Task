from flask import Flask

# Import all Blueprint objects from the routes package.
# Each Blueprint represents a separate module of the application.
from routes.home import home_bp
from routes.booking import booking_bp
from routes.customer import customer_bp
from routes.cancellation import cancellation_bp
from routes.revenue import revenue_bp
from routes.statistics import statistics_bp
from routes.reports import reports_bp
from routes.report_download import report_download
from routes.explorer import explorer_bp
from routes.downloads import downloads_bp

# Create the main Flask application instance.
app = Flask(__name__)

# Load application configuration variables from config.py.
# This includes settings such as secret keys, file paths, and other project configurations.
app.config.from_pyfile("config.py")

# Register the Home dashboard Blueprint.
# This provides the application's landing page and executive dashboard.
app.register_blueprint(home_bp)

# Register the Booking Analytics Blueprint.
# Handles booking trends, booking KPIs, and booking-related charts.
app.register_blueprint(booking_bp)

# Register the Customer Analytics Blueprint.
# Displays customer distribution, repeat guests, countries, and customer insights.
app.register_blueprint(customer_bp)

# Register the Cancellation Analytics Blueprint.
# Provides cancellation statistics, cancellation charts, and cancellation KPIs.
app.register_blueprint(cancellation_bp)

# Register the Revenue Analytics Blueprint.
# Displays ADR analysis, revenue metrics, and revenue visualizations.
app.register_blueprint(revenue_bp)

# Register the Statistical Analysis Blueprint.
# Shows hypothesis testing results, correlation analysis, VIF analysis, and statistical summaries.
app.register_blueprint(statistics_bp)

# Register the Reports Blueprint.
# Displays report pages and report-related templates.
app.register_blueprint(reports_bp)

# Register the PDF Report Download Blueprint.
# Generates and downloads the complete analytics report in PDF format.
app.register_blueprint(report_download)

# Register the Data Explorer Blueprint.
# Allows users to browse, search, filter, sort, and paginate hotel booking records.
app.register_blueprint(explorer_bp)

# Register the Downloads Blueprint.
# Handles downloading datasets, EDA reports, and other project resources.
app.register_blueprint(downloads_bp)

# Start the Flask development server when this file is executed directly.
# Debug mode automatically reloads the server after code changes and provides detailed error messages.
if __name__ == "__main__":

    app.run(debug=True)