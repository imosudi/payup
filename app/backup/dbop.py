from flask_mysqldb import MySQL
from app import app

from app import mysql

from app.appconfig import *

class createdbtable():
    cur = mysql.connection.cursor()
    cur.execute(
    ''' 
    CREATE TABLE IF NOT EXISTS employees ( 
	id INT(50) NOT NULL AUTO_INCREMENT , 
	name VARCHAR(100) NULL DEFAULT NULL ,
	dept VARCHAR(150) NULL DEFAULT NULL , 
	username VARCHAR(450) NULL DEFAULT NULL , 
	email VARCHAR(150) NULL DEFAULT NULL ,
	password VARCHAR(150) NULL DEFAULT NULL , 
	INDEX (id)) ENGINE = InnoDB;
	)
	'''
	)
	
