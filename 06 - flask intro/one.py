from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello flask!"

@app.route("/about")
def about():
    return "This is about page"

@app.route("/contact")
def contact():
    return "contact us"

@app.route("/user")
def greet():
    return "Welcome user"

if __name__ == "__main__":
    app.run(debug=True)