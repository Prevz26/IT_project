from flask import render_template, flash, redirect, url_for, request, session
from server import app
from server.forms import Registration, Login
from server.config import secret_key_config
from secrets import token_hex
from server.models import Student, db

secret_key_config(token_hex(16))

def check_if_student_exist(reg_no:str):
    return Student.query.filter_by(reg_no=reg_no).first() is not None

@app.route("/", methods = ["GET", "POST"])
@app.route("/login" , methods = ["GET", "POST"])
def home():
    form:Login = Login()
    if form.validate_on_submit():
        data = form.reg_no.data
        if check_if_student_exist(data):
            return redirect(url_for("profile"))
        else:
            return "do not exist"
    else:
        return render_template("index.html", form = form)



@app.route("/registration", methods = ["GET", "POST"])
def register():
    form:Registration = Registration()
    if form.validate_on_submit():
        student1 = Student(
            first_name=form.first_name.data, 
            last_name=form.last_name.data, 
            reg_no=form.reg_no.data, 
            email=form.email.data, 
            department=form.department.data, 
            faculty=form.faculty.data
        )
        session["first_name"] = form.first_name.data
        session["last_name"] = form.last_name.data
        session["reg_no"] = form.reg_no.data
        session["email"] = form.email.data
        session["department"] = form.department.data
        session["faculty"] = form.faculty.data
        db.session.add(student1)
        db.session.commit()
        return redirect(url_for("profiles"))
    return render_template("signup_form.html", title = "Registration", form = form)

@app.route("/profile/<name>")
def profiles(name):
    if name == session["first_name"]:
        return name