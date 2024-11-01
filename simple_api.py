import os
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Set the environment to production
app.config['ENV'] = 'production'

# Sample data storage
students = []

# Helper function to find a student by ID
def find_student(student_id):
    return next((student for student in students if student['id'] == student_id), None)

# GET /students - Retrieve a list of all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200

# GET /students/{id} - Retrieve details of a student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = find_student(student_id)
    if student is None:
        abort(404, description="Student not found.")
    return jsonify(student), 200

# POST /students - Add a new student
@app.route('/students', methods=['POST'])
def create_student():
    if not request.json or 'name' not in request.json or 'grade' not in request.json or 'email' not in request.json:
        abort(400, description="Name, Grade, and Email are required fields.")
    student = {
        'id': request.json.get('id', len(students) + 1),  # auto-increment ID
        'name': request.json['name'],
        'grade': request.json['grade'],
        'email': request.json['email']
    }
    students.append(student)
    return jsonify(student), 201

# PUT /students/{id} - Update an existing student by ID
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = find_student(student_id)
    if student is None:
        abort(404, description="Student not found.")
    if 'name' in request.json:
        student['name'] = request.json['name']
    if 'grade' in request.json:
        student['grade'] = request.json['grade']
    if 'email' in request.json:
        student['email'] = request.json['email']
    return jsonify(student), 200

# DELETE /students/{id} - Delete a student by ID
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = find_student(student_id)
    if student is None:
        abort(404, description="Student not found.")
    students.remove(student)
    return jsonify({"result": True}), 200

if __name__ == '__main__':
    app.run(debug=True)
