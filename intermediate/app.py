##app.py##

from flask import Flask, render_template
from flask_httpauth import HTTPDigestAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key here'
auth = HTTPDigestAuth()

users = {
    #"username": "password"
    "money": "bags",
    "wow": "wowza",
    "Tatyana": "word"
}

@app.route('/')
def index():
    return render_template('index.html')

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/another')
@auth.login_required
def another():
    return "Hello, %s!" % auth.username()

@app.route('/welcome')
@auth.login_required
def welcome():
    return render_template('welcome.html')

@app.route('/public')
def public():
    return render_template('public.html')
#can create more routes here

@app.route('/private')
@auth.login_required
def private():
    return render_template('private.html')

@app.route('/logout')
def logout():
        return "Logout", 401

if __name__ == '__main__':
    app.run()
