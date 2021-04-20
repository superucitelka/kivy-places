from sqlalchemy import create_engine, Column, ForeignKey, UniqueConstraint, desc
from sqlalchemy.types import Float, String, Integer, TIMESTAMP, Enum, Text, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Global Variables

SQLITE = 'sqlite'
MYSQL = 'mysql'

Base = declarative_base()

class Place(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    url = Column(String(100))
    rate = Column(Float(precision=1))
    latitude = Column(Float(precision=10))
    longitude = Column(Float(precision=10))
    photos = relationship('Photo', backref='place')
    category_id = Column(Integer, ForeignKey('categories.id'))
    UniqueConstraint('longitude', 'latitude', name='location')


class Photo(Base):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True)
    url = Column(String(100), unique=True, nullable=False)
    title = Column(String(length=50))
    time = Column(TIMESTAMP)
    type = Column(Enum('barevná', 'černobílá'))
    place_id = Column(Integer, ForeignKey('places.id'))


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    icon = Column(BLOB)
    places = relationship('Place', backref='category')


class Database:
    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB}',
        MYSQL: 'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@localhost/{DB}'
    }

    def __init__(self, dbtype='sqlite', username='', password='', dbname='../places.db'):
        dbtype = dbtype.lower()

        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname, USERNAME=username, PASSWORD=password)
            self.engine = create_engine(engine_url, echo=False)
        else:
            print('DBType is not found in DB_ENGINE')

        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_place(self, place):
        try:
            self.session.add(place)
            self.session.commit()
            return True
        except:
            return False

    def create_places(self, places):
        try:
            self.session.add_all(places)
            self.session.commit()
            return True
        except:
            return False

    def create_photo(self, photo):
        try:
            self.session.add(photo)
            self.session.commit()
            return True
        except:
            return False

    def create_category(self, category):
        try:
            self.session.add(category)
            self.session.commit()
            return True
        except:
            return False

    def read_places(self, order = Place.name):
        try:
            result = self.session.query(Place).all()
            return result
        except:
            print("Chyba")
            return False

    def read_categories(self, order = Category.name):
        try:
            result = self.session.query(Category).order_by(order).all()
            return result
        except:
            print("Chyba")
            return False


    def read_place_by_id(self, id):
        try:
            result = self.session.query(Place).get(id)
            return result
        except:
            return False

    def read_places_by_category(self, category):
        try:
            result = self.session.query(Place).join(Category).filter(Category.name.like(f'%{name}%')).order_by(Place.name).all()
            return result
        except:
            return False

    def read_category_by_name(self, name):
        try:
            result = self.session.query(Category).filter(Category.name.like(f'%{name}%')).all()
            return result
        except:
            return False

    def read_photos_by_place(self, name):
        try:
            result = self.session.query(Photo).all()
            return result
        except:
            return False

    def update(self):
        try:
            self.session.commit()
            return True
        except:
            return False

    def delete_place(self, id):
        try:
            place = self.read_place_by_id(id)
            self.session.delete(place)
            self.session.commit()
            return True
        except:
            return False

    def delete_photo(self, id):
        try:
            photo = self.read_photo_by_id(id)
            self.session.delete(photo)
            self.session.commit()
            return True
        except:
            return False

    def delete_category(self, id):
        try:
            category = self.read_category_by_id(id)
            self.session.delete(category)
            self.session.commit()
            return True
        except:
            return False

