from flask import Flask, request
import time

# In the first 60 seconds, the app will return 500, to simulate a startup
return500Seconds = 60
startTime = time.time()

def getUptime():
    """
    Returns the number of seconds since the program started.
    """
    # do return startTime if you just want the process start time
    return time.time() - startTime

# Flask app
app = Flask(__name__)

@app.route('/')
def index():
  # Return 500 if less than $return500Seconds have passed
  if getUptime() < return500Seconds:
    return '{"appVersion": "1", "status": "500"}'
  return '{"appVersion": "1", "status": "200"}'
app.run(host='0.0.0.0', port=7000)