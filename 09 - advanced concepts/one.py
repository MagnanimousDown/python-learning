# Understanding Decorators and sessions

# Decorators 
# def logger(func):
#     def wrapper():
#         print("Starting...")
#         func()
#         print("Finished...")

#     return wrapper

# @logger
# def greet():
#     print("Hello")

# greet()

# session in flask

from flask import Flask, session, jsonify, request

app = Flask(__name__)

app.secret_key = "my-super-secret-key"

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
        "message": "Logged in"
    }), 200

@app.route("/profile", methods=["GET"])
def get_profile():
    
    if not session.get("user"):
        return jsonify({
            "error": "Not logged in"
        }), 401

    return jsonify({
        "user": session.get("user")
    })

@app.route("/logout", methods=["GET"])
def logout():

    session.pop("user", None)

    return jsonify({
        "message": "Logged out"
    })

if __name__ == "__main__":
    app.run(debug=True)