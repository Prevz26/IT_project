from flask import Flask

def create_app():
    app = Flask(__name__, template_folder="templates")
    return app

from server import routes, forms, config, models