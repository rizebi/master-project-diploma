from webapplication import db
from webapplication.models import User, Produs

def populateUser():
  useri = []
  user = User("Rizescu", "Eusebiu", "rizescueusebiu@gmail.com", "parola1", "Str. Opulentei, nr. 1", "02bf5a0d67f55b90cb28cdaaffec5814ae9ab068")
  user.activated = True
  useri.append(user)

  db.session.add_all(useri)
  db.session.commit()

def populateProdus():
  produse = []
  produse.append(Produs('Rucsac', 'AMTR01', 'product-images/bag.jpg', 189))
  produse.append(Produs('HDD 1TB', 'USB02', 'product-images/external-hard-drive.jpg', 279))
  produse.append(Produs('Adidasi', 'SH03', 'product-images/shoes.jpg', 349))
  produse.append(Produs('Laptop', 'LPN4', 'product-images/laptop.jpg', 2339))
  produse.append(Produs('Camera', '3DCAM01', 'product-images/camera.jpg', 969))
  produse.append(Produs('Telefon mobil', 'MB06', 'product-images/mobile.jpg', 649))
  produse.append(Produs('Casti', 'HD08', 'product-images/headphone.jpg', 199))
  produse.append(Produs('Ceas', 'WH14', 'product-images/watch.jpg', 519))

  db.session.add_all(produse)
  db.session.commit()

if __name__ == '__main__':
  populateUser()
  populateProdus()
