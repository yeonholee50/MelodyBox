from bson.objectid import ObjectId

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email
        }

    @staticmethod
    def from_dict(user_dict):
        return User(
            username=user_dict.get('username'),
            email=user_dict.get('email')
        )

    @staticmethod
    def from_mongo(mongo_doc):
        return User(
            username=mongo_doc.get('username'),
            email=mongo_doc.get('email')
        )

