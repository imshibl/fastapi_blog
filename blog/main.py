from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import SavepointClause
from sqlalchemy.sql.functions import mode

from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", tags=["get requestes"])
def index(db: Session = Depends(get_db)):
    blogs = crud.get_all_blogs(db)
    return blogs

@app.post("/blog/post", tags=["post requestes"])
def add_blog(blog: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = crud.post_blog(db, blog)
    return new_blog

@app.get("/blog/{id}", tags=["get requestes"])
def get_selected_blog(id:int, db:Session = Depends(get_db)):
    blog = crud.get_selected_blog(id, db)
    if not blog:
        raise HTTPException(status_code=404, detail="item not found")
    return blog

@app.delete("/blog/delete/{id}", tags=["delete requestes"])
def delete(id:int, db:Session = Depends(get_db)):
    blog = crud.delete_blog(id, db).delete(synchronize_session=False)
    db.commit()
    if not blog:
        raise HTTPException(status_code=404, detail="item not found")

    return {"detail": "deleted"}

@app.put("/blog/update/{id}", tags=["update requestes"])
def update(id:int, updated_blog: schemas.Blog, db:Session = Depends(get_db)):
    blog = crud.update_blog(id,db).update({ models.Blog.title: updated_blog.title,models.Blog.body : updated_blog.body}, synchronize_session=False)
    db.commit()
    if not blog:
        raise HTTPException(status_code=404, detail="item not found")
    
    return {
        "updated"
    }

