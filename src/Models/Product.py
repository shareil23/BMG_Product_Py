from ..Config import db

import time


class Product(db.Model):
    __tablename__ = 'product'

    id           = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    product_name = db.Column(db.Text())
    product_code = db.Column(db.Integer())
    cdate_time   = db.Column(db.Integer())
    udate_time   = db.Column(db.Integer())

    def __init__(self, **data):
        self.product_name = data['product_name']
        self.product_code = data['product_code']
        self.cdate_time   = time.time()
        self.udate_time   = data['udate_time']
