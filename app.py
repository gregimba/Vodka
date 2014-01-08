
#Vodka Imports
from flask import Flask, render_template
from pony.orm import *

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = Database('sqlite', 'db.sqlite',create_db=True)

#Blueprint imports
from controllers.page import index
app.register_blueprint(index)

if __name__ == '__main__':
	app.run()
