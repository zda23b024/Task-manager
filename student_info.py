from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock student data
students = [
    {'roll_number': 'ZDA23001', 'name': 'Aisha Mohammed', 'course': 'DSAI', 'year': '3rd Year', 'gpa': 9.0},
    {'roll_number': 'ZDA23002', 'name': 'Omar Suleiman', 'course': 'DSAI', 'year': '3rd Year', 'gpa': 8.5},
    {'roll_number': 'ZDA23003', 'name': 'Fatma Ali', 'course': 'DSAI', 'year': '3rd Year', 'gpa': 6.9},
    {'roll_number': 'ZDA23004', 'name': 'Hassan Juma', 'course': 'DSAI', 'year': '3rd Year', 'gpa': 7.6},
    {'roll_number': 'ZDA23005', 'name': 'Maryam Yusuf', 'course': 'DSAI', 'year': '3rd Year', 'gpa': 7.8},
]


@app.route('/api/student')
def get_student():
    roll = request.args.get('id')  # <-- changed from 'roll_number' to 'id'
    if not roll:
        return jsonify({'error': 'Please provide an id parameter'}), 400

    for student in students:
        if student['roll_number'] == roll:
            return jsonify(student)

    return jsonify({'error': f'No student found with id {roll}'}), 404


@app.route('/api/students/count')
def student_count():
    return jsonify({'total_students': len(students)})


if __name__ == '__main__':
    app.run(debug=True, port=5002)  # <-- changed port to 5002
