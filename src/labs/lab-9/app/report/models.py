from flask_sqlalchemy import SQLAlchemy
from app import db


class GradeEntry(db.Model):
    __tablename__ = 'grade_entry'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    assignments = db.Column(db.Float)
    labs = db.Column(db.Float)
    mids = db.Column(db.Float)
    end_sem = db.Column(db.Float)
    student_rollno = db.Column(db.Integer,db.ForeignKey('Student.rollno'))
    course_code = db.Column(db.String(6),db.ForeignKey('Course.code'))

    def __init__(self, student, course):
        self.assignments = 0.0
        self.labs = 0.0
        self.mids = 0.0
        self.end_sem = 0.0
        self.student_rollno = student_rollno
        self.course_code = course_code

db.create_all()        
