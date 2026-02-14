from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session 
from .. import schemas, database, models


router = APIRouter()

get_db = database.get_db

@router.get('/blog',response_model=List[schemas.showBlog], tags=["blogs"]) #db : Session = #Depends(get_db)  is a database instance
def get_all(db : Session = Depends(get_db)):
    #we are querying on blog from models 
    blogs = db.query(models.Blog).all()
    return blogs

@router.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model = schemas.showBlog, tags=["blogs"])
def get_one(id:int, response : Response, db : Session = Depends(get_db) ):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f'the blog with id {id} is not available')
        # response.status_code  = status.HTTP_404_NOT_FOUND
        # return {'detail':f'the blog with id {id} is not available'}
    return blog




@router.post('/blog', status_code=status.HTTP_201_CREATED, tags=["blogs"])
def create_blog (request : schemas.Blog, db : Session = Depends(get_db)):
    # db: Session: This is your "link" to the database. You will use this variable to perform #your CRUD operations (like db.add() or db.query()).
    blog_data=request.model_dump()
    blog_data['user_id']=1
    new_blog = models.Blog(**blog_data)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT, tags=["blogs"])
def delete_blog(id, db: Session = Depends(get_db)):
    blog =db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        # This raises a 404 error if the blog isn't found
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED, tags=["blogs"])
def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog =  db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    updated_data = request.model_dump()
    
    blog.update(updated_data)
    db.commit()
    return 'updated'
