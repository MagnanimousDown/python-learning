from flask import Blueprint, jsonify

products_bp = Blueprint(
    "products",
    __name__,
    url_prefix = "/products"
)

@products_bp.route("/", methods=["GET"])
def get_all_products():
    return jsonify({
        "message": "all products"
    }), 200

@products_bp.route("/<int:id>", methods=["GET"])
def get_product_by_id(id):

    if id != 1:
        return jsonify({
            "message": f"no product found with id {id}"
        }), 404

    return jsonify({
        "id": 1
    }), 200