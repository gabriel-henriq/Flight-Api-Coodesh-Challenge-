
from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text
from .database import Base


class Articles(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    imageUrl = Column(String, nullable=False)
    newsSite = Column(String, nullable=False)
    summary = Column(String, nullable=True)
    publishedAt = Column(TIMESTAMP(timezone=True),
                         nullable=False, server_default=text('NOW()'))
    updatedAt = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=text('NOW()'))
    featured = Column(Boolean, nullable=False, server_default='FALSE')