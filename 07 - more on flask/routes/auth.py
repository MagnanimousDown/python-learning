from flask import Blueprint, jsonify

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix = "/auth"
)

@auth_bp.route("/login", methods=["GET"])
def login():
    return jsonify({
        "message": "login successful"
    }), 200

@auth_bp.route("/register", methods=["GET"])
def register():
    return jsonify({
        "message": "user registered successfully"
    }), 200
