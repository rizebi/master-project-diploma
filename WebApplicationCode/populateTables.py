from carplanner import db
from carplanner.models import User
import csv
import datetime

def populateUser():
  useri = []
  user = User("Popescu", "Ion", "carplannertest1@gmail.com", "parola1", "Personal", "02bf5a0d67f55b90cb28cdaaffec5814ae9ab068")
  user.imagineProfil='carplannertest1@gmail.com.jpg'
  user.activated = True
  useri.append(user)
  user = User("Georgescu", "Alexandru", "carplannertest2@gmail.com", "parola2", "TransportMarfa.SRL", "6de8815920815082c0e28ad5044446b639222375")
  user.activated = True
  useri.append(user)

  db.session.add_all(useri)
  db.session.commit()

if __name__ == '__main__':
  populateUser()
