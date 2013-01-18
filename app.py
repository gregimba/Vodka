from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import restful

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)
api = restful.Api(app)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/status")
def status():
	return render_template("status.html")

#Rest Api
class RestfulStatus(restful.Resource):
    def get(self):
        return {'status': 'good'}

api.add_resource(RestfulStatus, '/status/api')

if __name__ == '__main__':
	app.run()