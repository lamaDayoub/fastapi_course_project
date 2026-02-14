from fastapi import FastAPI
from . import  models
from .database import engine

from .routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(authentication.router, tags=['authentication'])
app.include_router(blog.router, tags=["blogs"],prefix='/blog')
app.include_router(user.router, tags=["users"],prefix='/user')

