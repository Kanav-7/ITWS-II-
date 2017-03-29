from flask_sqlalchemy import SQLAlchemy
from app import db

class Student(db.Model):
    __tablename__ = 'student'
    roll = db.Column(db.Integer, primary_key=True,unique = True)
    name = db.Column(db.String(200))
    year = db.Column(db.String(3))

    def __init__(self, roll, name, year):
        self.roll = roll
        self.name = name
        self.year = year

    def __repr__(self):
        return "Student's representation"
