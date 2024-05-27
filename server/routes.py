from flask import render_template, flash, redirect, url_for
from server import app
from server.forms import Registration, Login
from server.config import secret_key_config
from secrets import token_hex
from server.models import Student

secret_key_config(token_hex(16))
@app.route("/", methods = ["GET", "POST"])
@app.route("/login" , methods = ["GET", "POST"])
def home():
    student = Student.query.all()
    return str(student)
    # login = Login()
    # if login.validate_on_submit():
    #     if login.reg_no.data == "10760805fi".upper():
    #         flash("Welcome!")
    #     else:
    #         flash("Not found, register")
    return render_template("index.html", title = "Login", login = login)


@app.route("/registration", methods = ["GET", "POST"])
def register():
    form = Registration()
    if form.validate_on_submit():
        flash(f"registration successful{form.first_name.data}")
        return redirect(url_for("home"))
    return render_template("signup_form.html", title = "Registration", form = form)
