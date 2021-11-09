from pydantic import BaseModel
from typing import Optional,List


class User(BaseModel):
    name:str
    email:str
    password:str

class BlogBase(BaseModel):
    title:str
    body:str

class Blog(BlogBase):
    class Config():
        orm_mode=True

class ShowUser(BaseModel):
    id:int
    name:str
    email:str

    blogs: List[Blog]
    
    class Config():
        orm_mode=True

class ShowOnlyUser(BaseModel):
    name:str
    email:str

    class Config():
        orm_mode=True




class ShowBlog(BaseModel):
    id:int
    title:str
    body:str
    creator: ShowOnlyUser
    class Config():
        orm_mode=True




