from app.extensions import ma


class ProductDatasetSchema(ma.Schema):
    id = ma.Integer()
    index = ma.String()
    description = ma.String()
    quantity = ma.Float()


class ProductBaseSchema:
    id = ma.Integer()
    index = ma.String()
    description = ma.String()
    quantity = ma.Float()
    unit = ma.String()
    price = ma.Float()
    notes = ma.String()


class ProductSchema(ProductBaseSchema, ma.Schema):
    pass


class ProductHistorySchema(ProductBaseSchema, ma.Schema):
    date = ma.DateTime()
    product_id = ma.Integer()


class ProductExportSchema(ma.Schema):
    products = ma.Nested(ProductSchema, many=True)
    history = ma.Nested(ProductHistorySchema, many=True)
