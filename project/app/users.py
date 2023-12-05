#chyba finito



from flask import Blueprint, request, jsonify, abort
from .models import users, User
import json


users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('', methods=['GET'])
def get_users():
    return jsonify([user.to_json() for user in users]), 200

@users_blueprint.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user.id == user_id), None)
    if user is not None:
        return jsonify(user.to_json()), 200
    else:
        return jsonify({"error": "User not found"}), 404

@users_blueprint.route('', methods=['POST'])
def create_user():
    user_data = request.get_json()
    if 'name' in user_data and 'lastname' in user_data:
        new_user = User(_id=len(users) + 1, name=user_data['name'], lastname=user_data['lastname'])
        users.append(new_user)
        return jsonify(new_user.to_json()), 201
    else:
        return jsonify({"error": "Missing name or lastname"}), 400

@users_blueprint.route('/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user_data = request.get_json()
    user = next((user for user in users if user.id == user_id), None)
    if user is not None:
        user.name = user_data.get('name', user.name)
        user.lastname = user_data.get('lastname', user.lastname)
        return '', 204
    else:
        return jsonify({"error": "User not found"}), 404

@users_blueprint.route('/<int:user_id>', methods=['PUT'])
def replace_user(user_id):
    user_data = request.get_json()
    if 'name' in user_data and 'lastname' in user_data:
        user = next((user for user in users if user.id == user_id), None)
        if user is not None:
            user.name = user_data['name']
            user.lastname = user_data['lastname']
            return '', 204
        else:
            return jsonify({"error": "User not found"}), 404
    else:
        return jsonify({"error": "Missing name or lastname"}), 400

@users_blueprint.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((user for user in users if user.id == user_id), None)
    if user is not None:
        users = [user for user in users if user.id != user_id]
        return '', 204
    else:
        return jsonify({"error": "User not found"}), 404
