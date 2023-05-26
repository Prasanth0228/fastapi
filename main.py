import uvicorn
from fastapi import FastAPI
from fastapi import FastAPI, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi import FastAPI, Header,Request
from typing import List, Union
from routes.api import router as api_router
from database import Base
from database import SessionLocal
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
import models
from database import engine
import logging

# setup loggers
#logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)  # the __name__ resolve to "main" since we are at the root of the project.
                                      # This will get the root logger since no logger in the configuration has this name.

app = FastAPI()

# kabilan
from starlette.middleware.cors import CORSMiddleware
origins = [
    "https://reverpro.com/fastapi",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router)
@app.get("/")
def read_root():
    return {"message": "welcome to FastAPI!"}





@app.get("/authtoken")
async def root(request: Request):
    my_header = request.headers.get('authorization')
    return {"header":my_header}

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html(req: Request):
    root_path = req.scope.get("root_path", "").rstrip("/")
    openapi_url = root_path + app.openapi_url
    return get_swagger_ui_html(
        openapi_url=openapi_url,
        title="API",
    )


uvicorn.run(app, host="127.0.0.1", port=10048)
