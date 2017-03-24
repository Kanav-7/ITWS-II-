from flask import Blueprint, request, render_template, \
				  flash, g, session, redirect, url_for
from app import db
from app.students.models import Student

mod_students = Blueprint('students', __name__, url_prefix='/students')

@mod_students.route('/', methods=['GET'])
def get_all_students():
	students = Student.query.all()
	return render_template('students/index.html', students=students)

@mod_students.route('/<rollno>', methods=['GET'])
def get_student(rollno):
	student = Student.query.filter(Student.rollno == rollno).all()
	return render_template('students/index.html', students=student)

@mod_students.route('/<rollno>', methods=['POST'])
def update(rollno):
	nm = request.form['name']
	roll = request.form['rollno']
	student = Student.query.filter(Student.rollno == rollno).all()
	student.name = nm
	student.rollno = roll
	return redirect('/students')
		
@mod_students.route('/create', methods=['GET'])
def create_form():
	return render_template('students/createStudent.html')

@mod_students.route('/create', methods=['POST'])
def create_student():
	new = Student(request.form['rollno'],request.form['name'])
	db.session.add(new)
	db.session.commit()
	return redirect('/students')

@mod_students.route('/<rollno>/delete',methods=['GET'])
def delete_student(rollno):
	student = Student.query.filter(Student.rollno == rollno).all()
	for i in student:
		db.session.delete(i)
	db.session.commit()
	return redirect('/students')

@mod_students.route('/search', methods=['GET'])
def	search_student():
	search = request.args.get('q')
	search = "%" + search + "%"
	students = Student.query.filter(Student.name.like(search)).all()
	return render_template('students/index.html', students=students)	 


if __name__ == "__main__":
    app.run(debug=True)			

