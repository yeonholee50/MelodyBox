from flask import jsonify, request
from . import mongo

songs_collection = mongo.db.songs

@app.route('/playlists/<playlist_id>/songs', methods=['POST'])
def add_song_to_playlist(playlist_id):
    data = request.get_json()
    song_id = data.get('song_id')
    song_info = songs_collection.find_one({'_id': song_id})
    if song_info:
        playlists_collection.update_one(
            {'_id': ObjectId(playlist_id)},
            {'$addToSet': {'songs': song_info}}
        )
        return jsonify({"msg": "Song added to playlist successfully"}), 200
    else:
        return jsonify({"error": "Song not found"}), 404
