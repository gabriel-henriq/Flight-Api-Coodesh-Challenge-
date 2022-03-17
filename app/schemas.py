from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Articles(BaseModel):
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: Optional[str]
    publishedAt: datetime
    createdAt: datetime
    featured: bool = False


class CreateArticle(BaseModel):
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: Optional[str]
    featured: bool = False
