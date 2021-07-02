from http import HTTPStatus

from flask import request
from flask_restful import Resource

from lullaby.database.queries import delete_favorite
from lullaby.exceptions import Error
from lullaby.schemas.customer_schema import SaveFavoriteInput
from lullaby.services.favorite_service import add_favorite, get_customer_favorites,  get_favorite
from lullaby.services.validation_service import validate


class FavoriteListHandler(Resource):

    @staticmethod
    def get(customer_id):
        try:
            validate(request, customer_id)
            favorites = get_customer_favorites(customer_id)
            return favorites.serialize(), HTTPStatus.OK
        except Error as e:
            return str(e), e.status

    @staticmethod
    def post(customer_id):
        try:
            validate(request, customer_id, SaveFavoriteInput)
            payload = request.json
            add_favorite(payload, customer_id)
            return '', HTTPStatus.OK
        except Error as e:
            return str(e), HTTPStatus.INTERNAL_SERVER_ERROR


class FavoriteHandler(Resource):

    @staticmethod
    def get(customer_id, product_id):
        try:
            validate(request, customer_id)
            response = get_favorite(customer_id, product_id)
            return response.serialize(), HTTPStatus.OK
        except Error as e:
            return str(e), e.status

    @staticmethod
    def delete(customer_id, product_id):
        try:
            validate(request, customer_id)
            delete_favorite(customer_id, product_id)
            return '', HTTPStatus.NO_CONTENT
        except Error as e:
            return str(e), e.status


