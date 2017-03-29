from flask import Blueprint, request, render_template, \
				  flash, g, session, redirect, url_for,make_response
from app import db
from flask_cors import CORS
from app.enrolment.models import Enrolment
from app.courses.models import Course
from app.students.models import Student


mod_enrolment = Blueprint('enrolment', __name__)
CORS(mod_enrolment)


@mod_enrolment.route('/enroll', methods=['POST'])
def enroll_student_to_course():
	try:
		enrolment = Enrolment(request.form['roll'], request.form['code'])
		db.session.add(enrolment)
		db.session.commit()
		return make_response('Student Enrolled')
	except:
		return make_response('Error! While Enrolling Student')
