from flask import render_template, request, Blueprint
#from webapplication.models import BlogPost
from webapplication import db, app
from webapplication.models import Produs
import time
from random import randint
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

# Parameters
userAgentThatSometimesShouldFail = "Sometimes-Fail"
failRate = 50 # 50 means 50%

core = Blueprint('core',__name__)

@core.route('/')
def index():
  produse = db.session.query(Produs).all()
  instance_ip = socket.gethostbyname(socket.gethostname())
  if getUptime() < return500Seconds:
    return '{"appVersion": "2", "status": "500", "instance_ip": "' + instance_ip + '"}'

  userAgent = request.headers.get('User-Agent')
  if userAgent != userAgentThatSometimesShouldFail:
    return render_template('index.html', produse=produse, instance_ip=instance_ip)
  else:
    randomNumber = randint(0, 99)
    if randomNumber < failRate:
      return '{"appVersion": "2", "status": "500", "instance_ip": "' + instance_ip + '"}'
    else:
      return render_template('index.html', produse=produse, instance_ip=instance_ip)
