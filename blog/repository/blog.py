from .. import models,schemas
from sqlalchemy.orm  import Session

from fastapi import status, Response, HTTPException

def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog,db:Session):
    # db: Session: This is your "link" to the database. You will use this variable to perform #your CRUD operations (like db.add() or db.query()).
    blog_data=request.model_dump()
    blog_data['user_id']=1
    new_blog = models.Blog(**blog_data)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id:int,db:Session):
    blog =db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        # This raises a 404 error if the blog isn't found
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def update(id:int,db:Session, request:schemas.Blog):
    blog =  db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    updated_data = request.model_dump()
    
    blog.update(updated_data)
    db.commit()
    return 'updated'

def get_one(db:Session,id:int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f'the blog with id {id} is not available')
        # response.status_code  = status.HTTP_404_NOT_FOUND
        # return {'detail':f'the blog with id {id} is not available'}
    return blog