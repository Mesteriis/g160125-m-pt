from pydantic import BaseModel
from typing import Optional, List


class TagSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class AuthorSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class BookCreate(BaseModel):
    title: str
    author: Optional[AuthorSchema]
    tags: List[TagSchema] = []
    class Config:
        orm_mode = True


class BookResponse(BookCreate):
    id: int

    class Config:
        orm_mode = True
