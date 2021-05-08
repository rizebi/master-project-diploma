# Form Based Imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

# User Based Imports
from flask_login import current_user
from carplanner.models import User




class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired(message = "Introduceti mailul"), Email(message = "Mail invalid")], render_kw={"placeholder": "Email*"})
    parola = PasswordField(validators=[DataRequired(message = "Introduceti parola")], render_kw={"placeholder": "Parola*"})
    submit = SubmitField("Log In")

class ForgotForm(FlaskForm):
    email = StringField(validators=[DataRequired(message = "Introduceti mailul"), Email(message = "Mail invalid")], render_kw={"placeholder": "Email*"})
    submit = SubmitField("Reseteaza parola")

class RegistrationForm(FlaskForm):
    email = StringField(validators=[DataRequired(message = "Introduceti mailul"),Email(message = "Mail invalid")], render_kw={"placeholder": "Email*"})
    numeUser = StringField(render_kw={"placeholder": "Nume"})
    prenumeUser = StringField(render_kw={"placeholder": "Prenume"})
    numeCompanie = StringField(render_kw={"placeholder": "Nume Companie"})
    parola = PasswordField(validators=[DataRequired(message = "Introduceti parola"), EqualTo('parolaConfirm', message='Parolele sunt diferite!')], render_kw={"placeholder": "Parola*"})
    parolaConfirm = PasswordField(validators=[DataRequired(message = "Reintroduceti parola pentru confirmare")], render_kw={"placeholder": "Confirmare Parola*"})
    submit = SubmitField('Inregistrare!')

    def validate_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('Acest email este deja folosit!')
        if (len(str(field.data))) > 29:
          raise ValidationError('Mailul introdus este prea lung')

    def validate_numeUser(self, field):
        if (len(str(field.data))) > 29:
          raise ValidationError('Numele introdus este prea lung')

    def validate_prenumeUser(self, field):
        if (len(str(field.data))) > 29:
          raise ValidationError('Prenumele introdus este prea lung')

    def validate_numeCompanie(self, field):
        if (len(str(field.data))) > 29:
          raise ValidationError('Numele companiei introduse este prea lung')

class UpdateUserForm(FlaskForm):
    email = StringField(validators=[DataRequired(message = "Introduceti mailul"),Email(message = "Mail invalid")], render_kw={"placeholder": "Email"})
    numeUser = StringField(render_kw={"placeholder": "Nume"})
    prenumeUser = StringField(render_kw={"placeholder": "Prenume"})
    numeCompanie = StringField(render_kw={"placeholder": "Nume Companie"})
    picture = FileField('Incarca fotografie de profil', validators=[FileAllowed(['jpg', 'png'])])
    parola = PasswordField(validators=[EqualTo('parolaConfirm', message='Parolele sunt diferite!')], render_kw={"placeholder": "Parola"})
    parolaConfirm = PasswordField(render_kw={"placeholder": "Confirmare Parola"})
    submit = SubmitField('Actualizeaza')

    def validate_email(self, field):
        # Check if not None for that user email!
        if field.data != current_user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('Acest email este deja folosit!')

    def validate_numeUser(self, field):
        if (len(str(field.data))) > 29:
          raise ValidationError('Numele introdus este prea lung')

    def validate_prenumeUser(self, field):
        if (len(str(field.data))) > 29:
          raise ValidationError('Prenumele introdus este prea lung')

    def validate_numeCompanie(self, field):
        if (len(str(field.data))) > 29:
          raise ValidationError('Numele companiei introduse este prea lung')
