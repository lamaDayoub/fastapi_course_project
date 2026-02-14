from fastapi import APIRouter, Depends, status, HTTPException
from .. import database, schemas, models, hashing
from sqlalchemy.orm import Session 



router = APIRouter()
get_db=database.get_db
@router.post('/user',status_code=status.HTTP_201_CREATED,response_model=schemas.ShowUser, tags=["users"])
def create_user(request : schemas.User ,  db : Session = Depends(get_db)  ):
    hashed_password = hashing.Hash.bcrypt(request.password)
    new_user = models.User(name= request.name , email = request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/user/{id}',response_model=schemas.ShowUser, status_code=status.HTTP_200_OK, tags=["users"])
def show_user(id:int, db:Session= Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f'the user with id {id} is not available')
    return user