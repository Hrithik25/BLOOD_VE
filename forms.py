
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, validators,BooleanField,SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    NAME = StringField('Name', [validators.Length(min=1, max=50)])
    USERNAME =StringField('Username', [validators.Length(min=4, max=30)])
    EMAIL =StringField('Email', [validators.Length(min=6, max=50)])
    PASSWORD =PasswordField('Password', [
    validators.DataRequired(),validators.EqualTo('confirm',message='Password do not match')
    ])
    confirm = PasswordField('Confirm Password')
    BLOOD_GROUP =StringField('BLOOD_GROUP', [validators.Length(min=2, max=4)])
    EMAIL =StringField('Email', [validators.Length(min=6, max=50)])
    PHONE_NUMBER =StringField('PHONE_NUMBER', [validators.Length(min=10, max=50)])
    ADDRESS =StringField('ADDRESS', [validators.Length(min=2, max=200)])
    CITY = StringField('CITY',[validators.Length(min=2,max=50)])
    Submit=SubmitField('Sign Up')

class loginform(FlaskForm):
    USERNAME =StringField('Username', [validators.Length(min=4, max=30)])
    PASSWORD =PasswordField('Password', [validators.DataRequired()])
    remember=BooleanField('Remember Me')
    Submit=SubmitField('Login')

# Aricle form class
class ArticleForm(FlaskForm):
    title = StringField('Title', [validators.Length(min=1, max=500)])
    body =TextAreaField('Body', [validators.Length(min=30)])