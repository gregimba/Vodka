#Flask Imports
from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

#Blueprint imports
from controllers.page import page

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

app.register_blueprint(page)

if __name__ == '__main__':
	app.run()