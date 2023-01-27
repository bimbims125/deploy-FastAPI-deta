from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fastapi import Body
from fastapi.exceptions import HTTPException

from app.config import conn
from app.models import Author, Blog

db_engine = create_engine(conn)

async def get_all_authors():
  with Session(db_engine) as session:
    data = session.query(Author).\
    with_entities(Author.id, Author.name, Author.email).all()
    return {'status_code': 200, 'success':True, 'data': data}

async def create_author(name:str, email:str):
  with Session(db_engine) as session:
    session.add(Author(name=name, email=email))
    session.commit()
    return {'status_code': 200, 'message': 'Author created successfully'}

async def get_blog_by_author_id(author_id:int):
  with Session(db_engine) as session:
    if data := session.query(Blog).\
      with_entities(Blog.id, Blog.title, Blog.slug, Blog.body,).\
      filter(Author.id == author_id).all():
      return {'status_code':200, 'success':True, 'data':data}
    elif data == []:
      raise HTTPException(status_code=404, detail='Author not found')
