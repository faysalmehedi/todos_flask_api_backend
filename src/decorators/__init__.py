from functools import wraps 
from flask import request, jsonify
from src.utils import ResponseGenerator 
from src.models.models import User 
from src.core.config import Configuration

import jwt 


def json_data_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if not request.is_json:
            return ResponseGenerator.json_data_expected()

        try:
            request.get_json()
        except Exception as _e:
            return ResponseGenerator.json_data_expected()

        return f(*args, **kwargs)

    return wrap 

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({
                'message': 'Token is missing!'
            }), 401
        
        try:
            data = jwt.decode(token, Configuration.SECRET_KEY)
            current_user = User.query.filter_by(email=data['email']).first()
        except:
            return jsonify({
                "message": 'Token is invalid!'
            }), 401

        return f(current_user, *args, **kwargs)

    return decorated