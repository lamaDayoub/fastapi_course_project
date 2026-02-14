from .. import models,schemas
from sqlalchemy.orm  import Session
from .. import hashing

from fastapi import status, HTTPException

def create(db:Session,request:schemas.User ):
    hashed_password = hashing.Hash.bcrypt(request.password)
    new_user = models.User(name= request.name , email = request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_one(db:Session,id:int):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f'the user with id {id} is not available')
    return user
