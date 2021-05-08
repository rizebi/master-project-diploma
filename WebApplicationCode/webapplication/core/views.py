from flask import render_template, request, Blueprint
#from webapplication.models import BlogPost
from webapplication import db, app
from webapplication.models import Produs

core = Blueprint('core',__name__)

@core.route('/')
def index():
  produse = db.session.query(Produs).all()
  return render_template('index.html', produse=produse)
