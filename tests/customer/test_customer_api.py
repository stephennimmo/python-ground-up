import random
import string

from fastapi import status

from src.customer.schema import Customer
from tests.client import test_client


class TestCustomerApi:

    def test_get_customers(self):
        response = test_client.get("/v1/customers")
        assert response.status_code == status.HTTP_200_OK

    def test_create_customer(self):
        response = test_client.post("/v1/customers", json=self.new_customer().model_dump())
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["customer_id"] >= 0

    def new_customer(self) -> Customer:
        return Customer(
            first_name=''.join(random.choices(string.ascii_letters, k=10)),
            last_name=''.join(random.choices(string.ascii_letters, k=10)),
            email=f"{''.join(random.choices(string.ascii_letters, k=10))}@gmail.com"
        )