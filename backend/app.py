from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from .controllers import user_controller, playlist_controller
from pymongo.errors import PyMongoError
from . import config

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/melodybox'
mongo = PyMongo(app)
app.config['JWT_SECRET_KEY'] = config.JWT_SECRET_KEY
jwt = JWTManager(app)

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(PyMongoError)
def handle_mongo_error(error):
    return jsonify({"error": "Database error"}), 500

@app.errorhandler(Exception)
def handle_generic_error(error):
    return jsonify({"error": "An unexpected error occurred"}), 500

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)

