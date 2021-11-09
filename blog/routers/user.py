from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, database, schemas, models
from typing import List

router = APIRouter(
    tags=["Users"],
    prefix="/user"
)

get_db = database.get_db

@router.put("/signup")
def create_user(request: schemas.User, db:Session = Depends(get_db)):
    new_user = models.User(name = request.name, email=request.email, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
