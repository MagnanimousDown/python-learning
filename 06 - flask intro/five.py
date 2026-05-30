# Why input validation is necessary? - Never trust client input.

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/student", methods=["POST"])
def get_name():
    data = request.get_json()

    if not data.get("name"):
        return jsonify({
            "error": "Name is required"
        }), 400

    return jsonify({
        "message": "Student created"
    }), 201

@app.route("/employee", methods=["POST"])
def create_employee():
    data = request.get_json()

    required_fields = ["name", "department"]

    for field in required_fields:
        if not data.get(field):
            return jsonify({
                "error": f"{field} is required" 
            }), 400
    
    return jsonify({
        "message": "employee created"
    }), 201

@app.route("/product", methods=["POST"])
def create_product():
    data = request.get_json()

    required_fields = ["title", "price"]

    for field in required_fields:
        if not data.get(field):
            return jsonify({
                "error": f"{field} is required"
            }), 400

    return jsonify({
        "message": "product created",
        "data": data
    }), 201

@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify({
        "message": "pong"
    }), 200

@app.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    if id != 1:
        return jsonify({
            "error": "Book not found"
        }), 404

    return jsonify({
        "id": 1,
        "title": "Atomic Habits"
    }), 200

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data.get("username"):
        return jsonify({
            "error": "username is required"
        }), 400

    return jsonify({
        "message": "success"
    }), 201

if __name__ == "__main__":
    app.run(debug=True)