from datetime import datetime, timezone
from io import BytesIO
from typing import NoReturn

from sqlalchemy.orm import Query

from app.extensions import db
from app.products.models import Product, ProductHistory
from app.products.schemas import ProductExportSchema


class ProductService:
    def get_all_products(self) -> Query[Product]:
        return db.session.query(Product).order_by(Product.id).all()

    def get_product_by_id(self, product_id: int) -> Product:
        return db.session.query(Product).where(Product.id == product_id).one()

    def create_product(self, data: dict) -> Product:
        return self.update_product(Product(), data)

    def update_product(self, product: Product, data: dict) -> Product:
        for key in ProductHistory.data_fields:
            setattr(product, key, data.get(key))

        db.session.add(product)
        db.session.flush()

        product_history = ProductHistoryService().create_history(product)

        db.session.add(product_history)
        db.session.commit()

        return product

    def delete_product(self, product: Product) -> NoReturn:
        raise NotImplementedError

    def get_export_file(self) -> tuple[BytesIO, str]:
        products_all = self.get_all_products()
        history_all = ProductHistoryService().get_all_history()

        data = ProductExportSchema().dumps({"products": products_all, "history": history_all})
        filename = datetime.now(timezone.utc).strftime("im3-%Y%m%dT%H%M.json")

        file = BytesIO()
        file.write(data.encode())
        file.seek(0)

        return file, filename


class ProductHistoryService:
    def get_all_history(self) -> Query[ProductHistory]:
        return db.session.query(ProductHistory).order_by(ProductHistory.date.desc()).all()

    def get_history_by_product_id(self, product_id: int) -> Query[ProductHistory]:
        return (
            db.session.query(ProductHistory)
            .order_by(ProductHistory.date.desc())
            .where(ProductHistory.product_id == product_id)
        )

    def create_history(self, product: Product) -> ProductHistory:
        history = ProductHistory()
        history.date = datetime.now(timezone.utc)
        history.product_id = product.id

        for key in ProductHistory.data_fields:
            setattr(history, key, getattr(product, key))

        return history
