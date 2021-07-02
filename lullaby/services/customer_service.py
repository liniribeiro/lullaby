from typing import Dict

from lullaby.database.models import Customer
from lullaby.database.queries import get_by_id, get_all, save, update_customer
from lullaby.exceptions import DuplicatedEmailError, CustomerNotFoundError
from lullaby.schemas.customer_schema import CustomerSchemaModel, CustomerOutputList


def get_customers():
    customers = get_all(Customer)
    return get_customer_output(customers)


def save_customers(customers: Dict):
    try:
        return save(Customer, customers)
    except Exception as e:
        raise DuplicatedEmailError()


def update_customers(customers: Dict, request_id):
    try:
        return update_customer(request_id, customers.get('name'), customers.get('email'))
    except Exception as e:
        raise DuplicatedEmailError()


def get_customer(customer_id):
    try:
        return get_by_id(Customer, customer_id)
    except Exception as e:
        raise CustomerNotFoundError()


def get_customer_output(customers_dict):
    mapped_output = [CustomerSchemaModel(customer) for customer in customers_dict]
    schema = CustomerOutputList()
    schema.customers = mapped_output
    return schema
