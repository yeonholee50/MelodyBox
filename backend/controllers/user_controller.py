from flask import jsonify, request
from bson.json_util import dumps
from . import mongo
from .models.user import User

users_collection = mongo.db.users

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