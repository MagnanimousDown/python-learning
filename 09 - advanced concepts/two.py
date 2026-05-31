from flask import Flask, jsonify, request, session
from functools import wraps

app = Flask(__name__)

app.secret_key = "my-super-secret-key"

def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        if not session.get("user"):
            return jsonify({
                "error": "not logged in"
            }), 401

        return func(*args, **kwargs)    
    return wrapper

    
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    fields_required = ["username", "password"]
    
    for field in fields_required:
        if not data.get(field):
            return jsonify({
                "error": f"{field} is required"
            }), 400

    session["user"] = data.get("username")

    return jsonify({
        "message": "logged in successfully"
    })

@app.route("/dashboard", methods=["GET"])
@login_required
def get_dashboard():
    return jsonify({
        "message": "Welcome to dashboard"
    }), 200

@app.route("/settings", methods=["GET"])
@login_required
def get_settings():
    return jsonify({
        "message": "Settings page"
    }), 200

@app.route("/logout", methods=["GET"])
def logout():
    session.pop("user", None)

    return jsonify({
        "message": "Logged out"
    })

if __name__ == "__main__":
    app.run(debug=True)