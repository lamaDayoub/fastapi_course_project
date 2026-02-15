from pydantic import BaseModel
from typing import List
#This defines how data looks when it enters or leaves the API (the "validation" and #"formatting" layer)
class Blog(BaseModel):
    title:str
    body:str
    

class User(BaseModel):
    name:str
    email:str
    password:str
    class Config():
        from_attributes = True
        
class ShowUser(BaseModel):
    name:str
    email:str
    blogs:List['Blog']=[]
    class Config():
        from_attributes = True
    

class showBlog(Blog):
    creator:ShowUser
    
#It tells Pydantic:
#"If you don't find a dictionary key, don't crash. Try looking for an attribute (a dot) #instead." because Pydantic (The Schema): By default, expects data as a Dictionary. and       SQLAlchemy (The ORM) Returns data as Objects so they speak two different languages
    class Config():
        from_attributes = True
        
class Login(BaseModel):
    username : str
    password: str
        
        
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None