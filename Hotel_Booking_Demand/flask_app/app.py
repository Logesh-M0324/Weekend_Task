from flask import Flask

from routes.home import home_bp

app = Flask(__name__)

app.config.from_pyfile("config.py")

app.register_blueprint(home_bp)

if __name__ == "__main__":

    app.run(debug=True)