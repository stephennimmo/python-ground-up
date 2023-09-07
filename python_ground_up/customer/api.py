from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from python_ground_up.database import get_session
from python_ground_up.customer.schemas import Customer
from python_ground_up.customer.service import CustomerService

router = APIRouter(tags=["customer"])
customer_service = CustomerService()


@router.get("/customers", response_model=list[Customer])
def get(session: Session = Depends(get_session)) -> list[Customer]:
    return customer_service.find_all(session)


@router.get("/customers/{customer_id}", response_model=Customer)
def get_by_id(customer_id: int, session: Session = Depends(get_session)) -> Customer:
    customer = customer_service.find_by_id(session, customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail=f"Customer not found for customer_id[{customer_id}]")
    return customer


@router.post("/customers", response_model=Customer)
def create(customer: Customer, session: Session = Depends(get_session)) -> JSONResponse:
    if customer.customer_id is not None:
        raise HTTPException(status_code=400, detail=f"Customer object cannot contain customer_id[{customer.customer_id}]")
    existing_customer = customer_service.find_by_email(session, customer.email)
    if existing_customer is not None:
        raise HTTPException(status_code=400, detail=f"Customer already exists for email[{customer.email}]")
    new_customer = customer_service.create(session, customer)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder(new_customer))
