from flask import Blueprint, Response, redirect, url_for

base_bp = Blueprint("base", __name__, template_folder="templates")


@base_bp.route("/")
def index() -> Response:
    return redirect(url_for("products.product_list"))
