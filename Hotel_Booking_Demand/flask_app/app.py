from flask import Flask

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

app = Flask(__name__)

app.config.from_pyfile("config.py")

app.register_blueprint(home_bp)

app.register_blueprint(booking_bp)

app.register_blueprint(customer_bp)

app.register_blueprint(cancellation_bp)

app.register_blueprint(revenue_bp)

app.register_blueprint(statistics_bp)

app.register_blueprint(reports_bp)

app.register_blueprint(explorer_bp)

app.register_blueprint(report_download)

app.register_blueprint(downloads_bp)

if __name__ == "__main__":

    app.run(debug=True)