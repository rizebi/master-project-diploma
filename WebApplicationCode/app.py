from carplanner import app
import logging
from logging.handlers import RotatingFileHandler


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
