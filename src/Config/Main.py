from flask import Flask, jsonify
from .Types import *

from datetime import timedelta


app                                          = Flask(__name__, template_folder='../Templates', static_folder='../Static')
app.config['SECRET_KEY']                     = SECRET_KEY
app.config['CACHE_TYPE']                     = "redis"
app.config['CACHE_DEFAULT_TIMEOUT']          = 604800  # 1 week cache time duration in seconds
app.config['CACHE_REDIS_URL']                = "redis://mercari_redis_auth_services:6379"
app.config['SQLALCHEMY_DATABASE_URI']        = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"]                 = SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"]       = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"]      = timedelta(days=30)
app.config['JWT_BLACKLIST_ENABLED']          = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS']     = ['access', 'refresh']

# 404 handling
@app.errorhandler(404)
def page_not_found(e):
    data = {
        "Status": 404,
        "Message": 'Not Found.'
    }

    return jsonify(data), 404