from flask import Blueprint, render_template

page = Blueprint('page', __name__,
                        template_folder='templates')

@page.route('/')
def show():
	return render_template("index.html")