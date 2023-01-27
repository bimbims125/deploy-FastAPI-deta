from pydantic import BaseModel

from typing import Union, List

from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from fastapi import Body
from fastapi.exceptions import HTTPException

from app.config import conn
from app.models import Blog, Author
from app.dependencies.slugify import slugify
from app.schemas.blog import Blogs

db_engine = create_engine(conn)

class BaseResponseModel(BaseModel):
  data:Union[dict, list] = None
  meta: dict = {}
  success: bool = True
  code: int = 200
  message: str = 'Success'

  class Config:
      schema_extra = {
          'example': {
              'data':None,
              'meta':{},
              'success':True,
              'status_code':200,
              'message':'Success'
          }
      }

class GetBlogResponseModel(BaseResponseModel):
  class Config:
    schema_extra = {
          'example':{
              'data':{
                  'id':1,
                  'title':'Testing',
                  'slug':'testing',
                  'body':'This is a test',
              },
              'meta':{},
              'success':True,
              'status_code':200,
              'message':'Success'
          }
      }
    orm_mode = True


async def get_all_blogs():

  with Session(db_engine) as session:
    data = session.query(Blog).all()
    return {'status_code':200, 'success':True, 'data':data}

async def get_blog(slug:str):
  with Session(db_engine) as session:
    if data := session.query(Blog).filter(Blog.slug==slug).first():
      return GetBlogResponseModel(data=Blogs(id=data.id, title=data.title, slug=data.slug, body=data.body))
    raise HTTPException(status_code=404, detail='Blog not found')

async def create_blog(title:str=Body(), body:str=Body(), author_id:int=Body()):

  with Session(db_engine) as session:
    try:
      session.add(Blog(title=title, slug=slugify(title),body=body, author_id=author_id))
      session.commit()
      return {'status_code':200, 'success':True}
    except:
      raise HTTPException(status_code=422, detail=f"Blog with title '{title}' already exists, change the title!")

async def update_blog(id:int, title:str=Body(), body:str=Body()):
  with Session(db_engine) as session:
    try:
      blog = session.query(Blog).filter(Blog.id==id).first()
      blog.title = title
      blog.slug = slugify(title)
      blog.body = body
      session.commit()
      return {'status_code':200, 'success':True}
    except Exception as e:
      raise HTTPException(status_code=422, detail=str(e)) from e

async def delete_blog(id:int):
  with Session(db_engine) as session:
    session.delete(session.get(Blog, id))
    session.commit()
    return {'status_code':200, 'success':True}
