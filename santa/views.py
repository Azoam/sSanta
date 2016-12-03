from flask import Flask, render_template, request, json
from santa import app, db, User
from sqlalchemy.sql import select
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
import random


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/confirm', methods=['POST'])
def confirm():
    engine = create_engine('sqlite:///test.db', echo=True)
    print "yo"
    _name = request.form['idname'].lower()
    _email = request.form['idemail'].lower()
    _want = request.form['idwant'].lower()
    print _name
    print _email
    print _want
    print "yo"
    if _name and _email and _want:
    	print "yo"
        conn = engine.connect()
        print "conn worked"
        result = db.session.execute(
            "SELECT email FROM user where email=:param",
            {"param":_email}
        )
        print "Result Here:"
        print str(result)
        r = result.fetchall()
        print "r is here:"
        print str(r)
        if len(r) == 0:
            newUser = User(username=_name, email=_email, want=_want)
            db.session.add(newUser)
        else:
            return render_template('index.html')
	db.session.commit()
    	print "yo"
        match()
        return render_template('fin.html')

    else:
        return render_template('index.html')

@app.route('/match')
def match():
    engine = create_engine('sqlite:///test.db', echo=True)
    conn = engine.connect()
    result = db.session.execute(
        "SELECT email FROM user"
    )
    r = result.fetchall()
    tel = {}
    print "Testing database iteration:"
    print str(r)
    i = 0
    while len(r) > 0:
        temp = r.pop(i)
        if len(r) == 0:
            print "1 unmatched!"
            break
        i = random.randint(0,(len(r)-1))
        print(i)
        tel[str(temp)] = str(r[i])
    print "end"
    print tel
