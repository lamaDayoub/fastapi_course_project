from fastapi import FastAPI,Depends
from . import schemas, models
from .database import engine,SessionLocal
from sqlalchemy.orm import Session 


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

#The Logic: This is a core FastAPI concept. that is saying: "Before you run this function, I #need you to go run get_db and give me a database session."
#It ensures that every request gets its own database connection and, most importantly, closes #it when the request is finished.
@app.post('/blog')
def create (request : schemas.Blog, db : Session = Depends(get_db)):
    # db: Session: This is your "link" to the database. You will use this variable to perform #your CRUD operations (like db.add() or db.query()).
    new_blog = models.Blog(title = request.title , body = request .body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog') #db : Session = Depends(get_db)  is a database instance
def get_all(db : Session = Depends(get_db)):
    #we are querying on blog from models 
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}')
def get_one(id, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog