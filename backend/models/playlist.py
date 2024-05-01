from bson.objectid import ObjectId

class Playlist:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def to_dict(self):
        return {
            "name": self.name,
            "user_id": self.user_id
        }

    @staticmethod
    def from_dict(playlist_dict):
        return Playlist(
            name=playlist_dict.get('name'),
            user_id=playlist_dict.get('user_id')
        )

    @staticmethod
    def from_mongo(mongo_doc):
        return Playlist(
            name=mongo_doc.get('name'),
            user_id=mongo_doc.get('user_id')
        )
