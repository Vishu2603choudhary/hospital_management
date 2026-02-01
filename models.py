from app import db
from datetime import datetime

# Users ṭable created
class User(db.Model):
    __tablename__ = 'users'
    id = db.column(db.Integer,primary_key = True)
    # connecting department table to users as user to department has many to one relationship
    department_id = db.column(db.Integer, db.Foreignkey('department.id'), nullable = True )

    username = db.column(db.string(30),unique = True, nullable = False)
    email = db.column(db.string(100),unique = True ,nullable = False)
    password = db.column(db.string(50), nullable = False)
    role = db.column(db.string(20), nullable = False)
    created_at = db.column(db.DateTime, default = datetime.utcnow)



class Department(db.module):
    __tablename__ = 'department'
    id = db.column(db.Integer(50), primary_key = True)
    name = db.column(db.string(50), nullable = False, unique = True)
    description = db.column(db.text, nullable = False)



class Appointment(db.model):
    __tablename__ = 'appointment'
    id = db.column(db.integer , primary_key = True)
    date = db.column(db.string(12))
    time = db.column(db.string(6))
    status = db.column(db.string(30), default = 'Booked')