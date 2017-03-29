# Import flask and template operators
from flask import Flask, render_template
from flask_cors import CORS
# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.students.controllers import mod_students
from app.courses.controllers import mod_courses
from app.enrolment.controllers import mod_enrolment

# Register blueprint(s)
app.register_blueprint(mod_students)
app.register_blueprint(mod_courses)
app.register_blueprint(mod_enrolment)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
