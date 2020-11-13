from flask import Blueprint, request, jsonify, make_response
from src.models.models import User
from src.core.config import Configuration
from src.utils import ResponseGenerator
import jwt
import datetime

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/api/v1/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        # return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required"'})
        return ResponseGenerator.mandatory_field(["email", "password"], 401)
    
    user = User.query.filter_by(email=auth.username).first()
    
    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required"'})


    if User.check_password(user, auth.password):
        token = jwt.encode({'email' : user.email, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, Configuration.SECRET_KEY)
        return jsonify({
            'token': token.decode('UTF-8')
        })

    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required"'})