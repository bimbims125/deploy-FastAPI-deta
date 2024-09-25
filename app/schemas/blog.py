from typing import Union
from pydantic import BaseModel

class Blogs(BaseModel):
  id:int
  title:str
  slug:str
  body:str

  class Config:
    from_attributes = True

class BaseResponseModel(BaseModel):
  data:Union[dict, list] = None
  meta: dict = {}
  success: bool = True
  code: int = 200
  message: str = 'Success'

  class Config:
      json_schema_extra = {
          'example': {
              'data':None,
              'meta':{},
              'success':True,
              'code':200,
              'message':'Success'
          }
      }

