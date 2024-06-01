# from project.db_management import *
# from server.utils import password_hashing, decode_password
from flask import render_template, flash, redirect, url_for, request
from server import app
from server.forms import Registration, Login
from server.config import secret_key_config
from secrets import token_hex
from server.models import db, Student

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
             return 'not register'
        # return render_template("profile.html", data = data)
    else:
        return render_template("index.html", form = form)
    # else:
    #     redirect("register")
    # return render_template("index.html", title = "Login", login = login)


@app.route("/registration", methods = ["GET", "POST"])
def register():
    form = Registration()
    if form.validate_on_submit():
        flash(f"registration successful{form.first_name.data}")
        return redirect(url_for("home"))
    return render_template("signup_form.html", title = "Registration", form = form)

@app.route("/profile/")
def profile():
    return "hello"