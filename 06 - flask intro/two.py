from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def greet():
    return "Welcome"

@app.route("/products", methods=["GET", "POST"])
def get_products():
    if request.method == "GET":
        return "All products"
    
    if request.method == "POST":
        return "Product created"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return "Login page"
    
    if request.method == "POST":
        return "Login submitted"

if __name__ == "__main__":
    app.run(debug=True)