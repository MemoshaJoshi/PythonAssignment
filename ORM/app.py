import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from sqlalchemy import table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

# from flask import Flask
#
#
# app = Flask(__name__)


engine = create_engine('sqlite:///HotelManagementSystem.db', echo= True)
connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


# Model

class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    phone = Column(Integer, nullable=False, unique=True)

    def __repr__(self):
        return "name={},id={}, phone={}".format(self.id, self.name, self.phone)


def create_table():
    Base.metadata.create_all(engine)

def add_new_customer():
    customer = Customer(name='John Snow', phone= '9808562351')
    session.add(customer)
    session.commit()


if __name__ == '__main__':
    create_table()
    add_new_customer()
