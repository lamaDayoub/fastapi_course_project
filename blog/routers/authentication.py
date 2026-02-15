from fastapi import APIRouter,Depends, HTTPException,status
from .. import schemas,models,database, token
from sqlalchemy.orm import Session
from ..hashing import Hash

router=APIRouter()

@router.post('/login')
def login(request:schemas.Login, db:Session =Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email== request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"invalid credentials")
    
    if not Hash.verify(request.password,user.password):
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"incorrect pasword")
    #generate jwt and return it
    
    
    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return {'access_tokec' :access_token , 'token_type':'bearer'}
    

    