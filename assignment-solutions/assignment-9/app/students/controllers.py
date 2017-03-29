from flask import Blueprint, request, render_template, \
				  flash, g, session, redirect, url_for , jsonify, make_response
from app import db
from app.students.models import Student
from app.enrolment.models import Enrolment
from flask_cors import CORS


mod_students = Blueprint('students', __name__)
CORS(mod_students)

@mod_students.route('/students', methods=['GET'])
def get_all_students():
	alist = {'students': []}
	for i in Student.query.all():
		clist = []
		for j in Enrolment.query.all():
			if(j.roll == i.roll):
				clist.append(j.code)
		alist['students'].append({'roll': i.roll,'name': i.name,'year':i.year,'courses': clist})	
	return jsonify(alist)


@mod_students.route('/addStudent', methods=['POST'])
def add_student():
	try:		
		student = Student(request.form['roll'], request.form['name'], request.form['year'])
		db.session.add(student)
		db.session.commit()
		return make_response("Student added")
	except:
		return make_response("Error! While Adding Student")
