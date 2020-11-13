from flask import Blueprint, request, jsonify
from src.utils import ResponseGenerator
from src.decorators import token_required
from src.models.models import User


user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/api/v1/create_user', methods=['POST'])
def create_user():

    data = request.get_json()
    email = data['email']
    user = User.query.filter_by(email=email).first()

    if user:
        return ResponseGenerator.error_response(f"Already {email} exist in DB. Try using other email address", 409)
    
    if data['admin'] == "True":
        admin = True
    else:
        admin = False

    new_user = User(name=data['name'], email=data['email'], password=data['password'], admin=admin)
    User.save(new_user)

    return ResponseGenerator.generate_response(data, 200)


@user_blueprint.route('/api/v1/users', methods=['GET'])
@token_required
def get_all_users(current_user):
    if not current_user.admin:
        return ResponseGenerator.not_authorized()
    
    users = User.query.all()
    output = []

    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['name'] = user.name
        user_data['email'] = user.email 
        user_data['admin'] = user.admin
        output.append(user_data)

    return ResponseGenerator.generate_response(output, 200)


@user_blueprint.route('/api/v1/user/<email>', methods=['GET'])
@token_required
def get_one_user(current_user, email):
        if not current_user.admin:
            return ResponseGenerator.not_authorized()

        user = User.query.filter_by(email=email).first()

        if not user:
            return ResponseGenerator.not_found()

        user_data = {}
        user_data['id'] = user.id
        user_data['name'] = user.name
        user_data['email'] = user.email 
        user_data['admin'] = user.admin

        return ResponseGenerator.generate_response(user_data, 200)

@user_blueprint.route('/api/v1/update/<email>', methods=['PUT'])
@token_required
def update_user(current_user, email):
    
    if not current_user.admin:
        return ResponseGenerator.not_authorized()

    user = User.query.filter_by(email=email).first()
    data = request.get_json()

    if not user:
        return ResponseGenerator.not_found()

    if data['admin'] == "True":
        admin = True
    else:
        admin = False
    
    user.name = data['name']
    user.password = data['password']
    user.email = data['email']
    user.admin = admin
    update_user = User(name=user.name, email=user.email, password=user.password, admin=user.admin)

    User.update(update_user)

    return ResponseGenerator.generate_response(f"{update_user.name} has been successfully updated", 200)


@user_blueprint.route('/api/v1/delete/<email>', methods=['DELETE'])
@token_required
def delete_user(current_user, email):

    if not current_user.admin:
        return ResponseGenerator.not_authorized()

    user = User.query.filter_by(email=email).first()

    if not user:
        return ResponseGenerator.not_found()

    User.delete(user)

    return ResponseGenerator.generate_response(f"{user.name} deleted successfully from DB.", 200)


