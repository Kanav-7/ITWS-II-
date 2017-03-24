from flask_sqlalchemy import SQLAlchemy
from app import db

class Student(db.Model):
    __tablename__ = 'student'
    #id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rollno = db.Column(db.Integer, primary_key=True,unique = True)
    name = db.Column(db.String(20))

    def __init__(self, rollno, name):
        self.name = name
        self.rollno  = rollno

    def __repr__(self):
        return "Student { name: %r, rollno: %r }"%(self.rollno, self.name)

db.create_all()
