from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

@app.route("/")
def index():
	return render_template("index.html")


if __name__ == '__main__':
	app.run()