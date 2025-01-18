from decimal import ROUND_HALF_EVEN, Decimal

from app.base.models import UTCDateTime
from app.extensions import db


class ProductBase:
    data_fields = ("index", "description", "quantity", "unit", "price", "notes")

    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    quantity = db.Column(db.Numeric(10, 2), nullable=False)
    unit = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    notes = db.Column(db.Text)

    @property
    def total(self) -> Decimal:
        result = self.quantity * self.price
        return result.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)


class Product(ProductBase, db.Model):
    history = db.relationship("ProductHistory", backref="product", lazy=True)


class ProductHistory(ProductBase, db.Model):
    date = db.Column(UTCDateTime, nullable=False)
    product_id = db.Column(
        db.Integer,
        db.ForeignKey("product.id", ondelete="RESTRICT"),
        nullable=False,
    )
