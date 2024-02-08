from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField

#---------For the login page------------
class LoginForm(FlaskForm):
    email = StringField('Email')
    password = StringField('Password')


app = Flask(__name__)
app.secret_key = "we-will-win-this-next-hackathon"

@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)


if __name__ == "__main__":
    app.run(debug=True)