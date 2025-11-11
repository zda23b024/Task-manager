from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/student')
def student_info():
    student_id = request.args.get('id', '12345')
    data = {
        'id': student_id,
        'name': 'zakariya Y',
        'course': 'Data Science And AI',
        'year': '3rd Year',
        'gpa': 8.68
    }
    return jsonify(data)

@app.route('/api/students/count')
def student_count():
    return jsonify({'total_students': 150})

if __name__ == '__main__':
    app.run(debug=True, port=5002)
