from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for , make_response ,jsonify
from app import db
from flask_cors import CORS
from app.courses.models import Course

mod_courses = Blueprint('courses', __name__)
CORS(mod_courses)
@mod_courses.route('/courses', methods=['GET'])
def get_all_courses():
    alist = []
    for i in Course.query.all():
        alist.append({'code': i.code,'name': i.name}) 
    return jsonify({'courses':alist})

@mod_courses.route('/addCourse', methods=['POST'])
def add_course():
    try:
        course = Course(request.form['code'],request.form['name'])
        db.session.add(course)
        db.session.commit() 
        return make_response('Course Added')
    except:
        return make_response('Error! While Adding Course')