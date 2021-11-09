from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, schemas
from typing import List
from ..repository import blog



router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    return blog.get_all(db)

@router.post("/post")
def add_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.post(request, db)

@router.get("/{id}", response_model=schemas.ShowBlog)
def get_selected_blog(id:int, db:Session = Depends(get_db)):
    return blog.get_selected(id, db)

@router.delete("/delete/{id}")
def delete_blog(id:int, db:Session = Depends(get_db)):
    return blog.delete(id, db)

@router.put("/update/{id}")
def update_blog(id:int, updated_blog: schemas.Blog, db:Session = Depends(get_db)):
    return blog.update(id, updated_blog, db)