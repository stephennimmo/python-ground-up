from sqlalchemy.orm import Session
from src.customer.repository import CustomerRepository, CustomerBase
from src.customer.schema import Customer


class CustomerService:

    def __init__(self):
        self._customer_repository = CustomerRepository()

    def find_all(self, session: Session) -> list[Customer]:
        customers = self._customer_repository.find_all(session)
        return [Customer.model_validate(customer) for customer in customers]

    def find_by_id(self, session: Session, customer_id: int) -> Customer | None:
        customer_base = self._customer_repository.find_by_id(session, customer_id)
        return Customer.model_validate(customer_base) if customer_base else None

    def find_by_email(self, session: Session, email: str) -> Customer | None:
        customer_base = self._customer_repository.find_by_email(session, email)
        return Customer.model_validate(customer_base) if customer_base else None

    def create(self, session: Session, customer: Customer) -> Customer:
        customer_base = CustomerBase(first_name=customer.first_name, middle_name=customer.middle_name,
                                   last_name=customer.last_name, suffix=customer.suffix, email=customer.email,
                                   phone=customer.phone)
        customer_base = self._customer_repository.create(session, customer_base)
        return Customer.model_validate(customer_base)

    def update(self, session: Session, customer: Customer) -> Customer:
        customer_base = CustomerBase(customer_id=customer.customer_id, first_name=customer.first_name, middle_name=customer.middle_name, last_name=customer.last_name,
                                   suffix=customer.suffix, email=customer.email, phone=customer.phone)
        customer_base = self._customer_repository.update(session, customer_base)
        return Customer.model_validate(customer_base)
