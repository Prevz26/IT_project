from server.config import database_config
from server import create_app
app = create_app()
db = database_config()
db.init_app(app)


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
    






