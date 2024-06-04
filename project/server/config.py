from server import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

def secret_key_config(secret_key:str) -> None:
    """
    Set the secret key for the Flask application.

    Parameters:
        secret_key (str): The secret key for the application to be set.

    Returns:
        None
    """

    app.config['SECRET_KEY'] = secret_key


def database_config() -> dict:
    """
    Returns a dictionary containing the configuration settings for the database.

    :return: A dictionary with the following keys:
             - "SQLALCHEMY_DATABASE_URI": The URI for the database connection.
             - "SQLALCHEMY_TRACK_MODIFICATIONS": A boolean indicating whether or not to track modifications to database objects.
    :rtype: dict
    """
    return {
        "SQLALCHEMY_DATABASE_URI": "sqlite:///student.db",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }

class Encryption:
    def __init__(self, password:str):
        self.password = password

    def password_hashing(self):
        """
        Generates a hashed password using the bcrypt algorithm.

        Parameters:
            password (str): The password to be hashed.

        Returns:
            str: The hashed password.
        """
        hashed_password = bcrypt.generate_password_hash(self.password).decode("utf-8")
        return hashed_password

    def decode_password(self, hashed_password, password):
        """
        Check if the provided password matches the hashed password.

        Parameters:
            hashed_password (str): The hashed password to compare against.
            password (str): The password to check.

        Returns:
            bool: True if the password matches the hashed password, False otherwise.
        """
        ispassword = bcrypt.check_password_hash(hashed_password, password)
        if ispassword:
            return True
        return False

if __name__ == "__main__":
    obj1 = Encryption("ojogu")
    password = (obj1.password_hashing())
    print (obj1.decode_password(password, "prevz"))

