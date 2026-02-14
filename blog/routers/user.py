from fastapi import APIRouter, Depends, status, HTTPException
from .. import database, schemas, models, hashing
from sqlalchemy.orm import Session 
from ..repository import user


router = APIRouter()
get_db=database.get_db
@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.ShowUser)
def create_user(request : schemas.User ,  db : Session = Depends(get_db)  ):
    return user.create(db,request)


@router.get('/{id}',response_model=schemas.ShowUser, status_code=status.HTTP_200_OK)
def show_user(id:int, db:Session= Depends(get_db)):
    return user.get_one(db,id)