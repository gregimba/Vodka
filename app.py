from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

#Blueprint imports
from controllers.page import index
app.register_blueprint(index)

if __name__ == '__main__':
	app.run()
