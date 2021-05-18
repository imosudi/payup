#from flask_mysqldb import MySQL
from flask import flash
from app import app

from app import mysql


#Config MySQL
app.config['MYSQL_USER'] = 'root'#'payup'#'miodbapp' 
app.config['MYSQL_PASSWORD'] = 'pa33word'#'miodbapp1' 
app.config['MYSQL_HOST'] = 'localhost'#'mysql-20948-0.cloudclusters.net' #'204.2.63.91' 
app.config['MYSQL_DB'] = 'payup'#'miodbapp' 
app.config['MYSQL_PORT'] = 3906 #20992
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SECRET_KEY'] = 'this should be very very difficult ot teg by moc.liamg@idusomi'



mio_config=app.config

# Employee table SQL
class createEmployee():
    def createEmployeeSQL():
        employee_table = ''' 
        CREATE TABLE IF NOT EXISTS employees ( 
	id INT(5) NOT NULL AUTO_INCREMENT , 
	fname VARCHAR(100) NULL DEFAULT NULL ,
	lname VARCHAR(100) NULL DEFAULT NULL ,
	dept VARCHAR(150) NULL DEFAULT NULL , 
	username VARCHAR(450) NULL DEFAULT NULL , 
	imagename VARCHAR(255) NULL DEFAULT NULL ,
	image MEDIUMBLOB NOT NULL ,
	email VARCHAR(150) NULL DEFAULT NULL ,
	password VARCHAR(150) NULL DEFAULT NULL , 
	INDEX (id)) ENGINE = InnoDB;
	)
	'''
        return employee_table
	
    def dbConnect():
        create_employee_table=createEmployee.createEmployeeSQL()
        #if mysql.connect.is_connected():
        try:
            #print("Successfully Connected to Database Server")
            cur = mysql.connect.cursor()
            #Next line for debugging only
            print("Successfully Connected to Database Server")
            #Web client database connection status notification
            flash("Successfully Connected to Database Server")
            if cur:
               print(" Database Connection Successful! ")
            #print(create_employee_)
            cur.execute(create_employee_table)
            mysql.connect.commit()
            mysql.connect.close()
        #else:
        except :
            #Next line for debugging only
            print("Can't connect to MySQL Database server")
            #Web client database connection status notification
            flash("Can't connect to MySQL Database server")
        
class employeeEnrolmentTable():
    def enrolmentSQL():
        #fname lname pnumber email image staff_type acct_name acct_number acct_type acct_sort_number bank_name bank_branch_addr home_addr1 home_addr2 country state city postal_zip_code
        employee_enrolment_table = ''' 
        CREATE TABLE IF NOT EXISTS enrolment ( 
	id INT(5) NOT NULL AUTO_INCREMENT , 
	fname VARCHAR(100) NULL DEFAULT NULL ,
	lname VARCHAR(100) NULL DEFAULT NULL ,
	pnumber VARCHAR(50) NULL DEFAULT NULL ,
	email VARCHAR(150) NULL DEFAULT NULL ,
	imagename VARCHAR(255) NULL DEFAULT NULL ,
	image MEDIUMBLOB , 
	staff_type VARCHAR(50) NULL DEFAULT NULL , 
	acct_name VARCHAR(80) NULL DEFAULT NULL ,
	acct_number INT(50) NULL DEFAULT NULL , 
	acct_type VARCHAR(100) NULL DEFAULT NULL ,
	acct_sort_number VARCHAR(80) NULL DEFAULT NULL ,
	bank_name VARCHAR(80) NULL DEFAULT NULL ,
	bank_branch_addr VARCHAR(100) NULL DEFAULT NULL ,
	home_addr1 VARCHAR(100) NULL DEFAULT NULL ,
	home_addr2 VARCHAR(100) NULL DEFAULT NULL ,
	country VARCHAR(100) NULL DEFAULT NULL ,
	state VARCHAR(100) NULL DEFAULT NULL ,
	city VARCHAR(100) NULL DEFAULT NULL ,
	postal_zip_code VARCHAR(100) NULL DEFAULT NULL ,
	timestamp TIMESTAMP,
	INDEX (id)) ENGINE = InnoDB;
	)
	'''
        return employee_enrolment_table
	
    def dbConnect():
        enrol_employee=employeeEnrolmentTable.enrolmentSQL()
        try:
            cur = mysql.connect.cursor()
            #Next line for debugging only
            print("Successfully Connected to Database Server")
            #Web client database connection status notification
            flash("Successfully Connected to Database Server")
            #print(create_employee)
            cur.execute(enrol_employee)
            mysql.connect.commit()
            mysql.connect.close()
        except:
            #Next line for debugging only
            print("Can't connect to MySQL Database server")
            #Web client database connection status notification
            flash("Can't connect to MySQL Database server")
        
#cur.execute("INSERT INTO documents(docname, docfile) VALUES(%s, %s)", (docname, docfile))
"""
form = createNoteForm(request.form)
    if request.method == "POST" and  form.validate():
        title = form.title.data
        #notebody = form.notebody.data
        body = form.body.data
        username = session['username']
        app.logger.info(username)
        
        # Creating cursor
        cur = mysql.connection.cursor()
        
        cur.execute("INSERT INTO notes(title, body, username) VALUES(%s, %s, %s)", (title, body,
        username))
        
        # Commit to Database
        mysql.connection.commit()
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
        cur.execute("INSERT INTO enrolment(fname, lname, pnumber, email, image, staff_type, \
         acct_name, acct_number, acct_type, acct_sort_number, bank_name, bank_branch_addr, \
          home_addr1, home_addr2, country, state, city, postal_zip_code) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (fname, lname, pnumber, email, image, staff_type, acct_name, acct_number, acct_type, acct_sort_number, bank_name, bank_branch_addr, home_addr1, home_addr2, country, state, city, postal_zip_code)
        #mysql.connect.commit()
        #mysql.connect.close()
"""
