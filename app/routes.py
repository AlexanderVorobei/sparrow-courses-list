from app import app, db
from flask import request, jsonify
from app.models import Course, course_schema, courses_schema


@app.route('/', methods=['GET'])
def get_courses_list():
    courses = Course.query.order_by(Course.id).all()
    res = courses_schema.dump(courses)
    return jsonify(res.data)


@app.route('/courses/create', methods=['POST'])
def create():
    title = request.json['title']
    startdate = request.json['startdate']
    enddate = request.json['enddate']
    hours = request.json['hours']

    course = Course(title, startdate, enddate, hours)

    db.session.add(course)
    db.session.commit()

    return course_schema.jsonify(course)


@app.route('/courses/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def one_course(id):
    if request.method == 'DELETE':
        course = Course.query.get(id)
        db.session.delete(course)
        db.session.commit()

    if request.method == 'PUT':
        course = Course.query.get(id)
        title = request.json['title']
        startdate = request.json['startdate']
        enddate = request.json['enddate']
        hours = request.json['hours']

        course.title = title
        course.startdate = startdate
        course.enddate = enddate
        course.hours = hours
        db.session.commit()
        return course_schema.jsonify(course)

    if request.method == 'GET':
        course = Course.query.get(id)
        return course_schema.jsonify(course)


@app.route('/search', methods=['GET'])
def search():
    return " "
