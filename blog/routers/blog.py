from typing import List
from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session 
from .. import schemas, database, oauth2
from ..repository import blog

router = APIRouter()

get_db = database.get_db



@router.get('/',response_model=List[schemas.showBlog]) #db : Session = #Depends(get_db)  is a database instance
def get_all(db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    #we are querying on blog from models 
    
    return blog.get_all(db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model = schemas.showBlog)
def get_one(id:int, response : Response, db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user) ):
   return blog.get_one(db,id)




@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog (request : schemas.Blog, db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request,db)


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog.destroy(id,db)


@router.put('blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id,db,request)
