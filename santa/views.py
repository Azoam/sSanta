from flask import Flask, render_template, request, json
from santa import app, db, User
from sqlalchemy.sql import select
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
import random
import smtplib
import config


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/confirm', methods=['POST'])
def confirm():
    engine = create_engine('sqlite:///test.db', echo=True)
    _name = request.form['idname'].lower()
    _email = request.form['idemail'].lower()
    _want = request.form['idwant'].lower()
    print _name
    print _email
    print _want
    if _name and _email and _want:
	if(_name == config.adminName and _email == config.adminEmail and _want == config.adminEmail):
		match()
		return render_template('fin.html')
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
        return render_template('fin.html')
    else:
        return render_template('index.html')


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
    originalKey = r[0]
    key = r[0]
    while len(r) > 0:
	r.remove(key)
        if len(r) == 0:
            break
        i = random.randint(0,(len(r)-1))
        print(i)
        tel[str(key)] = (str(r[i]))
	print str(key) + " ,  " + str(r[i]) 
	key = r[i]
    print "end"
    tel[str(key)] = str(originalKey)
    print str(key) + "  ,  " + str(originalKey)
    emailSecretSantas(tel)

def emailSecretSantas(tel):
	engine = create_engine('sqlite:///test.db',echo=True)
	conn = engine.connect()
	if(len(tel) == 1):
		return
	print("test1")
	sender = 'secretsanta@maildrop.cc'
	mail = smtplib.SMTP()
	mail.connect("smtp.gmail.com","587")
	mail.ehlo()
	mail.starttls()
	mail.ehlo()
	mail.login("ssusacs123@gmail.com", config.password)
	mail.ehlo()
	for key in tel:
		s1 = db.session.execute(
			"SELECT username FROM user WHERE email=:e",
			{'e':correctString(str(key))})
		s2 = db.session.execute(
			"SELECT username FROM user WHERE email=:e",
			{'e':correctString(str(tel[key]))})
		want = db.session.execute(
			"SELECT want FROM user WHERE email=:e",
			{'e':correctString(str(tel[key]))})
		reciever = [correctString(str(key))]
		s2 = correctString(str(s2.fetchone()))
		want = correctString(str(want.fetchone()))
		msg1 = "Hello %s!, you are going to be %s's Secret Santa! Shh don't tell anyone! %s said they would like:\n%s" %(correctString(str(s1.fetchone())).title(),s2.title(),s2.title(),want.title())
		msg = 'Subject: %s\n\n%s' % ("Secret Santa!", msg1)
		mail.sendmail(sender, reciever, msg)
	mail.quit()

def correctString(st):
	st = st.replace("u'","").replace("\'","").replace("[","").replace("]","").replace("(","").replace(")","").replace(",","").replace("{","").replace("}","")
	return st
	
		







    
