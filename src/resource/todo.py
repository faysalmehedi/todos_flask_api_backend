from flask import Blueprint, request, jsonify
from src.utils import ResponseGenerator
from src.decorators import token_required
from src.models.models import Todo

todo_blueprint = Blueprint('todo', __name__)

@todo_blueprint.route('/api/v1/todos', methods=['GET'])
@token_required
def get_all_todos(current_user):

    todos = Todo.query.filter_by(user_id=current_user.id).all()

    output = []

    for todo in todos:
        todo_data = {}
        todo_data['id'] = todo.id
        todo_data['text'] = todo.text
        todo_data['complete'] = todo.complete
        todo_data['user_id'] = todo.user_id
        output.append(todo_data)

    return ResponseGenerator.generate_response(output, 200)


@todo_blueprint.route('/api/v1/todo/<todo_id>', methods=['GET'])
@token_required
def get_one_todo(current_user, todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()

    if not todo:
        return jsonify({'message' : 'No todo found!'})

    todo_data = {}
    todo_data['id'] = todo.id
    todo_data['text'] = todo.text
    todo_data['complete'] = todo.complete
    todo_data['user_id'] = todo.user_id

    return ResponseGenerator.generate_response(todo_data, 200)


@todo_blueprint.route('/api/v1/todo/create', methods=['POST'])
@token_required
def create_todo(current_user):
    data = request.get_json()

    new_todo = Todo(text=data['text'], complete=False, user_id=current_user.id)
    Todo.save(new_todo)

    return ResponseGenerator.generate_response(f"{new_todo.text} has been created!", 200)

@todo_blueprint.route('/api/v1/todo/complete/<todo_id>', methods=['PUT'])
@token_required
def complete_todo(current_user, todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()

    if not todo:
        return ResponseGenerator.not_found()

    todo.complete = True
    Todo.update(todo)

    return ResponseGenerator.generate_response(f"{todo.text} has been completed!", 200)


@todo_blueprint.route('/api/v1/todo/delete/<todo_id>', methods=['DELETE'])
@token_required
def delete_todo(current_user, todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()

    if not todo:
        return ResponseGenerator.not_found()

    Todo.delete(todo)

    return ResponseGenerator.generate_response(f"{todo.text} has been Deleted!", 200)