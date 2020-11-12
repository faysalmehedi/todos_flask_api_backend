from flask import Blueprint, request, jsonify, make_response
from src.utils import ResponseGenerator
from src.decorators import token_required
from src.models.user import User


user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/api/v1/create_user', methods=['POST'])
def create_user():

    data = request.get_json()
    
    if data['admin'] == "True":
        admin = True
    else:
        admin = False

    new_user = User(name=data['name'], email=data['email'], password=data['password'], admin=admin)
    User.save(new_user)

    return jsonify({
        'message': data
    })


@user_blueprint.route('/api/v1/users', methods=['GET'])
@token_required
def get_all_users(current_user):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})
    users = User.query.all()
    output = []

    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['name'] = user.name
        user_data['email'] = user.email 
        user_data['admin'] = user.admin
        output.append(user_data)

    return jsonify({
        'users': output
    })


@user_blueprint.route('/api/v1/user/<email>', methods=['GET'])
@token_required
def get_one_user(current_user, email):
        if not current_user.admin:
            return jsonify({'message' : 'Cannot perform that function!'})
        user = User.query.filter_by(email=email).first()

        if not user:
            return jsonify({
                'message': 'No user found in the Database!'
            })

        user_data = {}
        user_data['id'] = user.id
        user_data['name'] = user.name
        user_data['email'] = user.email 
        user_data['admin'] = user.admin

        return jsonify({
            'user': user_data
        })

@user_blueprint.route('/api/v1/update/<email>', methods=['PUT'])
@token_required
def update_user(current_user, email):
    
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    user = User.query.filter_by(email=email).first()
    data = request.get_json()

    if not user:
        return jsonify({
            'message': 'No user found in the Database!'
        })

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

    return jsonify({
        'message': 'User information Updateed!'
    })

@user_blueprint.route('/api/v1/delete/<email>', methods=['DELETE'])
@token_required
def delete_user(current_user, email):

    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({
            'message': 'No user found in the Database!'
        })

    User.delete(user)


    return jsonify({
        'message': "User deleted Successfully!"
    })


# @user_blueprint.route("/api/v1/register")
# def register():
#     return ResponseGenerator.generate_response("Hello", 200)

# @user_blueprint.route("/api/v1/login")
# def login():
#     return ResponseGenerator.generate_response("Hello", 200)
