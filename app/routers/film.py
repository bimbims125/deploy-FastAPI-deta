from fastapi import APIRouter

from app.crud.film import (
  get_all_films,
  add_film, get_film,
  update_film,
  delete_film
)

router = APIRouter(prefix="/api/v1", tags=["Films"])


router.add_api_route(
  '/films',
  get_all_films,
  methods=['GET']
)

router.add_api_route(
  '/film',
  get_film,
  methods=['GET']
)

router.add_api_route(
  '/film/add',
  add_film,
  methods=['POST']
)

router.add_api_route(
  '/film/edit',
  update_film,
  methods=['PUT']
)

router.add_api_route(
  '/film/delete',
  delete_film,
  methods=['DELETE']
)
