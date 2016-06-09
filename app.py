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

if app.debug == True:
	db = records.Database('sqlite:///development.db')
else:
	db = records.Database('sqlite:///production.db')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/login",methods=['GET','POST'])
def login():
	if request.method == 'POST':
		if request.form['USERNAME'] != app.config['USERNAME']:
			error = "you fucked up"
		elif request.form['PASSWORD'] != app.config['PASSWORD']:
			error = "you fucked up"
		else:
			session['logged_in'] = True
			flash("you were logged in")
			redirect(url_for('index'))
		return render_template("login.html",error=error)
	else:
		return render_template("login.html")

@app.route("/logout")
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('index'))

if __name__ == "__main__":
	app.run()