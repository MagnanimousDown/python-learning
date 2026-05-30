# Returning json in flask
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/profile", methods=["GET"])
def profile_details():
    return jsonify({
        "name": "Omkar",
        "role": "Backend Developer"
    })

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify({
        "message": "User created",
        "data": data
    })

@app.route("/create-product", methods=["POST"])
def create_product():
    data = request.get_json()

    return jsonify({
        "status": "success",
        "product": data
    })


if __name__ == "__main__":
    app.run(debug=True)