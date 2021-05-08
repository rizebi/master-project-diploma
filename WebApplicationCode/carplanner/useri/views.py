from flask import render_template, url_for, flash, redirect, request, Blueprint, abort
from flask_login import login_user, current_user, logout_user, login_required
from carplanner import db, app
from werkzeug.security import generate_password_hash,check_password_hash
from carplanner.models import User
from carplanner.useri.forms import RegistrationForm, LoginForm, UpdateUserForm, ForgotForm
import time
import hashlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

useri = Blueprint('useri', __name__)


gmail_user = 'carplannerroot@gmail.com'
gmail_password = 'samsungS3'

def sendMail(email, subject, hash, tip):

  msg = MIMEMultipart('alternative')
  msg['Subject'] = subject
  msg['From'] = gmail_user
  msg['To'] = email

  if tip == "activate":
    body = "<b>Salut " + email.split("@")[0] + "!</b><br>"
    body += "<br><br>Contul a fost creat cu succes, insa necesita activare pentru a putea fi folosit!"
    body += "<br> Pentru a il activa, acceseaza link-ul <a href='https://carplanner.ro/" + email + "/" + hash + "/activate" + "'>urmator</a></b><br><br>"
  elif tip == "forgot":
    body = "<b>Salut " + email.split("@")[0] + "!</b><br>"
    body += "<br><br>Ai solicitat resetarea parolei!"
    body += "<br> Pentru a alege o noua parola, acceseaza link-ul <a href='https://carplanner.ro/" + email + "/" + hash + "/forgot" + "'>urmator</a></b><br><br>"
    body += "<br><br>Daca nu tu ai solicitat resetarea parolei, ignora acest mail, contul tau este in siguranta"

  HTMLpart = MIMEText(body, 'html')
  msg.attach(HTMLpart)

  try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, email, msg.as_string())
    server.close()

    print('Email sent to ' + email)
  except:
    print('Something went wrong when sending email to ' + email)


@useri.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    forHash = str(form.email.data).encode('utf-8') + str(time.time()).encode('utf-8')
    hashObj = hashlib.sha1(forHash)
    hashString = str(hashObj.hexdigest())
    user = User(email=form.email.data,
                numeUser=form.numeUser.data,
                prenumeUser=form.prenumeUser.data,
                adresa=form.adresa.data,
                parola=form.parola.data,
                hash=hashString)

    db.session.add(user)
    db.session.commit()
    sendMail(form.email.data, "Activare cont carplanner.ro", hashString, "activate")
    flash('Multumim pentru inregistrare! Pentru a finaliza crearea contului, te rog verifica mailul si acceseaza link-ul de activare')
    return redirect(url_for('useri.login'))
  return render_template('register.html', form=form)


@useri.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    # Grab the user from our User Models table
    user = User.query.filter_by(email = form.email.data).first()

    # Check that the user was supplied and the password is right
    # The verify_password method comes from the User object
    # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not

    if user is not None:
      if user.activated is True and user.check_password(form.parola.data):
        #Log in the user
        login_user(user)

        # If a user was trying to visit a page that requires a login
        # flask saves that URL as 'next'.
        next = request.args.get('next')

        # So let's now check if that next exists, otherwise we'll go to
        # the welcome page.
        if next == None or not next[0]=='/':
          next = url_for('useri.userhome', email=user.email)

        return redirect(next)
      else:
        if user.activated is False:
          flash('Contul nu a fost inca activat')
        else:
          flash('Email sau parola gresita!')
    else:
      flash('Email-ul nu este gasit in baza de date!')

  return render_template('login.html', form=form)


@useri.route('/uitatparola', methods=['GET', 'POST'])
def uitatparola():
  form = ForgotForm()
  if form.validate_on_submit():

    # Grab the user from our User Models table
    user = User.query.filter_by(email=form.email.data).first()

    if user is not None:
      sendMail(user.email, "Resetare parola carplanner.ro", user.hash, "forgot")
      flash('Un mail cu link de restare a parolei a fost trimis la mailul introdus')
    else:
      flash('Nu avem in baza de date acest mail')
  return render_template('uitatparola.html', form=form)

@useri.route('/<email>/<hash>/forgot', methods=['GET', 'POST'])
def resetparola(email, hash):

  # Grab the user from our User Models table
  user = User.query.filter_by(email=email).first()

  if user is not None and hash == user.hash:
    login_user(user)
    flash("Actualizeaza-ti parola!")
    return redirect(url_for('useri.updateuser', email=email))
  else:
    flash("Nu s-a putut reseta parola. Te rugam sa accesezi din nou linkul din email!")
    return redirect(url_for('useri.updateuser', email=email))



@useri.route("/logout")
@login_required
def logout():
  logout_user()
  return redirect(url_for('core.index'))


@useri.route("/<email>/<hash>/activate", methods=['GET', 'POST'])
def activateuser(email, hash):
  form = LoginForm()

  user = User.query.filter_by(email = email).first()
  if user is not None and hash == user.hash:
    user.activated = True
    db.session.commit()
    flash("Felicitari! Contul a fost activat cu success! Te poti autentifica")
    return redirect(url_for('useri.userhome', email=email))
  else:
    flash("Nu s-a putut activa contul. Te rugam sa accesezi din nou linkul din email!")
    return redirect(url_for('useri.userhome', email=email))





@useri.route("/<email>/updateuser", methods=['GET', 'POST'])
@login_required
def updateuser(email):
  if email != current_user.email:
    # Forbidden, No Access
    abort(403)
  form = UpdateUserForm()

  if form.validate_on_submit():

    current_user.email = form.email.data
    current_user.numeUser = form.numeUser.data
    current_user.prenumeUser = form.prenumeUser.data
    current_user.adresa = form.adresa.data
    if form.parola.data:
      current_user.parola=generate_password_hash(form.parola.data)

    db.session.commit()
    flash('Datele contului au fost actualizate cu succes.')
    return redirect(url_for('useri.userhome', email=current_user.email))

  elif request.method == 'GET':
    form.email.data = current_user.email
    form.numeUser.data = current_user.numeUser
    form.prenumeUser.data = current_user.prenumeUser
    form.adresa.data = current_user.adresa

  return render_template('updateuser.html', form=form)


@useri.route("/<email>/removeuser", methods=['GET', 'POST'])
@login_required
def removeuser(email):
  if email != current_user.email:
    # Forbidden, No Access
    abort(403)
  return render_template('removeuser.html', email=email)

@useri.route("/<email>/removeuseryes", methods=['GET', 'POST'])
@login_required
def removeuseryes(email):
  if email != current_user.email:
    # Forbidden, No Access
    abort(403)

  logout_user()

  db.session.delete(user)

  db.session.commit()


  flash("Ne pare rau ca pleci! Contul tau a fost sters cu scucces")

  return render_template('index.html')



@useri.route("/<email>")
@login_required
def userhome(email):

  if email != current_user.email:
    # Forbidden, No Access
    abort(403)

  user = User.query.filter_by(email=email).first_or_404()

  if current_user.prenumeUser is None or current_user.prenumeUser == "" or current_user.prenumeUser == " ":
    nume = current_user.email.split("@")[0]
  else:
    nume = current_user.prenumeUser

  return render_template('userhome.html', user=user, nume=nume)
