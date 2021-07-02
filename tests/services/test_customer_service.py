import unittest
from unittest.mock import patch

from lullaby.exceptions import DuplicatedEmailError, CustomerNotFoundError
from lullaby.schemas.customer_schema import CustomerSchemaModel, CustomerOutputList
from lullaby.services.customer_service import get_customers, save_customers, get_customer


class TestCustomerServices(unittest.TestCase):

    @patch('lullaby.services.customer_service.get_all')
    @patch('lullaby.services.customer_service.get_customer_output')
    def test_get_customers_should_return_customers(self, get_customer_output, get_all):
        customers = [{"name": "name1", "email": "email@email.com"}]
        get_all.return_value = customers

        customer_model = CustomerSchemaModel({"name": "name1", "email": "email@email.com"})
        schema = CustomerOutputList()
        schema.customers = [customer_model]

        get_customer_output.return_value = schema
        output = get_customers()
        assert output == schema

    @patch('lullaby.services.customer_service.get_all')
    @patch('lullaby.services.customer_service.get_customer_output')
    def test_get_customers_should_return_empty_customers(self, get_customer_output, get_all):
        customers = []
        get_all.return_value = customers
        get_customer_output.return_value = []
        output = get_customers()
        assert output == []

    @patch('lullaby.services.customer_service.save')
    def test_save_customers_should_save(self, save):
        customers = {"name": "name1", "email": "email@email.com"}
        customer_id = "1234"
        save.return_value = customer_id
        output = save_customers(customers)
        assert output == customer_id

    @patch('lullaby.services.customer_service.save')
    def test_save_customers_should_return_exception(self, save):
        customers = {"name": "name1", "email": "email@email.com"}
        save.side_effect = Exception()
        with self.assertRaises(DuplicatedEmailError) as context:
            save_customers(customers)

    @patch('lullaby.services.customer_service.get_by_id')
    def test_get_customers_should_return_customer(self, get_by_id):
        customer = {"name": "name1", "email": "email@email.com"}
        customer_id = "1234"
        get_by_id.return_value = customer
        output = get_customer(customer_id)
        assert output == customer

    @patch('lullaby.services.customer_service.get_by_id')
    def test_get_customers_should_return_exception(self, get_by_id):
        customer_id = "1234"
        get_by_id.side_effect = Exception()
        with self.assertRaises(CustomerNotFoundError) as context:
            get_customer(customer_id)
