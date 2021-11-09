from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, database, schemas, models
from typing import List



router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

get_db = database.get_db


@router.get("/")
def index(db: Session = Depends(get_db)):
    blogs = crud.get_all_blogs(db)
    return blogs

@router.post("/post")
def add_blog(blog: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = crud.post_blog(db, blog)
    return new_blog

@router.get("/{id}")
def get_selected_blog(id:int, db:Session = Depends(get_db)):
    blog = crud.get_selected_blog(id, db)
    if not blog:
        raise HTTPException(status_code=404, detail="item not found")
    return blog

@router.delete("/delete/{id}")
def delete(id:int, db:Session = Depends(get_db)):
    blog = crud.delete_blog(id, db).delete(synchronize_session=False)
    db.commit()
    if not blog:
        raise HTTPException(status_code=404, detail="item not found")

    return {"detail": "deleted"}

@router.put("/update/{id}")
def update(id:int, updated_blog: schemas.Blog, db:Session = Depends(get_db)):
    blog = crud.update_blog(id,db).update({ models.Blog.title: updated_blog.title,models.Blog.body : updated_blog.body}, synchronize_session=False)
    db.commit()
    if not blog:
        raise HTTPException(status_code=404, detail="item not found")
    
    return {
        "updated"
    }