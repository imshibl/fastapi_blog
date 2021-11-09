from .. import schemas, models
from typing import List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def post(blog: schemas.Blog, db: Session):
    new_blog = models.Blog(title=blog.title, body=blog.body, creator_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_selected(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="item not found")
    return blog

def delete(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    if not blog:
        raise HTTPException(status_code=404, detail="item not found")

    return {"detail": "deleted"}

def update(id:int, updated_blog: schemas.Blog, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).update({ models.Blog.title: updated_blog.title,models.Blog.body : updated_blog.body}, synchronize_session=False)
    db.commit()
    if not blog:
        raise HTTPException(status_code=404, detail="item not found")
    
    return {
        "updated"
    }