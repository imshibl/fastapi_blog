from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, schemas, models
from typing import List
from passlib.context import CryptContext
from ..repository import user

router = APIRouter(
    tags=["Users"],
    prefix="/user"
)

get_db = database.get_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get("/", response_model=List[schemas.ShowUser])
def get_all_users(db:Session = Depends(get_db)):
    return user.get_all(db)

@router.put("/signup", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db:Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db:Session = Depends(get_db)):
    return user.get_single_user(id, db)


   
