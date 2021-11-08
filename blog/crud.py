from sqlalchemy.orm import Session

from . import models, schemas

def post_blog(db: Session, blog: schemas.Blog):
    new_blog = models.Blog(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_all_blogs(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def get_selected_blog(id:int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog

def delete_blog(id:int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    return blog

def update_blog(id:int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    return blog
    