from flask import Flask

from routes.home import home_bp
from routes.booking import booking_bp
from routes.customer import customer_bp
from routes.cancellation import cancellation_bp
from routes.revenue import revenue_bp
from routes.statistics import statistics_bp
from routes.reports import reports_bp

app = Flask(__name__)

app.config.from_pyfile("config.py")

app.register_blueprint(home_bp)

app.register_blueprint(booking_bp)

app.register_blueprint(customer_bp)

app.register_blueprint(cancellation_bp)

app.register_blueprint(revenue_bp)

app.register_blueprint(statistics_bp)

app.register_blueprint(reports_bp)

if __name__ == "__main__":

    app.run(debug=True)