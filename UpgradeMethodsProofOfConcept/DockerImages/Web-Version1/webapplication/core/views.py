from flask import render_template, request, Blueprint
#from webapplication.models import BlogPost
from webapplication import db, app
from webapplication.models import Produs
import time
import socket
# In the first 60 seconds, the app will return 500, to simulate a startup
return500Seconds = 60
startTime = time.time()

def getUptime():
    """
    Returns the number of seconds since the program started.
    """
    # do return startTime if you just want the process start time
    return time.time() - startTime


core = Blueprint('core',__name__)

@core.route('/')
def index():
  produse = db.session.query(Produs).all()
  instance_ip = socket.gethostbyname(socket.gethostname())

  if getUptime() < return500Seconds:
    return '{"appVersion": "1", "status": "500", "instance_ip": "' + instance_ip + '"}'

  return render_template('index.html', produse=produse, instance_ip=instance_ip)
