from server.models import db, Student
from server import app

def add_student_if_not_exists(first_name:str, last_name:str, reg_no:str, email:str, department:str, faculty:str):
    """
    Adds a new student to the database if the student with the given registration number does not already exist.

    Args:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        reg_no (str): The registration number of the student.
        email (str): The email address of the student.
        department (str): The department of the student.
        faculty (str): The faculty of the student.

    Returns:
        Student or None: The newly created student object if the student with the given registration number does not exist, None otherwise.
    """
    if not Student.query.filter_by(reg_no=reg_no).first():
        student = Student(
            first_name=first_name,
            last_name=last_name,
            reg_no=reg_no,
            email=email,
            department=department,
            faculty=faculty
        )
        db.session.add(student)
        db.session.commit()
        return student
    print("exist already")

def check_if_student_exist(reg_no:str):
    if Student.query.filter_by(reg_no=reg_no).first() is not None:
        print(Student.first_name)
    else:
        print("does not exist")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
        stud1 = add_student_if_not_exists(
            first_name="precious", 
            last_name="ojogu", 
            reg_no="10760805fi", 
            email="nkangprecious26@.com", 
            department="computer science", 
            faculty="physical science"
        )

        stud2 = add_student_if_not_exists(
            first_name="caleb", 
            last_name="azunobi", 
            reg_no="12345678fi", 
            email="caleb@.com", 
            department="physics", 
            faculty="physical science",
        ) 

        reg_no = "12345678fi"
        check_if_student_exist(reg_no)
        
        #check if the are valid object
        # if stud1 or stud2:
        #     print(Student.query.all())
        # else:
        #     print("nothing")
