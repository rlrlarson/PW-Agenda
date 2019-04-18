from flask import Flask, flash, render_template, request, url_for, redirect, jsonify, session
from models import db, Session #, Favorite
# from forms import SignupForm, LoginForm
# from passlib.hash import sha256_crypt

from flask_heroku import Heroku

app = Flask(__name__)

# local postgresql or heroku postgresql 
# to deploy on heroku
# heroku = Heroku(app)

# to use locally
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pwagenda' 

db.init_app(app)
app.secret_key = "pwagenda"

# index route
@app.route('/')
@app.route('/index')
def index():
	print "in index route"
	sessions = Session.query.all()
	return render_template('index.html', title='All Sessions', sessions=sessions)


if __name__ == "__main__":
    app.run(debug=True)