from flask import Flask, request

from flask_wtf import FlaskForm

from wtforms import Form, StringField, SubmitField, IntegerField, HiddenField, validators, BooleanField, PasswordField
from wtforms.validators import Required  
from wtforms.widgets import TextArea
from flask_wtf.file import FileField
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

import email_validator


class registrationForm(Form):
    name = StringField('Name', [validators.Length(min=5, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Email()])
    password = PasswordField('New Password', [
        validators.DataRequired(), validators.Length(min=6),
        validators.EqualTo('confirm', message='Password mismatch!')
    ])
    #file = FileField('File')
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
    #The submit button was of no effect inserting data into the table
    #submit = SubmitField('Complete Registeration')
    


class loginForm(Form):
    username = StringField( validators=[Required()])
    password = PasswordField( validators=[Required()])
    


