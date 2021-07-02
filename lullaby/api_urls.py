from flask_restful import Api

from lullaby.handlers.customer_handler import CustomerListHandler, CustomerHandler
from lullaby.handlers.favorite_handler import FavoriteListHandler, FavoriteHandler


def init_resources(app):
    api = Api(app)
    api.add_resource(CustomerListHandler, '/api/customer')
    api.add_resource(CustomerHandler, '/api/customer/<customer_id>')
    api.add_resource(FavoriteListHandler, '/api/customer/<customer_id>/favorite')
    api.add_resource(FavoriteHandler, '/api/customer/<customer_id>/favorite/<product_id>')
