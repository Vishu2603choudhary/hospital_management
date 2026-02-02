from app import db
from datetime import datetime

# Users ṭable created
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    # connecting department table to users as user to department has many to one relationship
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable = True )

    username = db.Column(db.String(30),unique = True, nullable = False)
    email = db.Column(db.String(100),unique = True ,nullable = False)
    password = db.Column(db.String(50), nullable = False)
    role = db.Column(db.String(20), nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)


class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False, unique = True)
    description = db.Column(db.Text, nullable = False)



class Appointment(db.Model):
    __tablename__ = 'appointment'
    id = db.Column(db.Integer , primary_key = True)
    date = db.Column(db.String(12))
    time = db.Column(db.String(6))
    status = db.Column(db.String(30), default = 'Booked')