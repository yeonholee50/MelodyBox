from flask import jsonify, request
from bson.json_util import dumps
from . import mongo
from .models.user import User

users_collection = mongo.db.users

@app.route('/users/<user_id>')
def get_user_info(user_id):
    user = users_collection.find_one_or_404({'_id': ObjectId(user_id)})
    return jsonify(User.from_mongo(user).to_dict())

