from flask import Flask, render_template
from flask_script import Manager
from flask_moment import Moment

from datetime import datetime




from app import app

from app import mysql

from app.models import *
from app.appconfig import mio_config, createEmployee
#from app.dbop import createdbtable

#dbConnect()

# Home Page
@app.route('/', methods=['POST', 'GET'])
def home():
    pageName = '/'
    #createdbtable = createdbtable()
    #employee=createEmployee()
    #employeeQuery= createEmployee.createEmployeeSQL()
    dbconnect=createEmployee.dbConnect()
    
    return render_template('index.html', pageName=pageName, current_time=datetime.utcnow())
    

# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    pageName = 'login'
    form = loginForm(request.form)
    return render_template('login.html', pageName=pageName, form=form, current_time=datetime.utcnow())
	


#User registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    pageName = 'register'
    form = registrationForm(request.form)
    return render_template('register.html', pageName=pageName, form=form, current_time=datetime.utcnow())


# About App Page
@app.route('/about')
def about():
    pageName = 'about'
    return render_template('about.html', pageName=pageName, current_time=datetime.utcnow())
    

# Employee Enrolment
@app.route('/enrolment')
def renrollment():
    pageName = 'enrolment'
    return render_template('enrolment.html', pageName=pageName, current_time=datetime.utcnow())
    
    
# Test Pages
@app.route('/register2')
def register2():
    pageName = 'register2'
    return render_template('register2.html', pageName=pageName, current_time=datetime.utcnow())

# Errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html', current_time=datetime.utcnow()), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html', current_time=datetime.utcnow()), 500
