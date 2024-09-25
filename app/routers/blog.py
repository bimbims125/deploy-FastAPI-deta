from typing import List
from fastapi import APIRouter

from app.crud.blog import get_all_blogs, create_blog, get_blog, update_blog, delete_blog, GetBlogResponseModel

from app.schemas.blog import Blogs

router = APIRouter(prefix="/api/v1", tags=["Blogs"])



router.add_api_route(
  '/blogs',
  get_all_blogs,
  methods=["GET"],
)

router.add_api_route(
  '/blog',
  get_blog,
  methods=["GET"],
  response_model=GetBlogResponseModel,
)

router.add_api_route(
  '/blog/add',
  create_blog,
  methods=["POST"],
  status_code=201
)

router.add_api_route(
  '/blog/edit',
  update_blog,
  methods=["PUT"]
)

router.add_api_route(
  '/blog/delete',
  delete_blog,
  methods=["DELETE"]

)
