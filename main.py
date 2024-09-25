import uvicorn

from fastapi import Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


from sqlalchemy import create_engine

from app import app
from app.config import conn
from app.models import Base

db_engine = create_engine(conn)

templates = Jinja2Templates(directory="app/templates")
Base.metadata.create_all(db_engine)

@app.get('/')
async def root(request: Request):
  return templates.TemplateResponse('welcome.html', {'request': request})

@app.get('/test-deploy')
async def test_deploy(request: Request):
  return {'message':'berhasil deploy ulang!'}

if  __name__ == '__main__':
  uvicorn.run('app:app', host='0.0.0.0', port=9000, reload=True)

