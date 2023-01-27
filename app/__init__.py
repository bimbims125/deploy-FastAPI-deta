from fastapi import FastAPI
from app.routers.film import router as film_router
from app.routers.blog import router as blog_router
from app.routers.author import router as author_router


app = FastAPI()

app.include_router(film_router)
app.include_router(blog_router)
app.include_router(author_router)
