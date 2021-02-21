from flask import Flask, render_template
from flask_script import Manager
from flask_moment import Moment

from datetime import datetime




from app import app

from app.models import *
from app.appconfig import *
#from app.dbop import createdbtable



# Home Page
@app.route('/')
def home():
    pageName = '/'
    #createdbtable = createdbtable()
    class createdbtable():
        cur = mysql.connection.cursor()
        cur.execute(
        ''' 
        CREATE TABLE IF NOT EXISTS employees ( 
	id INT(50) NOT NULL AUTO_INCREMENT , 
	fname VARCHAR(100) NULL DEFAULT NULL ,
	lname VARCHAR(100) NULL DEFAULT NULL ,
	dept VARCHAR(150) NULL DEFAULT NULL , 
	username VARCHAR(450) NULL DEFAULT NULL , 
	email VARCHAR(150) NULL DEFAULT NULL ,
	password VARCHAR(150) NULL DEFAULT NULL , 
	INDEX (id)) ENGINE = InnoDB;
	)
	'''
	)
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
    

# Errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html', current_time=datetime.utcnow()), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html', current_time=datetime.utcnow()), 500
