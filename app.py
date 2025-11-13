from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to Task Manager API',
        'status': 'running'
    })

@app.route('/hello')
def hello():
    return jsonify({
        'message': 'Hello, World!'
    })

@app.route('/api/info')
def info():
    return jsonify({
        'app_name': 'Task Manager',
        'version': '1.0',
        'author': 'omsekhar'
    })

@app.route('/api/status')
def status():
    return jsonify({
        'database': 'connected',
        'server': 'running',
        'uptime': '24 hours'
    })

@app.route('/api/add')
def add():
    a = int(request.args.get('a', 1))
    b = int(request.args.get('b', 1))
    result = a + b
    return jsonify({'result': result})

# Create a new task
@app.route('/api/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    data = request.get_json()

    new_task = {
        'id': task_id_counter,
        'title': data.get('title'),
        'description': data.get('description'),
        'completed': False
    }
    tasks.append(new_task)
    task_id_counter += 1

    return jsonify({
        'message': 'Task created successfully',
        'task': new_task
    }), 201


# Get all tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({
        'tasks': tasks,
        'count': len(tasks)
    }), 200


# Get task by ID
@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task), 200


# Update a task
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    data = request.get_json()
    task['title'] = data.get('title', task['title'])
    task['description'] = data.get('description', task['description'])
    task['completed'] = data.get('completed', task['completed'])

    return jsonify({
        'message': 'Task updated successfully',
        'task': task
    }), 200


# Delete a task
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'message': f'Task {task_id} deleted successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
