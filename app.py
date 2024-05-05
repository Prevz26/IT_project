from flask import Flask, render_template, flash, redirect, url_for
from forms import Registration, Login
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder= "templates")
app.config["SECRET_KEY"] = 'e941012ddf789c17596497c401245063'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
model = db.Model
class Student(model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    reg_no = db.Column(db.String(10), unique = True, nullable = False)
    department = db.Column(db.String(20), nullable = False)
    faculty = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)

    def __repr__(self):
        return f"Student('{self.name}', '{self.reg_no}', '{self.department}', '{self.faculty}', '{self.email}')"
@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("Database initialized.")    

@app.route("/", methods = ["GET", "POST"])
@app.route("/login" , methods = ["GET", "POST"])
def home():
    login = Login()
    if login.validate_on_submit():
        if login.reg_no.data == "10760805fi".upper():
            flash("Welcome!")
        else:
            flash("Not found, register")
    return render_template("index.html", title = "Login", login = login)


@app.route("/registration", methods = ["GET", "POST"])
def register():
    form = Registration()
    if form.validate_on_submit():
        flash(f"registration successful{form.first_name.data}")
        return redirect(url_for("home"))
    return render_template("signup_form.html", title = "Registration", form = form)

if __name__ == "__main__":
    app.run(
        debug= True
    )