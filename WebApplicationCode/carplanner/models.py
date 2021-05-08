from carplanner import db, login_manager
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
  imagineProfil = db.Column(db.String(50), nullable=False, default='default_profile.png')
  numeUser = db.Column(db.String(30), nullable=False)
  prenumeUser = db.Column(db.String(30), nullable=False)
  email = db.Column(db.String(30), nullable=False)
  parola = db.Column(db.String(128))
  numeCompanie = db.Column(db.String(30))
  activated = db.Column(db.Boolean)
  hash = db.Column(db.String(50))

  def __init__(self, numeUser, prenumeUser, email, parola, numeCompanie, hash):
    self.numeUser = numeUser
    self.prenumeUser = prenumeUser
    self.email = email
    self.numeCompanie = numeCompanie
    self.parola = generate_password_hash(parola)
    self.activated = False
    self.hash = hash

  def check_password(self, parola):
    # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
    return check_password_hash(self.parola, parola)

  def __repr__(self):
    return f"Nume: {self.numeUser}, Prenume: {self.prenumeUser}"

  def get_id(self):
    return (self.IDUser)