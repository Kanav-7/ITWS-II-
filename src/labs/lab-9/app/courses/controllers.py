
from flask import Blueprint, request, render_template, \
				  flash, g, session, redirect, url_for
from app import db
from app.courses.models import Course

mod_courses = Blueprint('courses', __name__, url_prefix='/courses')

@mod_courses.route('/', methods=['GET'])
def get_all_courses():
	course=Course.query.all()
	return render_template('courses/index.html', courses=course)

@mod_courses.route('/<code>', methods=['GET'])
def get_course(code):
	course=Course.query.filter(Course.code==code).all()
	return render_template('courses/index.html', courses=course)

@mod_courses.route('/<code>', methods=['POST'])
def update(code):
	cd = request.form['code']
	nm = request.form['name']
	dcptn = request.form['description']
	course = Course.query.filter(Course.code == code).all()
	course.code = cd
	course.name = nm
	course.description = dcptn
	return redirect('/courses')

@mod_courses.route('/create', methods=['GET'])
def create_form():
	return render_template('courses/createCourse.html')

@mod_courses.route('/create', methods=['POST'])
def create_course():
	cd = request.form['code']
	nm = request.form['name']
	dcptn = request.form['description']
	new = Course(cd,nm,dcptn)
	db.session.add(new)
	db.session.commit()
	return redirect('/courses')

@mod_courses.route('/<code>/delete',methods=['GET'])
def delete_course(code):
	course = Course.query.filter(Course.code == code).all()
	for i in course:
		db.session.delete(i)
	db.session.commit()
	return redirect('/courses')

@mod_courses.route('/search', methods=['GET'])
def	search_course():
	search = request.args.get('q')
	search = "%" + search + "%"
	courses = Course.query.filter(Course.name.like(search)).all()
	return render_template('courses/index.html', courses=courses)	

if __name__ == "__main__":
	app.run(debug=True)
