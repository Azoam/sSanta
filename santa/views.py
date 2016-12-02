from flask import Flask, render_template, request, json
from santa import app, db, User

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/confirm', methods=['POST'])
def confirm():
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
    	user = User(username=_name, email=_email, want=_want)
    	db.session.add(user)
	db.session.commit()
    	print "yo"
        return "It worked!"
    else:
        return "Plz enter the required fields"
