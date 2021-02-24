from flask import Flask, render_template
from flask_script import Manager
from flask_moment import Moment

from datetime import datetime




from app import app

from app import mysql

from app.models import *
from app.appconfig import mio_config, createEmployee, employeeEnrolmentTable
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
    
# About App Page

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


@app.route('/about')
def about():
    pageName = 'about'
    return render_template('about.html', pageName=pageName, current_time=datetime.utcnow())
    

# Employee Enrolment
@app.route('/enrolment', methods=['GET', 'POST'])
def renrollment():
    pageName = 'enrolment'
    dbconnect=employeeEnrolmentTable.dbConnect()
    form = enrolmentForm(request.form) #try (request.flaskForm)
    print(form)
    if request.method == "POST" and  form.validate():
        print("This form has been validated and ready for POSTING")
        fname = form.fname.data
        lname = form.lname.data 
        pnumber = form.pnumber.data 
        email = form.email.data 
        image = form.image.data 
        staff_type = form.staff_type.data 
        acct_name = form.acct_name.data 
        acct_number = form.acct_number.data 
        acct_type =form.acct_type.data 
        acct_sort_number = form.acct_sort_number.data 
        bank_name = form.bank_name.data 
        bank_branch_addr =form.bank_branch_addr.data 
        home_addr1 = form.home_addr1.data 
        home_addr2 = form.home_addr2.data 
        country = form.country.data 
        state = form.state.data 
        city = form.city.data 
        postal_zip_code = form.postal_zip_code.data
        # Creating cursor
        cur = mysql.connection.cursor()
        mysql.connection.autocommit(True) 
        #cur.execute("SELECT * FROM enrolment")
        #dbasedata = cur.fetchall()
        
        cur.execute("INSERT INTO enrolment(fname, lname, pnumber, email, image, staff_type,   \
        acct_name, acct_number, acct_type, acct_sort_number, bank_name, bank_branch_addr, \
        home_addr1, home_addr2, country, state, city, postal_zip_code)  \
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", \
         ( fname, lname, pnumber, email, image, staff_type, acct_name, acct_number, acct_type, \
          acct_sort_number, bank_name, bank_branch_addr, home_addr1, home_addr2, country, state, \
           city, postal_zip_code))

        mysql.connect.close()
        
        pass
    return render_template('enrolment.html', form=form, pageName=pageName, current_time=datetime.utcnow())
    
    
# Test Pages
@app.route('/register2')
def register2():
    pageName = 'register2'
    if request.method == 'POST':
        image_name 	= request.files['image']
        imagename 	= image_name.filename
        image 	= image_name.read() #.filename
    return render_template('register2.html', pageName=pageName, current_time=datetime.utcnow())

# Errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html', current_time=datetime.utcnow()), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html', current_time=datetime.utcnow()), 500
