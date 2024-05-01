from flask import jsonify, request
from bson.json_util import dumps
from . import mongo
from .models.playlist import Playlist
from bson.objectid import ObjectId


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

def update_playlist(playlist_id):
    data = request.get_json()
    updated_playlist = Playlist.from_dict(data)
    result = playlists_collection.update_one({'_id': ObjectId(playlist_id)}, {'$set': updated_playlist.to_dict()})
    return jsonify(result.modified_count)

@app.route('/playlists/<playlist_id>', methods=['DELETE'])
def delete_playlist(playlist_id):
    result = playlists_collection.delete_one({'_id': ObjectId(playlist_id)})
    return jsonify(result.deleted_count)

@app.route('/playlists/<playlist_id>', methods=['PUT'])
def update_playlist(playlist_id):
    data = request.get_json()
    updated_playlist = Playlist.from_dict(data)
    result = playlists_collection.update_one({'_id': ObjectId(playlist_id)}, {'$set': updated_playlist.to_dict()})
    if result.modified_count == 1:
        return jsonify({"msg": "Playlist updated successfully"}), 200
    else:
        return jsonify({"error": "Playlist not found or not updated"}), 404

@app.route('/playlists/<playlist_id>', methods=['DELETE'])
def delete_playlist(playlist_id):
    result = playlists_collection.delete_one({'_id': ObjectId(playlist_id)})
    if result.deleted_count == 1:
        return jsonify({"msg": "Playlist deleted successfully"}), 200
    else:
        return jsonify({"error": "Playlist not found or not deleted"}), 404