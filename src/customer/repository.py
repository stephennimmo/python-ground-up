from typing import Type, Optional, List

from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import Session, DeclarativeBase
from sqlalchemy_utils import EmailType

from src.database import Base


class CustomerBase(Base):
    __tablename__ = "customer"

    customer_id = Column('customer_id', Integer, primary_key=True)
    first_name = Column('first_name', Text, nullable=False)
    middle_name = Column('middle_name', Text)
    last_name = Column('last_name', Text, nullable=False)
    suffix = Column('suffix', Text)
    email = Column('email', EmailType, nullable=False, unique=True)
    phone = Column('phone', Text)


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
