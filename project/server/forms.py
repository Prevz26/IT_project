from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, EmailField
from wtforms.validators import DataRequired, Length, Email


class Registration(FlaskForm):
    first_name = StringField(label="FIRST NAME ", validators=[DataRequired(), Length(min=4, max=10)])
    
    last_name = StringField(label="LAST NAME", validators=[DataRequired(), Length(min=4, max=20)])
    
    reg_no = StringField(label="REG-NO", validators=[DataRequired(), Length(min=10, max=10)])
    
    department = StringField(label="DEPARTMENT", validators=[DataRequired()])
    
    faculty = StringField(label="FACULTY", validators=[DataRequired()])
    
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    
    submit = SubmitField("Submit")
    reset = SubmitField("Reset")
    
class Login(FlaskForm):
    reg_no = StringField(label="Reg Number", validators=[DataRequired(), Length(min=10, max=10)])
    
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
    
