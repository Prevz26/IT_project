from server.models import Student, db

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
    return None

def check_if_student_exist(reg_no:str):
    if Student.query.filter_by(reg_no=reg_no).first():
        return True
    return False

if __name__ == "__main__":
    print (check_if_student_exist("10760805fi"))