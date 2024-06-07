from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///student.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    reg_no = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    faculty = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
         return f"{self.first_name} {self.last_name} {self.reg_no} {self.email} {self.department} {self.faculty}"

with app.app_context():
    db.create_all()
    stud1 = Student(
            first_name="precious", 
            last_name="ojogu", 
            reg_no="10760805fi", 
            email="nkangprecious26@.com", 
            department="computer science", 
            faculty="physical science")
    db.session.add(stud1)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        student = Student.query.all()
        print(student)





# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt()
# class Encryption:
#     def __init__(self, password:str):
#         self.password = password
#         # self.hashed_password  = hashed_password

#     def password_hashing(self):
#         """
#         Generates a hashed password using the bcrypt algorithm.

#         Parameters:
#             password (str): The password to be hashed.

#         Returns:
#             str: The hashed password.
#         """
#         hashed_password = bcrypt.generate_password_hash(self.password).decode("utf-8")
#         return hashed_password

#     def decode_password(self, hashed_password, password):
#         """
#         Check if the provided password matches the hashed password.

#         Parameters:
#             hashed_password (str): The hashed password to compare against.
#             password (str): The password to check.

#         Returns:
#             bool: True if the password matches the hashed password, False otherwise.
#         """
#         ispassword = bcrypt.check_password_hash(hashed_password, password)
#         if ispassword:
#             return True
#         return False

# if __name__ == "__main__":
#     obj1 = Encryption("ojogu")
#     password = (obj1.password_hashing())
#     print (obj1.decode_password(password, "prevz"))
