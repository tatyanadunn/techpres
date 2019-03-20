#basic
from flask import Flask
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
auth = HTTPBasicAuth()

#define the users
users = {
    #"username": "password"
    "Tatyana": "Okay",
    "Kam": "Random"
}

# get_password is a callback function to check the password for specific user
@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

# login_required is a callback function for when authentication is successful
@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()

if __name__ == '__main__':
    app.run()
