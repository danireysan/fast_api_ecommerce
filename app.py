from fastapi import FastAPI

from routes.user import user
from routes.product import product
app = FastAPI(
    openapi_tags=[{
        "name": "users",
        "description": "user routes " 
        
    }]
)

app.include_router(user)
app.include_router(product)