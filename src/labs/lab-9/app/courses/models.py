from flask_sqlalchemy import SQLAlchemy
from app import db

class Course(db.Model):
    __tablename__= 'course'
    name = db.Column(db.String(20))
    code = db.Column(db.String(6),primary_key=True,unique = True)
    description = db.Column(db.String(400))

    def __init__(self, code, name, description):
    	self.code = code
    	self.name = name
    	self.description = description    

    def __repr__(self):
        return "Course { code: %r, name: %r, description: %r}"%(self.code,self.name, self.description)

db.create_all()
