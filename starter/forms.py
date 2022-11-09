from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, BooleanField, SelectField, TextAreaField, PasswordField, ValidationError, validators
from wtforms.validators import DataRequired, Email, EqualTo
from model import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('pass_confirm', message='Passwords must match!')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Registered!')

    # def check_email(self,field):
    #     if User.query.filter_by(email=field.data).first():
    #         raise ValidationError('Your email has already been registered')

    # def check_username(self,field):
    #     if User.query.filter_by(username=field.data).first():
    #         raise ValidationError('Username is taken')