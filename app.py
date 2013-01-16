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


#Rest Api
class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/api')

if __name__ == '__main__':
	app.run()