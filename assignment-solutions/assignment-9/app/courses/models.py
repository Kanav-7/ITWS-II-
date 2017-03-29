from flask_sqlalchemy import SQLAlchemy
from app import db

class Course(db.Model):
    __tablename__= 'course'
    code = db.Column(db.String(6),primary_key=True, unique = True)
    name = db.Column(db.String(200))

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __repr__(self):
        return "Some nice representation"


