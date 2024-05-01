from flask import jsonify

# Example route for retrieving user information
def get_user_info(user_id):
    # Replace this with actual logic to fetch user info from database
    user_info = {
        "id": user_id,
        "username": "john_doe",
        "email": "john@example.com"
    }
    return jsonify(user_info)
