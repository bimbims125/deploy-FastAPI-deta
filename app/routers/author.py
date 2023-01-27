from fastapi import APIRouter

from app.crud.author import *


router = APIRouter(prefix='/api/v1', tags=['Author'])


router.add_api_route(
  '/authors',
  get_all_authors,
  methods=['GET']
)

router.add_api_route(
  '/author/{author_id}/blogs',
  get_blog_by_author_id,
  methods=['GET']
)

router.add_api_route(
  '/author/create',
  create_author,
  methods=['POST']
  )
