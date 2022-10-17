import time

from flask_restful import Resource
from flask import request

from ..Config import db
from ..Models import Product
from ..Schema import ProductSchemaList


class ProductDetailAPI(Resource):
    def post(self):
        """
        :target : API
        :return : Get Detail Product Data
        """

        # get data from formdata and transform it to dict
        body = request.form.to_dict()

        validate_string = [
            "product_code"
        ]

        if all(key in body for key in validate_string):
            # query are product exists
            query = Product.query \
                .filter(Product.product_code == body['product_code'])

            # check are product exists
            if query.count() == 0:
                datas = {
                    "status": "error",
                    "data": None,
                    "message": "Data product tidak ditemukan, coba dengan data lainnya."
                }

                return datas, 400

            product_schema = ProductSchemaList(many=True)
            output = product_schema.dump(query.all())

            result = {
                "status": 200,
                "data": output[0],
                "message": "Success"
            }

            return result, 200
        else:
            datas = {
                "status": "error",
                "data": None,
                "message": "Data yang di perlukan tidak lengkap, mohon periksa kembali."
            }

            return datas, 400
