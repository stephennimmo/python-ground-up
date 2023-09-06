from fastapi import FastAPI

from src.customer.api import router as customer_api

app = FastAPI(title='Customer API', version='0.0.1', separate_input_output_schemas=False)

app.include_router(customer_api, prefix="/v1")
