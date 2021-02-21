from flask import Flask, render_template

from flask_bootstrap import Bootstrap

from flask_script import Manager
from flask_moment import Moment

app = Flask(__name__)



moment = Moment(app)


bootstrap = Bootstrap(app)


from app import routes
