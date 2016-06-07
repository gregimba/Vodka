from flask import *
import records

app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

if __name__ == "__main__":
	app.run()