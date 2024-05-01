from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify, request
from bson.json_util import dumps
from . import mongo
from .models.user import User

users_collection = mongo.db.users

@app.route('/users/<user_id>/preferences', methods=['PUT'])
def update_user_preferences(user_id):
    data = request.get_json()
    
    preferences = data.get('preferences')
    result = users_collection.update_one(
        {'_id': ObjectId(user_id)},
        {'$set': {'preferences': preferences}}
    )
    if result.modified_count == 1:
        return jsonify({"msg": "User preferences updated successfully"}), 200
    else:
        return jsonify({"error": "User not found or preferences not updated"}), 404

@app.route('/users/<user_id>')
def get_user_info(user_id):
    user = users_collection.find_one_or_404({'_id': ObjectId(user_id)})
    return jsonify(User.from_mongo(user).to_dict())

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User.from_dict(data)
    result = users_collection.insert_one(user.to_dict())
    return jsonify(str(result.inserted_id))

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    updated_user = User.from_dict(data)
    result = users_collection.update_one({'_id': ObjectId(user_id)}, {'$set': updated_user.to_dict()})
    return jsonify(result.modified_count)

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = users_collection.delete_one({'_id': ObjectId(user_id)})
    return jsonify(result.deleted_count)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = users_collection.find_one({'email': email})
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity=str(user['_id']))
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Invalid email or password"}), 401

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = generate_password_hash(data.get('password'))

    if users_collection.find_one({'email': email}):
        return jsonify({"msg": "Email already exists"}), 400

    user = User(username=username, email=email, password=password)
    result = users_collection.insert_one(user.to_dict())
    return jsonify(str(result.inserted_id)), 201

@app.route('/profile')
@jwt_required()
def profile():
    current_user_id = get_jwt_identity()
    user = users_collection.find_one({'_id': current_user_id})
    if user:
        return jsonify(User.from_mongo(user).to_dict())
    else:
        return jsonify({"msg": "User not found"}), 404