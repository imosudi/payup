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



