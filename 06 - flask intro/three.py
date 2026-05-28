# Concept 1 — Route Parameters
# By default Flask treats the route parameters as string but it supports converters as well.

from flask import Flask, request

app = Flask(__name__)

# By default id is treated as a string
# <class 'str'>
@app.route("/product/<id>")
def product(id):
    print(type(id))
    return f"Product id is {id}"

# <class 'int'>
@app.route("/products/<int:id>")
def products(id):
    print(type(id))
    return f"Product id is {id}"

# | Converter | Example          |
# | --------- | ---------------- |
# | string    | `<name>`         |
# | int       | `<int:id>`       |
# | float     | `<float:price>`  |
# | path      | `<path:url>`     |
# | uuid      | `<uuid:user_id>` |


# Concept 2 — Query Parameters
# Example: /products?category=mobile - This is not route parameter, this is query parameter.

# To access the query parameters use request.args

# Route Param - Used for: specific resource like IDs
# Query Param - Optional usually. Used for: filtering, searching, sorting, pagination.

@app.route("/user/<name>")
def get_name(name):
    return f"Hello  {name}"

@app.route("/search")
def get_products():
    q = request.args.get("q")
    return f"You searched for {q}"

@app.route("/filter")
def get_details():
    category = request.args.get("category")
    price = request.args.get("price")
    return f"Category: {category}, Price: {price}"

# request : You’ll use it constantly for: query params, json body, form data, files, headers, cookies.

if __name__ == "__main__":
    app.run(debug=True)