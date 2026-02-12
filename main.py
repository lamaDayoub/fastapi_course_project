from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()


class Blog(BaseModel):
    title: str
    body:str
    published:Optional[bool]=True

@app.get('/')
def hello():
    return {"details" : {'name':'lama'}}

@app.post('/blog/create')
def create_blog(blog:Blog):
    return blog.title