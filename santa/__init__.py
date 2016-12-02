from flask import Flask
from flask_alchemy import SQLAlchemy
app=Flask(__name__)
app.config
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    want = db.Column(db.String(200), unqiue=True)

    def __init__(self, username, email, want):
        self.username = username
        self.email = email
        self.want = want

    def __repr__(self):
        return '<User %r>' % self.username
import views
