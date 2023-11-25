# from app import db
from flask_sqlalchemy import SQLAlchemy

from main import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    leave_balance = db.Column(db.Integer, nullable=False)

class LeaveBalances(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    leave_type = db.Column(db.String(50))
    balance = db.Column(db.Float(8, 2))

    # Define the relationship with the Employee table
    employee = db.relationship('Employee', backref='leave_balances')
class LeavePolicy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    leave_policy = db.Column(db.String(100), nullable=False)
    max_leave_days = db.Column(db.Integer(), nullable = False)

class Holiday(db.Model):

    HolidayID = db.Column(db.Integer, primary_key=True)
    HolidayDate = db.Column(db.Date, nullable=False)
    HolidayDay = db.Column(db.String(20), nullable = False)
    Description = db.Column(db.String(100), nullable=False)

