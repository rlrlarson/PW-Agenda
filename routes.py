from flask import Flask, flash, render_template, request, url_for, redirect, jsonify, session
from models import db, Session, User, Agenda
from forms import SignupForm, LoginForm
from passlib.hash import sha256_crypt

from flask_heroku import Heroku

app = Flask(__name__)

# local postgresql or heroku postgresql 
# to deploy on heroku
# heroku = Heroku(app)

# to use locally
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pwagenda' 

db.init_app(app)
app.secret_key = "pwagenda"

# global variable for grouped sessions
grouped_sessions = []

# index route
@app.route('/')
@app.route('/index')
def index():
	sessions = Session.query.all()

	# parse out all sets of sessions for each day, for each time

	all_sessions = Session.query.order_by(Session.session_id).all()


	timeslot = all_sessions[0].start_time
	group = []

	# for item in all_sessions:
	# 	print item.start_time

	for item in all_sessions:
		if timeslot == item.start_time:
			group.append(item)
		else:
			timeslot = item.start_time
			grouped_sessions.append(group)
			group = []
			group.append(item)

	print grouped_sessions
		

 	if 'username' in session:
		session_user = User.query.filter_by(username=session['username']).first()
		return render_template('index.html', title='All Sessions', username=session_user.username, grouped_sessions=grouped_sessions)
	else:
		return render_template('index.html', title='All Sessions', sessions=sessions, grouped_sessions=grouped_sessions)

@app.route('/save/<session_id>', methods=['POST'])
def save(session_id):
	session_saved = Session.query.filter_by(session_id=session_id).first()
	# new_saved = Saved(_______)

# signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignupForm()
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		repeat_password = request.form['repeat_password']

		existing_user = User.query.filter_by(username=username).first()

		if password != repeat_password:
			flash('Passwords do not match.')
			return redirect(url_for('signup'))

		if existing_user:
			flash('The username already exists. Please pick another one.')
			return redirect(url_for('signup'))
		else:
			user = User(username=username, password=sha256_crypt.hash(password), agendas=[])
			db.session.add(user)
			db.session.commit()
			flash('Congratulations, you are now a registered user!')
			return redirect(url_for('login'))
	else:
		return render_template('signup.html', title='Signup', form=form)


# login route
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		user = User.query.filter_by(username=username).first()

		if user is None or not sha256_crypt.verify(password, user.password):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		else:
			session['username'] = username
			return redirect(url_for('index'))
	else:
		return render_template('login.html', title='Login', form=form)

# logout route
@app.route('/logout', methods=['POST'])
def logout():
	session.clear()
	return redirect(url_for('index'))

# create agenda route
@app.route('/agenda', methods=['POST'])
def agenda():
#	agenda = Saved.query.all()
	# agenda_name = request['agendaname']
	# print agenda_name
	return render_template('agenda.html', grouped_sessions=grouped_sessions)


if __name__ == "__main__":
    app.run(debug=True)