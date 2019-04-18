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

