from flask import Flask, request, jsonify
from db import get_connection

app = Flask(__name__)

@app.route("/users", methods=["POST"])
def create_user():

    data = request.get_json()

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO Users (name, email)
        VALUES (?, ?)
        """,
        (
            data["name"],
            data["email"]
        )
    )

    conn.commit()

    conn.close()

    return jsonify({
        "message": "User created"
    }), 201

@app.route("/users", methods=["GET"])
def get_users():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, name, email
        FROM Users
        """
    )

    rows = cursor.fetchall()

    users = []

    for user in rows:
        users.append({
            "id": user.id,
            "name": user.name,
            "email": user.email
        })

    conn.close()

    return jsonify(users)

@app.route("/users/<int:id>", methods=["GET"])
def get_user_by_id(id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, name, email
        FROM Users
        WHERE id = ?
        """, (id)
    )

    user = cursor.fetchone()

    conn.close()

    if not user:
        return jsonify({
            "error": "User not found"
        }), 404

    return jsonify({
        "name": user.name,
        "email": user.email
    }), 200

@app.route("/users/<int:id>", methods=["PUT"])
def update_name_by_id(id):

    data = request.get_json()
    
    if not data.get("name"):
        return jsonify({
            "error": "name is required"
        }), 400
    
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE Users
        SET name = ?
        WHERE id = ?
        """, (data.get("name"), id)
    )

    conn.commit()
    
    conn.close()

    return jsonify({
        "message": "user updated successfully"
    }), 200
    
@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    conn =  get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM Users
        WHERE id =  ?
        """, (id)
    )

    conn.commit()

    conn.close()

    return jsonify({
        "message": "User deleted successfully"
    }), 200

if __name__ == "__main__":
    app.run(debug=True)

