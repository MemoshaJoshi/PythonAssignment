import sqlite3
from sqlalchemy import create_engine, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

engine = create_engine('sqlite:///hotel6.db', echo=True)

# metadata = MetaData()

# connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Model

class Customer(Base):
    __tablename__ = 'customer'

    c_id = Column(Integer(), primary_key=True)
    name = Column(String, nullable= False)
    gender = Column(String, nullable= False)
    age = Column(Integer(), nullable= False)
    phone = Column(Integer(), nullable= False, unique= True)

    # def __repr__(self):
    #     return "c_id={},name={},gender={},age={},phone={}".format(self.c_id, self.name, self.gender,self.age,self.phone)

class Room(Base):
    __tablename__ = 'room'

    r_id = Column(Integer(), primary_key= True)
    room_type = Column(String, nullable= False)
    price = Column(Integer(),nullable= False)

    def __repr__(self):
        return "r_id={},room_type={}".format(self.r_id, self.room_type)

# Foreign Key Relationship

class Booking(Base):
    __tablename__ = 'booking'

    booking_id = Column(Integer(), primary_key=True)
    check_in = Column(Date(), nullable= False)
    check_out = Column(Date(), nullable= False)
    cost = Column(Integer(), nullable= False)
    payment = Column(String(), nullable= False)
    customer_id = Column(Integer(), ForeignKey('customer.c_id'))
    room_id = Column(Integer(), ForeignKey('room.r_id'))

    def __repr__(self):
        return "booking_id={},check_in={},check_out={},cost={},payment={},customer_id={},room_id={}".format(self.booking_id, self.check_in, self.check_out,self.cost,self.payment,self.customer_id,self.room_id)

def create_table():
    Base.metadata.create_all(engine)

def date_convert(date):
    return datetime.strptime(date, '%Y-%m-%d').date()

# add_customer
@app.route('/add_customer', methods=['POST'])
def add_customer():
    print(request.url)

    name = request.args.get('name')
    gender = request.args.get('gender')
    age = int(request.args.get('age'))
    phone = int(request.args.get('phone'))

    print('request')

    customer = Customer(name=name, gender= gender, age= age, phone= phone)
    print('req')
    session.add(customer)
    session.commit()

    return jsonify({'message':'Customer added successfully'})

@app.route('/price_stay', methods=['GET'])
def price_stay():
    print(request.url)

    room_type = request.args.get('room_type')
    check_in = date_convert(request.args.get('check_in'))
    check_out = date_convert(request.args.get('check_out'))
    print(room_type,check_in,check_out)

    room1 = session.query(Room).filter_by(
    room_type =room_type).first()

    # calculate the total price of stay for the given dates
    total_price = (check_out - check_in).days * room1.price

    return jsonify({'Total price is': total_price})


@app.route('/add_booking', methods=['POST'])
def add_booking():
    print(request.url)

    check_in1 = date_convert(request.args.get('check_in'))
    check_out2 = date_convert(request.args.get('check_out'))
    payment = request.args.get('payment')
    customer_id = int(request.args.get('customer_id'))
    room_id = int(request.args.get('room_id'))

    room1 = session.query(Room).filter_by(r_id= room_id).first()
    # calculate the total price of stay for the given dates
    total_price = (check_out2 - check_in1).days * room1.price
    print(total_price)

    # create a new booking object
    booking = Booking(check_in=check_in1, check_out=check_out2, payment=payment,
                      cost=total_price, customer_id=customer_id, room_id=room_id)
    # add the booking to the session
    session.add(booking)
    # commit the changes to the DB
    session.commit()
    return jsonify({'message': 'Booking successfully', 'customer_id':customer_id})

@app.route('/track_status', methods=['GET'])
def track_room():
    print(request.url)

    room_id1 = request.args.get('room_id')
    check_in1 = date_convert(request.args.get('check_in'))
    check_out2 = date_convert(request.args.get('check_out'))

    if check_room(check_in1, check_out2, room_id1):
        return jsonify({"message": "Room available", 'room_id': room_id1})
    else:
        return jsonify({"message": "Room not available"})

def check_room(check_in1, check_out2, room_id1):

    booking1s = session.query(Booking).filter_by(room_id=room_id1).all()

    for booking in booking1s:
        if (check_in1 <= booking.check_in <= check_out2) or (check_in1 <= booking.check_out <= check_out2):
            return False
    return True



















# customer = Table('customer', metadata,
#                  Column('customer_id', Integer(), primary_key=True, nullable=False),
#                  Column('name', String(30), nullable=False, unique=True),
#                  Column('gender', String(1), nullable=False),
#                  Column('age', Integer(), nullable=False),
#                  Column('phone', Integer(), nullable=False, unique=True)
#                  )


#
# # room = Table('room', metadata,
# #              Column('room_id', Integer(), primary_key= True, nullable= False),
# #              Column('room_type', String(), nullable= False)
# #              )
# #
# booking = Table('booking', metadata,
#                 Column('booking_id', Integer(), primary_key= True, nullable= False),
#                 Column('check_in', Integer(), nullable= False),
#                 Column('check_out', Integer(), nullable= False),
#                 Column('cost', Integer(), nullable= False),
#                 Column('payment', Integer()),
#                 Column('customer_id', Integer, ForeignKey('customer.customer_id')),
#                 Column('room_id', Integer, ForeignKey('room.room_id'))
#                 )
#
# # Create the table in the database
# metadata.create_all(engine)

# # Inserting multiple records at once...
# # Build a list of dictionaries: values_list
# customer_list = [
#     {'customer_id': 1, 'name': 'Anna', 'gender': 'F', 'age': 32, 'phone': 9808426701},
#     {'customer_id': 2, 'name': 'Chris', 'gender': 'M', 'age': 40, 'phone': 9813114467},
#     {'customer_id': 3, 'name': 'Will', 'gender': 'M', 'age': 42, 'phone': 9818124541}
#
# ]
#
# # Build an insert statement for the data table: stmt
# stmt = insert(customer)
#
# # Execute stmt with the values_list: results
# results = connection.execute(stmt, customer_list)
#
# # Print rowcount
# print(results.rowcount)
#
# booking_list = [
#     {'booking_id': 1, 'check_in': '6', 'check_out': '12', 'cost': 32000, 'payment': 32000, 'customer_id': 1, 'room_id': 1 },
#     {'booking_id': 2, 'check_in': '2', 'check_out': '8', 'cost': 18000, 'payment': 18000, 'customer_id': 3, 'room_id': 3},
#     {'booking_id': 3, 'check_in': '6', 'check_out': '5', 'cost': 25000, 'payment': 25000, 'customer_id': 2, 'room_id': 2}
#
# ]
#
# stmt = insert(booking)
#
# results = connection.execute(stmt, booking_list)
#
# room_list = [
#     {'room_id': 1, 'room_type': 'deluxe'},
#     {'room_id': 2, 'room_type': 'single'},
#     {'room_id': 3, 'room_type': 'double'}
#
# ]
#
# stmt = insert(room)
#
# results = connection.execute(stmt, room_list)


if __name__ == '__main__':
    create_table()
    app.run(host= '127.0.0.3', port=5000, debug=True)







