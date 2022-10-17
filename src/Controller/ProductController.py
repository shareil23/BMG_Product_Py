import time

from flask_restful import Resource
from flask import request
import math

from ..Config import db
from ..Models import Product
from ..Schema import ProductSchemaList


class ProductAPI(Resource):
    def get(self, page=1, totalData=10):
        """
        :target : API
        :return : Get All Product Data
        """

        # query product data
        query = Product.query \
            .order_by(Product.udate_time.desc()) \
            .paginate(page, totalData, False)

        # get product data
        product_schema = ProductSchemaList(many=True)
        output         = product_schema.dump(query.items)

        # check the data is exists
        if len(output) == 0:
            result = {
                "status": 400,
                "data": None,
                "message": "Data product tidak ditemukan.",
                "totalPage": math.ceil(Product.query.count() / totalData),
                "totalData": Product.query.count()
            }
            return result, 400

        result = {
            "status": 200,
            "data": output,
            "message": "Success",
            "totalPage": math.ceil(Product.query.count() / totalData),
            "totalData": Product.query.count()
        }

        return result, 200

    def post(self):
        """
        :target : API
        :return : Insert New Product Data
        """

        # get data from formdata and transform it to dict
        body = request.form.to_dict()

        validate_string = [
            "product_name",
            "product_code"
        ]

        if all(key in body for key in validate_string):
            # init utime
            body['udate_time'] = 0

            # query are product exists
            query = Product.query \
                .filter(Product.product_code == body['product_code']) \
                .filter(Product.product_name == body['product_name']) \
                .count()

            # check are product exists
            if query != 0:
                datas = {
                    "status": "error",
                    "data": None,
                    "message": "Data product sudah digunakan, coba dengan data lainnya."
                }

                return datas, 400

            # insert user data to database
            user_insert_data = Product(**body)
            db.session.add(user_insert_data)
            db.session.commit()
            db.session.flush()

            datas = {
                "status": "success",
                "data": None,
                "message": "Product berhasil di input"
            }

            return datas, 200
        else:
            datas = {
                "status": "error",
                "data": None,
                "message": "Data yang di perlukan tidak lengkap, mohon periksa kembali."
            }

            return datas, 400

    def patch(self):
        """
        :target : API
        :return : Update Product Data
        """

        # get data from formdata and transform it to dict
        body = request.form.to_dict()

        validate_string = [
            "product_name",
            "product_code"
        ]

        if all(key in body for key in validate_string):
            # init utime
            body['udate_time'] = time.time()

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

            # insert user data to database
            query.update(body)
            db.session.commit()
            db.session.flush()

            datas = {
                "status": "success",
                "data": None,
                "message": "Product berhasil di update"
            }

            return datas, 200
        else:
            datas = {
                "status": "error",
                "data": None,
                "message": "Data yang di perlukan tidak lengkap, mohon periksa kembali."
            }

            return datas, 400

    def delete(self):
        """
        :target : API
        :return : Delete Product Data
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

            # delete user data to database
            db.session.delete(query.one())
            db.session.commit()
            db.session.flush()

            datas = {
                "status": "success",
                "data": None,
                "message": "Product berhasil di hapus"
            }

            return datas, 200
        else:
            datas = {
                "status": "error",
                "data": None,
                "message": "Data yang di perlukan tidak lengkap, mohon periksa kembali."
            }

            return datas, 400