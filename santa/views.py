from flask import Flask, render_template, request, json
from santa import app, db, User
from sqlalchemy.sql import select
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/confirm', methods=['POST'])
def confirm():
    engine = create_engine('sqlite:///test.db', echo=True)
    print "yo"
    print request.form['idname']
    print request.form['idemail']
    print request.form['idwant']
    _name = request.form['idname']
    _email = request.form['idemail']
    _want = request.form['idwant']
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
        if len(r) != 0:
            print "FOUND A DUP!"
        newUser = User(username=_name, email=_email, want=_want)
        db.session.add(newUser)


	db.session.commit()
    	print "yo"
        return "It worked!"
    else:
        return render_template('index.html')
