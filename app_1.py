from flask import Flask, jsonify# We import the `Flask` and `jsonify` classes from the Flask library.
from flask_sqlalchemy import SQLAlchemy

# We create a Flask application by initializing the `app` object.
app = Flask(__name__)
                                                    #replace with username:password
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/students'

db = SQLAlchemy(app)

class Student(db.Model): #define a student class as model to represent the "students" table
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(10))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

# We define a route `/students` that responds to GET requests.
@app.route('/students', methods=['GET'])
def get_all_students():
    students = Student.query.all()
    
    json_students = [{'id': student.id, 
             'first_name': student.first_name, 
             'last_name': student.last_name, 
             'age': student.age, 
             'grade': student.grade
             }
             for student in students]
    response = jsonify(json_students)
    return response

# We define a route `/old_students` that responds to GET requests.
@app.route('/old_students/', methods=['GET'])
def old_students():
    students = Student.query.filter(Student.age > 20).all()
    student_list = [{'id': student.id, 
             'first_name': student.first_name, 
             'last_name': student.last_name, 
             'age': student.age, 
             'grade': student.grade
             }
             for student in students]
    return jsonify(student_list)

# We define a route `/young_students` that responds to GET requests.
@app.route('/young_students/', methods=['GET'])
def get_young_students():
    students = Student.query.filter(Student.age < 21).all()
    student_list = [{'id': student.id, 
             'first_name': student.first_name, 
             'last_name': student.last_name, 
             'age': student.age, 
             'grade': student.grade
             }
             for student in students]
    return jsonify(student_list)

# We define a route `/advance_students` that responds to GET requests.
@app.route('/advance_students/', methods=['GET'])
def get_advance_students():
    max_age = 20
    min_grade = "B"
    students = Student.query.filter(Student.age < max_age, Student.grade < min_grade).all()
    student_list = [{'id': student.id, 
             'first_name': student.first_name, 
             'last_name': student.last_name, 
             'age': student.age, 
             'grade': student.grade
             }
             for student in students]
    return jsonify(student_list)

# We define a route `/student_names` that responds to GET requests.
@app.route('/student_names/', methods=['GET'])
def get_student_names():
    students = Student.query.all()
    student_list = [{'first_name': student.first_name, 
             'last_name': student.last_name, 
             }
             for student in students]
    return jsonify(student_list)

# We define a route `/student_ages` that responds to GET requests.
@app.route('/student_ages/', methods=['GET'])
def get_student_ages():
    students = Student.query.all()
    student_list = [
            {'first_name': student.first_name, 
             'last_name': student.last_name, 
             'age': student.age
             }
             for student in students]
    return jsonify(student_list)

if __name__ == '__main__':
    app.run(debug=True)
