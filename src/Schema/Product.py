from ..Config import ma
from ..Models import Product


class ProductSchemaList(ma.SQLAlchemyAutoSchema):
    class Meta:
        model      = Product
        include_fk = True