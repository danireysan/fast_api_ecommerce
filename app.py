from fastapi import FastAPI

from routes.user import user
app = FastAPI(
    openapi_tags=[{
        "name": "users",
        "description": "user routes " 
        
    }]
)

app.include_router(user)