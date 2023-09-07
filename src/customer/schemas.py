from pydantic import BaseModel, ConfigDict, EmailStr


class Customer(BaseModel):
    customer_id: int | None = None
    first_name: str
    middle_name: str | None = None
    last_name: str
    suffix: str | None = None
    email: EmailStr
    phone: str | None = None

    model_config = ConfigDict(from_attributes=True)
