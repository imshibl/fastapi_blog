from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import SavepointClause
from sqlalchemy.sql.functions import mode

from . import models, schemas, database
from .database import SessionLocal, engine

from .routers import blog, user


models.Base.metadata.create_all(engine)
app = FastAPI()





app.include_router(blog.router)
app.include_router(user.router)




