from fastapi import FastAPI,Depends,status, Response, HTTPException
from . import schemas, models
from .database import engine,SessionLocal
from sqlalchemy.orm import Session 
from typing import List
from passlib.context import CryptContext

app = FastAPI()
def get_db():
    #Before yield: FastAPI runs this part before your route starts (creates the session).
    #This creates a new, private session for a single request
    db = SessionLocal()
    try:
        yield db
    #even if the code crashes—always execute the code in finally
    finally:
        # Once your route has finished sending the response to the user, FastAPI "wakes up" #this function and runs the code after the yield (closing the session).
        db.close()
    


#like migrate in django it tells to make all tables from models.py if they are not created #befor in the database
models.Base.metadata.create_all(engine)

pwd_cxt = CryptContext(schemes=['bcrypt'],deprecated='auto')

#The Logic: This is a core FastAPI concept. that is saying: "Before you run this function, I #need you to go run get_db and give me a database session."
#It ensures that every request gets its own database connection and, most importantly, closes #it when the request is finished.
@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create_blog (request : schemas.Blog, db : Session = Depends(get_db)):
    # db: Session: This is your "link" to the database. You will use this variable to perform #your CRUD operations (like db.add() or db.query()).
    blog_data=request.model_dump()
    new_blog = models.Blog(**blog_data)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(get_db)):
    blog =db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        # This raises a 404 error if the blog isn't found
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog =  db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    updated_data = request.model_dump()
    
    blog.update(updated_data)
    db.commit()
    return 'updated'


@app.get('/blog',response_model=List[schemas.showBlog]) #db : Session = Depends(get_db)  is a database instance
def get_all(db : Session = Depends(get_db)):
    #we are querying on blog from models 
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model = schemas.showBlog)
def get_one(id, response : Response, db : Session = Depends(get_db) ):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f'the blog with id {id} is not available')
        # response.status_code  = status.HTTP_404_NOT_FOUND
        # return {'detail':f'the blog with id {id} is not available'}
    return blog

@app.post('/user',status_code=status.HTTP_201_CREATED)
def create_user(request : schemas.User ,  db : Session = Depends(get_db)  ):
    hashed_password = pwd_cxt.hash(request.password)
    new_user = models.User(name= request.name , email = request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user