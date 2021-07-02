from http import HTTPStatus
from typing import Type

from schematics import Model
from schematics.exceptions import DataError

from lullaby.database.queries import customer_exists
from lullaby.exceptions import PayloadError, NotAuthorizedError, CustomerNotFoundError
from lullaby.settings import API_KEY


def validate(received_request, customer_id=None, request_class: Type[Model] = None):
    validate_auth(received_request.headers.get('Authorization'))
    validate_schema(request_class, received_request.json)
    validate_customer(customer_id)


def validate_customer(customer_id):
    if customer_id and not customer_exists(customer_id):
        raise CustomerNotFoundError(status=HTTPStatus.NOT_FOUND)


def validate_auth(auth_header):
    api_key = auth_header
    if api_key != API_KEY:
        raise NotAuthorizedError(status=HTTPStatus.UNAUTHORIZED)


def validate_schema(request_class, body):
    if request_class:
        try:
            request_class(body).validate()
        except DataError as e:
            raise PayloadError(data=str(e), status=HTTPStatus.INTERNAL_SERVER_ERROR)
