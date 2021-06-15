from webapplication import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
# By inheriting the UserMixin we get access to a lot of built-in attributes
# which we will be able to call in our views!
# is_authenticated()
# is_active()
# is_anonymous()
# get_id()


# The user_loader decorator allows flask-login to load the current user
# and grab their id.

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

class User(db.Model, UserMixin):

  # Create a table in the db
  __tablename__ = 'useri'

  IDUser = db.Column(db.Integer, primary_key = True)
  numeUser = db.Column(db.String(30), nullable=False)
  prenumeUser = db.Column(db.String(30), nullable=False)
  email = db.Column(db.String(30), nullable=False)
  parola = db.Column(db.String(128))
  adresa = db.Column(db.String(30))
  shopping = db.Column(db.String(300))
  activated = db.Column(db.Boolean)
  hash = db.Column(db.String(50))

  def __init__(self, numeUser, prenumeUser, email, parola, adresa, hash):
    self.numeUser = numeUser
    self.prenumeUser = prenumeUser
    self.email = email
    self.adresa = adresa
    self.parola = generate_password_hash(parola)
    self.activated = False
    self.shopping = ""
    self.hash = hash

  def check_password(self, parola):
    # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
    return check_password_hash(self.parola, parola)

  def __repr__(self):
    return f"Nume: {self.numeUser}, Prenume: {self.prenumeUser}"

  def get_id(self):
    return (self.IDUser)



class Produs(db.Model):

  # Create a table in the db
  __tablename__ = 'produse'

  IDProdus = db.Column(db.Integer, primary_key = True)
  nume = db.Column(db.String(300), nullable=False)
  cod = db.Column(db.String(300), nullable=False)
  imagine = db.Column(db.String(300), nullable=False)
  pret = db.Column(db.Integer)

  def __init__(self, nume, cod, imagine, pret):
    self.nume = nume
    self.cod = cod
    self.imagine = imagine
    self.pret = pret

  def __repr__(self):
    return f"Nume: {self.numeProdus}, Cod: {self.cod}"