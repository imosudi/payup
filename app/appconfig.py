#from flask_mysqldb import MySQL
from app import app

from app import mysql


#Config MySQL
app.config['MYSQL_USER'] = 'miodbapp' 
app.config['MYSQL_PASSWORD'] = 'miodbapp1' 
app.config['MYSQL_HOST'] = 'mysql-20948-0.cloudclusters.net' #'204.2.63.91' 
app.config['MYSQL_DB'] = 'miodbapp' 
app.config['MYSQL_PORT'] = 20992
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mio_config=app.config

# Employee table SQL
class createEmployee():
    def createEmployeeSQL():
        create_employee = ''' 
        CREATE TABLE IF NOT EXISTS employees11 ( 
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
        return create_employee
	
    def dbConnect():
        create_employee=createEmployee.createEmployeeSQL()
        cur = mysql.connect.cursor()
        if cur:
           print(" Database Connection Successful! ")
        #print(create_employee)
        cur.execute(create_employee)
        mysql.connect.commit()
        mysql.connect.close()
