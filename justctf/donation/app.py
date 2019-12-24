from flask import Flask, request, session, redirect, url_for, flash, abort, render_template, send_file
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import requests
import os
import re

app = Flask(__name__)

with open('/secret', 'rb') as f:
    app.secret_key = f.read(32)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:cybercyber@database/donation'
db = SQLAlchemy(app)

### Models ###

class User(db.Model):
    name = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.BigInteger, nullable=False)

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.balance = 0

### Endpoints ###

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            abort(403)
    return wrap

@app.route('/')
def index():
    if 'logged_in' in session:
        return redirect('home')

    return render_template('index.html', login=url_for('login'), register=url_for('register'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    user = User.query.filter_by(name=request.form.get('name', '')).first()

    if not user:
        return "Invalid username", 404

    if not check_password_hash(user.password, request.form.get('passwd', '')):
        return "Invalid password", 403

    session['name'] = user.name
    session['logged_in'] = True

    return redirect('home')


@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    return redirect('/')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    name = request.form.get('name', '')
    passwd = request.form.get('passwd', '')

    if not (name and passwd):
        abort(500)

    if not re.match("^[a-zA-Z0-9]+$", name):
        return "The username should be alphanumeric", 500

    try:
        user = User(name, generate_password_hash(passwd))
        db.session.add(user)
        db.session.commit()
    except:
        return "Username already taken", 500

    return redirect('login')


@app.route('/home')
@is_logged_in
def home():
    user = User.query.filter_by(name=session['name']).first()
    return render_template('home.html', user=user, kitten=url_for('kitten'))


@app.route('/coffee')
def coffee():
    return "Do i really look like a coffeepot??????", 418


@app.route('/donate', methods=['GET', 'POST'])
@is_logged_in
def donate():
    if request.method == 'GET':
        return redirect('home')

    user = session['name']
    to = request.form['to']
    amount = int(request.form['amount'])

    if amount < 0:
        return 'You really wont to steal money from the poor kittens 0o??!1!11!!!!!!<br><a href="/home">Back to home</a>', 500

    ret = requests.get('http://127.0.0.1:5001/payment', params="to={}&amount={}&frm={}".format(to, amount, user))

    if ret.status_code != 200:
        return 'Sorry, something went wrong<br>Please check your balance<br><a href="/home">Back to home</a>'

    message = 'Thank you for your donation<br><a href="/home">Back to home</a>'

    # Thank you for 1000 dollarrrzzzzz!!!!!!
    if to == 'kitten' and amount >= 1000:
        message = open('/app/flag.txt').read()

    return message, ret.status_code

@app.route('/kitten')
@is_logged_in
def kitten():
    return render_template('kitten.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
