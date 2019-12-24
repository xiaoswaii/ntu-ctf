from flask import Flask, request, session, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:cybercyber@database/donation'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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

db.create_all()
try:
    user = User('kitten', 'notavalidpasswordhash')
    db.session.add(user)
    db.session.commit()
except:
    pass
try:
    user = User('bank', 'notavalidpasswordhash')
    db.session.add(user)
    db.session.commit()
except:
    pass

@app.route('/payment')
def payment():
    frm = request.args.get('frm')
    to = request.args.get('to')
    amount = int(request.args.get('amount'))

    print(frm, to, amount)

    frm_user = User.query.filter_by(name=frm).first()
    to_user = User.query.filter_by(name=to).first()

    print(frm_user, to_user)

    print(to_user is  not None and frm_user.name == 'bank')

    if to_user and frm_user.name == 'bank':
        #frm_user.balance -= amount JUST PRINT MORE MONEYYYYYYY!!!!!!
        to_user.balance += amount
        db.session.commit()
        return "", 200

    if frm_user and to_user and frm_user.balance >= amount:
        frm_user.balance -= amount
        to_user.balance += amount
        db.session.commit()
        return "", 200

    abort(500)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=False)
