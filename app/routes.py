from app import app, db
from flask import request, jsonify
from app.models import Course


@app.route('/')
@app.route('/courses', methods=['GET'])
def get_courses_list():
    courses = Course.query.order_by(Course.id).all()
    return jsonify(courses)


@app.route('/courses/create', methods=['POST'])
def create():
    course = request.json
    db.session.add(course)
    db.session.commit()
    return 'Successful'


@app.route('/courses/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def one_course():
    if request.method == 'DELETE':
        return jsonify()
    if request.method == 'PATCH':
        return jsonify()
    if request.method == 'GET':
        return jsonify()


@app.route('/search', methods=['GET'])
def search():
    return jsonify()
