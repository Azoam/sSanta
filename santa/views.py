from flask import render_template, request
from santa import app

@app.route('/')
def main():
    return render_template('index.html')
