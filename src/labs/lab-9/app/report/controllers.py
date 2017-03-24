from flask import Blueprint, request, render_template, \
				  flash, g, session, redirect, url_for
from app import db
from app.report.models import GradeEntry

mod_report = Blueprint('report', __name__, url_prefix='/report')

@mod_report.route('/student/<rollno>', methods=['GET'])
def get_student_grades(rollno):
	grades = GradeEntry.query.filter(GradeEntry.student_rollno == rollno).all()
	return render_template('report/courses_for_student.html', report=grades)

@mod_report.route('/course/<code>', methods=['GET'])
def get_course(code):
	grades = GradeEntry.query.filter(GradeEntry.course_code == code).all()
	return render_template('report/students_for_course.html', report=grades)

@mod_report.route('/entry/<rollno>/<code>', methods=['GET'])
def get_student_course(rollno,code):
	grades = GradeEntry.query.filter(GradeEntry.course_code == code,GradeEntry.student_rollno == rollno).all()
	return render_template('/report/StudentCourse.html', report = grades)
