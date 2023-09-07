from typing import Type
from sqlalchemy.orm import Session

from python_ground_up.customer.models import CustomerBase


class CustomerRepository:

    def find_all(self, session: Session) -> list[Type[CustomerBase]]:
        return session.query(CustomerBase).all()

    def find_by_id(self, session: Session, customer_id: int) -> CustomerBase | None:
        return session.query(CustomerBase.customer_id).filter(CustomerBase.customer_id == customer_id).scalar()

    def find_by_email(self, session: Session, email: str) -> CustomerBase | None:
        return session.query(CustomerBase).filter(CustomerBase.email == email).scalar()

    def create(self, session: Session, customer_base: CustomerBase) -> CustomerBase:
        session.add(customer_base)
        session.commit()
        session.refresh(customer_base)
        return customer_base

    def update(self, session: Session, customer_base: CustomerBase) -> CustomerBase:
        customer = self.find_by_id(session, customer_base.customer_id)
        customer.first_name = customer_base.first_name
        customer.middle_name = customer_base.middle_name
        customer.last_name = customer_base.last_name
        customer.suffix = customer_base.suffix
        customer.email = customer_base.email
        customer.phone = customer_base.phone
        session.commit()
        return customer_base
