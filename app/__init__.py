from flask import Flask, flash, render_template

from flask_bootstrap import Bootstrap

from flask_script import Manager
from flask_moment import Moment



from flask_mysqldb import MySQL

app = Flask(__name__)



moment = Moment(app)


bootstrap = Bootstrap(app)

mysql = MySQL(app)



from app import routes
