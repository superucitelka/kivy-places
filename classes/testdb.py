from classes.database import *

#db = Database(dbtype='sqlite', dbname='../places.db')
db = Database(dbtype='mysql', username='root', password='', dbname='places')

category = Category()
category.name = "vzdělávání"
db.create_category(category)

place = Place()
place.name = "SŠPU Opava"
place.description = "Střední odborná škola"
db.create_place(place)

photo1 = Photo()
photo1.title = "Hlavní budova školy"
photo1.url = "https://www.sspu-opava.cz/media/cms_page_media/80/skola1.jpg"
db.create_photo(photo1)

photo2 = Photo()
photo2.title = "Tělocvična"
photo2.url = "https://www.sspu-opava.cz/media/cms_page_media/80/telocvicna.jpg"
db.create_photo(photo2)
