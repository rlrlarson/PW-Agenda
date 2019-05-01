# import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# create new instance
db = SQLAlchemy()

# Create class Session
class Session(db.Model):
	__tablename__ = 'sessions'
	session_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String, unique=True, nullable=False)
	speaker = db.Column(db.String, nullable=False)
	start_time = db.Column(db.String, nullable=False)
	end_time = db.Column(db.String, nullable=False)

# Create class User
class User(db.Model):
	__tablename__ = 'users'
	uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String, unique=True, nullable=False)
	password = db.Column(db.String, nullable=False)


# Create class Saved
class Saved(db.Model):
	__tablename__ = 'agenda'
	saved_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	user = db.Column(db.Integer, db.ForeignKey('users.uid'), nullable=False)
	saved_session = db.Column(db.Integer, db.ForeignKey('sessions.session_id'), nullable=False)