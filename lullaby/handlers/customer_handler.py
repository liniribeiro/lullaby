from http import HTTPStatus

from flask import request
from flask_restful import Resource


from lullaby.database.queries import delete_customer
from lullaby.exceptions import Error
from lullaby.schemas.customer_schema import SaveCustomerInput, CustomerSchemaModel
from lullaby.services.customer_service import get_customers, save_customers, update_customers, get_customer
from lullaby.services.validation_service import validate


class CustomerListHandler(Resource):

    @staticmethod
    def get():
        try:
            validate(request)
            response = get_customers()
            return response.serialize(), HTTPStatus.OK
        except Error as e:
            return str(e), e.status

    @staticmethod
    def post():
        try:
            validate(request, request_class=SaveCustomerInput)
            payload = request.json
            saved_id = save_customers(payload)
            return {"id": saved_id}, HTTPStatus.OK
        except Error as e:
            return str(e), e.status


class CustomerHandler(Resource):

    @staticmethod
    def get(customer_id):
        try:
            validate(request, customer_id)
            response = get_customer(customer_id)
            return CustomerSchemaModel(response).serialize(), HTTPStatus.OK
        except Error as e:
            return str(e),e.status

    @staticmethod
    def delete(customer_id):
        try:
            validate(request, customer_id)
            delete_customer(customer_id)
            return '', HTTPStatus.NO_CONTENT
        except Error as e:
            return str(e), e.status

    @staticmethod
    def put(customer_id):
        try:
            validate(request, customer_id)
            payload = request.json
            update_customers(payload, customer_id)
            return '', 201
        except Error as e:
            return str(e), HTTPStatus.INTERNAL_SERVER_ERROR

    @staticmethod
    def patch(customer_id):
        try:
            validate(request, customer_id)
            payload = request.json
            update_customers(payload, customer_id)
            return '', 201
        except Error as e:
            return str(e), HTTPStatus.INTERNAL_SERVER_ERROR
