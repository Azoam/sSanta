from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
db = SQLAlchemy(app)

print "Hello"
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique = False)
    email = db.Column(db.String(120), unique = True)
    want = db.Column(db.String(120), unique = False)

    def __init__(self, username, email, want):
        self.username = username
        self.email = email
        self.want = want

    def __repr__(self):
        return '<User %r>' % self.username
import views
