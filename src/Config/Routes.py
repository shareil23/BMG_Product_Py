from ..Controller import *
from .Config import api

def Routes(api):
    api.add_resource(ProductDetailAPI, '/api/v1/product/detail')
    api.add_resource(ProductAPI, '/api/v1/product', '/api/v1/product/<int:page>/<int:totalData>')

Routes(api)