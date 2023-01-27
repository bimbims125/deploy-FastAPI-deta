from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fastapi import Body
from fastapi.exceptions import HTTPException

from app.config import conn
from app.models import Film

db_engine = create_engine(conn)

async def get_all_films():
  with Session(db_engine) as session:
    data = session.query(Film).all()
    return {'status_code':200,'success':True,'data':data}

async def add_film(title: str = Body(), description: str = Body()):
  with Session(db_engine) as session:
    session.add(Film(title=title, description=description))
    session.commit()
    return {'status_code':200, 'success':True, 'title': title, 'description': description}

async def get_film(id: int):
  if id == 0:
    raise HTTPException(status_code=404, detail='Enter valid id.')
  with Session(db_engine) as session:
    if data := session.get(Film, id):
      return {'status_code':200, 'success':True, 'data':data}
    raise HTTPException(status_code=404, detail='Film not found.')

async def update_film(id: int, title: str = Body(), description: str = Body()):
  with Session(db_engine) as session:
    session.query(Film).\
      filter(Film.id == id).\
      update({Film.title:title, Film.description:description})
    session.commit()
    return {'status_code':200, 'success':True}

async def delete_film(id: int):
  with Session(db_engine) as session:
    data = session.get(Film, id)
    session.delete(data)
    session.commit()
    return {'status_code':200, 'success':True}
