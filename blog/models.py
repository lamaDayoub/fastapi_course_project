from sqlalchemy import Column, Integer, String, ForeignKey

from .database import Base
from sqlalchemy.orm import relationship
 


#This defines the actual database tables (the "physical" structure).
class Blog(Base) :
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key =True, index=True)
    title = Column(String)
    body = Column(String)
    # 1. The Physical Link: Store the actual User ID
    user_id= Column(Integer, ForeignKey('users.id'))
    # 2. The Virtual Link: The "Bridge" to the User object
    creator = relationship('User', back_populates='blogs')
    
    
class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key =True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    # The other side of the Bridge
    blogs = relationship("Blog", back_populates="creator")
     
    
