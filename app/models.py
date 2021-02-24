from flask import Flask, request

from flask_wtf import FlaskForm

from wtforms import Form, StringField, SubmitField, IntegerField, HiddenField, validators, BooleanField, PasswordField, RadioField, SelectField
from wtforms.validators import Required  
from wtforms.widgets import TextArea
from flask_wtf.file import FileField
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

import email_validator
#fname lname pnumber email image staff_type acct_name acct_number acct_type acct_sort_number bank_name bank_branch_addr home_addr1 home_addr2 country state city postal_zip_code

class enrolmentForm(Form):
    fname = StringField('First Name', [validators.Length(min=5, max=50)])
    lname = StringField('Last Name', [validators.Length(min=5, max=50)])
    pnumber = StringField('Phone Number', [validators.Length(min=10, max=14)])
    email = StringField('E-mail Address', [validators.Email()])
    image = FileField()
    staff_type = RadioField('Staff Type', 
    choices=[('flexRadioDefault1','Contract'),('flexRadioDefault1','Permanent')])
    acct_name = StringField('Account Name', [validators.Length(min=8)])
    acct_number = StringField('Account Number', [validators.Length(min=10, max=14)])
    acct_type = SelectField(u'Account Type', 
    choices = [('Savings', 'Savings'), ('Current', 'Current')])
    acct_sort_number = StringField('Sorting Number', [validators.Length(min=4)])
    bank_name = StringField('Bank Name', [validators.Length(min=3, max=80)])
    bank_branch_addr = StringField('Bank Branch Address', [validators.Length(min=3, max=80)])
    home_addr1 = StringField(u'Home Address 1', 
    widget=TextArea()) #, [validators.Length(min=11, max=80), validators.DataRequired()])
    home_addr2 = StringField(u'Home Address 2', 
    widget=TextArea())#, [validators.Length(min=11, max=80)])  
    country = StringField('Country', [validators.Length(min=3, max=80)])
    state = StringField('State', [validators.Length(min=3, max=80)])  
    city = StringField('City', [validators.Length(min=3, max=80)])
    postal_zip_code = StringField('Postal/Zip Code', [validators.Length(min=3, max=80)])
    
    
    
    
    

class registrationForm(FlaskForm): #Form/FlaskForm
    fname = StringField('Firstname', [validators.Length(min=5, max=50)])
    lname = StringField('Lastname', [validators.Length(min=5, max=50)])
    dept = StringField('Department', [validators.Length(min=4, max=25)])
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
    


