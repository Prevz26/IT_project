#imports 
from server import app
from server.config import database_config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

#setting up the database configuration
app.config.update(database_config())

#creating an instance of the flask sqlalchemy and passing the flask application to it
db = SQLAlchemy()
db.init_app(app)


#Database Model  
class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    reg_no = db.Column(db.String(50), unique = True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    faculty = db.Column(db.String(50), nullable=False)
    
    def __repr__(self) -> str:
        """
        Returns a string representation of the object.

        :return: A string containing the first name, last name, registration number, email, department, and faculty of the object.
        :rtype: str
        """
        return f"{self.first_name} {self.last_name} {self.reg_no} {self.email} {self.department} {self.faculty}"








