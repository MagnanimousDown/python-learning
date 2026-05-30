# Lesson 6 — Headers, Form Data, Cookies, and File Uploads
# A request can carry:
# Request
# │
# ├── Route Params      /users/10
# ├── Query Params      ?page=1
# ├── JSON Body         {"name":"Omkar"}
# ├── Headers           Authorization: Bearer xyz
# ├── Form Data         HTML forms
# ├── Cookies           Session info
# └── Files             Images, PDFs, Excel files



# Quick Summary
# | Data Source | Flask                   |
# | ----------- | ----------------------- |
# | Route Param | `<int:id>`              |
# | Query Param | `request.args.get()`    |
# | JSON Body   | `request.get_json()`    |
# | Header      | `request.headers.get()` |
# | Form        | `request.form.get()`    |
# | Cookie      | `request.cookies.get()` |
# | File        | `request.files`         |

from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

# Headers - Access them using: request.headers
@app.route("/check-header", methods=["GET"])
def read_header():
    x_user = request.headers.get("x-user")

    print(x_user)
    return jsonify({
        "user": x_user
    })

@app.route("/login-form", methods=["POST"])
def login_form():
    username = request.form.get("username")
    password = request.form.get("password")

    return jsonify({
        "username": username,
        "password": password,
        "message": "received"
    })

@app.route("/set-theme", methods=["GET"])
def set_theme():
    response = make_response("Theme cookie set")

    response.set_cookie(
        "theme",
        "dark"
    )

    return response

@app.route("/get-theme", methods=["GET"])
def get_theme():
    theme = request.cookies.get("theme")

    return jsonify({
        "theme": theme
    })

if __name__ == "__main__":
    app.run(debug=True)