from flask import render_template, request, Blueprint
#from carplanner.models import BlogPost


core = Blueprint('core',__name__)

@core.route('/')
def index():
    return render_template('index.html')

@core.route('/despre')
def despre():
    return render_template('despre.html')

@core.route('/tarife')
def tarife():
    return render_template('tarife.html')

@core.route('/contact')
def contact():
    return render_template('contact.html')
