from server import create_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

def secret_key_config(secret_key:str):
    """
    Set the secret key for the Flask application.

    Parameters:
        secret_key (str): The secret key for the application to be set.

    Returns:
        None
    """
    app = create_app()
    app.config['SECRET_KEY'] = secret_key


def database_config():
    """
    Configure the database connection for the Flask application.

    This function sets the SQLAlchemy database URI for the Flask application.
    It uses the SQLite database file "project.db" located in the current directory.

    Parameters:
        None

    Returns:
        SQLAlchemy: An instance of the SQLAlchemy class, taking the flask instance as parameter.
    """
    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///student.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    return SQLAlchemy(app)



