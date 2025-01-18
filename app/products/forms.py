from decimal import Decimal

from flask_babel import lazy_gettext
from flask_wtf import FlaskForm
from wtforms.fields.numeric import DecimalField
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired, NumberRange


class ProductForm(FlaskForm):
    index = StringField("index", validators=[DataRequired()])
    description = StringField("description", validators=[DataRequired()])
    quantity = DecimalField("quantity", validators=[NumberRange(min=0)], default=Decimal(0))
    unit = StringField("unit", validators=[DataRequired()], default=lazy_gettext("pcs"))
    price = DecimalField("price", validators=[NumberRange(min=0)], default=Decimal(0))
    notes = StringField("notes")


class ProductCreateForm(ProductForm):
    quantity = DecimalField("quantity", validators=[NumberRange(min=0.01)], default=Decimal(0))


class ProductUpdateForm(ProductForm):
    index = StringField("index", render_kw={"disabled": ""})
