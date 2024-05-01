from flask import jsonify, request
from bson.json_util import dumps
from . import mongo
from .models.playlist import Playlist

playlists_collection = mongo.db.playlists

@app.route('/playlists', methods=['POST'])
def create_playlist():
    data = request.get_json()
    playlist = Playlist.from_dict(data)
    result = playlists_collection.insert_one(playlist.to_dict())
    return jsonify(str(result.inserted_id))

@app.route('/playlists/<user_id>')
def get_playlists_by_user(user_id):
    playlists = playlists_collection.find({'user_id': user_id})
    return jsonify([Playlist.from_mongo(playlist).to_dict() for playlist in playlists])
