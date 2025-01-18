from datetime import datetime, timezone

from flask import Blueprint, Response, abort, redirect, render_template, send_file, url_for
from sqlalchemy.exc import NoResultFound

from app.products.forms import ProductCreateForm, ProductUpdateForm
from app.products.schemas import ProductDatasetSchema
from app.products.services import ProductHistoryService, ProductService

products_bp = Blueprint("products", __name__, url_prefix="/products", template_folder="templates")


@products_bp.route("/")
def product_list() -> Response | str:
    products_all = ProductService().get_all_products()
    products = [p for p in products_all if p.quantity > 0]

    context = {
        "products": products_all,
        "products_count": len(products),
        "products_total": sum(p.total for p in products),
        # ---
        "serializer": ProductDatasetSchema(),
        "now": datetime.now(timezone.utc),
    }

    return render_template("product_list.html", **context)


@products_bp.route("/new", methods=("GET", "POST"))
def product_add() -> Response | str:
    products_all = ProductService().get_all_products()
    form = ProductCreateForm()

    if form.validate_on_submit():
        data = form.data
        data.pop("csrf_token")
        product = ProductService().create_product(data)
        return redirect(url_for("products.product_list", _anchor=str(product.id)))

    context = {
        "form": form,
        "related": products_all,
        # ---
        "serializer": ProductDatasetSchema(),
    }

    return render_template("product_edit.html", **context)


@products_bp.route("/<int:product_id>", methods=("GET", "POST"))
def product_edit(product_id: int) -> Response | str:
    try:
        product = ProductService().get_product_by_id(product_id)
    except NoResultFound:
        abort(404)

    form = ProductUpdateForm(obj=product)

    if form.validate_on_submit():
        data = form.data
        data.pop("csrf_token")
        ProductService().update_product(product, data)
        return redirect(url_for("products.product_list", _anchor=str(product_id)))

    context = {
        "form": form,
        "product": product,
        "history": ProductHistoryService().get_history_by_product_id(product.id),
    }

    return render_template("product_edit.html", **context)


@products_bp.route("/export")
def product_export() -> Response:
    file, filename = ProductService().get_export_file()
    return send_file(file, as_attachment=True, download_name=filename)
