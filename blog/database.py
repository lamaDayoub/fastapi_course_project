from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
#create_engine: The "Engine" is the actual connection pool to the database. It handles the #low-level communication.
engine = create_engine( SQLALCHEMY_DATABASE_URL, connect_args ={"check_same_thread": False})
#sessionmaker: This is a factory that creates "Sessions." A session is a single conversation #with the database (e.g., "Give me user #5").
SessionLocal = sessionmaker(bind = engine , autocommit= False , autoflush = False)
#declarative_base: This is the "Parent" for the models. In Django, we use models.Model; here, #we  use Base.
Base = declarative_base()