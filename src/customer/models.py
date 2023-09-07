from sqlalchemy import Column, Integer, Text
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