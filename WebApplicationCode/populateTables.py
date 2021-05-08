from webapplication import db
from webapplication.models import User
import csv
import datetime

def populateUser():
  useri = []
  user = User("Rizescu", "Eusebiu", "rizescueusebiu@gmail.com", "parola1", "Str. Opulentei, nr. 1", "02bf5a0d67f55b90cb28cdaaffec5814ae9ab068")
  user.activated = True
  useri.append(user)

  db.session.add_all(useri)
  db.session.commit()

if __name__ == '__main__':
  populateUser()
