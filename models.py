# import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# create new instance
db = SQLAlchemy()

# Create class Session
class Session(db.Model):
	__tablename__ = 'sessions'
	session_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	type = db.Column(db.String, nullable=False)
	title = db.Column(db.String, nullable=False)
	start_time = db.Column(db.String, nullable=False)
	end_time = db.Column(db.String, nullable=False)
	location = db.Column(db.String, nullable=False)
	status = db.Column(db.String, nullable=False)
	is_panel = db.Column(db.String, nullable=False)
	led_by = db.Column(db.String, nullable=False)
	type_nospaces = db.Column(db.String, nullable=False)


# class Session(db.Model):
# 	__tablename__ = 'sessions'
# 	session_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
# 	title = db.Column(db.String, unique=True, nullable=False)
# 	speaker = db.Column(db.String, nullable=False)
# 	start_time = db.Column(db.String, nullable=False)
# 	end_time = db.Column(db.String, nullable=False)


# Create class User
class User(db.Model):
	__tablename__ = 'users'
	uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String, unique=True, nullable=False)
	password = db.Column(db.String, nullable=False)
	agendas = db.Column(db.ARRAY(db.Integer, db.ForeignKey('agendas.aid')))

	#db.relationship('Agenda', backref='user', lazy=True)



# Create class Saved
# class Saved(db.Model):
# 	__tablename__ = 'agenda'
# 	saved_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
# 	user = db.Column(db.Integer, db.ForeignKey('users.uid'), nullable=False)
# 	saved_session = db.Column(db.Integer, db.ForeignKey('sessions.session_id'), nullable=False)

# Create class Agenda
class Agenda(db.Model):
	__tablename__ = 'agendas'
	aid = db.Column(db.Integer, primary_key=True, autoincrement=True)
	agenda_name = db.Column(db.String, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.uid'), nullable=False)
	saved_sessions = db.Column(db.ARRAY(db.Integer, db.ForeignKey('sessions.session_id')))

	# db.relationship('Session', backref='agenda', lazy=True)


# ATTN: I think the user to multiple agendas relationship is established. now onto the several sessions in several agendas
# ACK BUT go back to the just storing a list of IDs thing!

# CREATE TABLE agenda (aid serial NOT NULL PRIMARY KEY,
# name TEXT NOT NULL,
# user INT NOT NULL,
# saved_sessions INT []);


# CREATE TABLE sessions (
# session_id serial NOT NULL PRIMARY KEY,
# type TEXT NOT NULL,
# title TEXT NOT NULL,
# start_time TEXT NOT NULL,
# end_time TEXT NOT NULL,
# location TEXT NOT NULL,
# status TEXT NOT NULL.
# is_panel TEXT,
# led_by TEXT);






