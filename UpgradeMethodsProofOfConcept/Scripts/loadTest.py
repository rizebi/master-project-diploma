import time # for sleep
import json # for JSON manipulation
import requests # for requests launching
import threading # for threading purposes
from flask import Flask # used for exposing metrics

# Variables

# For A/B testing setup
#destinationIP = "http://localhost:8000"
# For all other setups
destinationIP = "http://192.168.64.2"
userAgent1 = "Always-Good"
userAgent2 = "Sometimes-Fail"
hostnameToUse = "dizertatie.com"
portToExposeMetrics = 7001

# Flask app
app = Flask(__name__)

# Global counters
requests200V1 = 0
requests500V1 = 0
requests200V2 = 0
requests500V2 = 0

# Load test function
def loadTest():
  global requests200V1
  global requests500V1
  global requests200V2
  global requests500V2

  while True:
    try:
      # User Agent 1
      headers = {'User-Agent': userAgent1, 'Host': hostnameToUse}
      resp = requests.get(destinationIP, headers=headers).json()
      if resp["appVersion"] == "1" and resp["status"] == "200":
        requests200V1 += 1
      if resp["appVersion"] == "1" and resp["status"] == "500":
        requests500V1 += 1
      if resp["appVersion"] == "2" and resp["status"] == "200":
        requests200V2 += 1
      if resp["appVersion"] == "2" and resp["status"] == "500":
        requests500V2 += 1

      # User Agent 2
      headers = {'User-Agent': userAgent2, 'Host': hostnameToUse}
      resp = requests.get(destinationIP, headers=headers).json()
      if resp["appVersion"] == "1" and resp["status"] == "200":
        requests200V1 += 1
      if resp["appVersion"] == "1" and resp["status"] == "500":
        requests500V1 += 1
      if resp["appVersion"] == "2" and resp["status"] == "200":
        requests200V2 += 1
      if resp["appVersion"] == "2" and resp["status"] == "500":
        requests500V2 += 1
    except:
      pass
    time.sleep(0.01)

# Page that is queried by Prometheus to get metrics
@app.route('/')
def index():
  global requests200V1
  global requests500V1
  global requests200V2
  global requests500V2

  # Compose return string
  stringToReturn = ""
  stringToReturn += "requests200V1 " + str(requests200V1) + "\n"
  stringToReturn += "requests500V1 " + str(requests500V1) + "\n"
  stringToReturn += "requests200V2 " + str(requests200V2) + "\n"
  stringToReturn += "requests500V2 " + str(requests500V2) + "\n"

  # Reset the counters
  requests200V1 = 0
  requests500V1 = 0
  requests200V2 = 0
  requests500V2 = 0

  return stringToReturn

# Main
if __name__ == "__main__":
  loadTestThread = threading.Thread(target=loadTest, name="loadTester", args="")
  loadTestThread.start()
  app.run(host='0.0.0.0', port=portToExposeMetrics)
