from flask import Flask, render_template, request, json
from santa import app

@app.route('/')
def main():
    return render_template('index.html')
@app.route('/confirm', methods=['POST'])
def confirm():
    _name = request.form['idname']
    _email = request.form['idemail']
    _want = request.form['idwant']
    if _name and _email and _want:
        return json.dumps({'html':'<span> All fields inputed</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})
