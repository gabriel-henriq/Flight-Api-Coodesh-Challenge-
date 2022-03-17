from fastapi import Depends, status, APIRouter
from sqlalchemy.orm import Session

from app import models
from app.services import get_all_articles
from app.database import get_db

router = APIRouter(prefix="/scrape-articles", tags=["Scrape Articles"])


@router.get('/', status_code=status.HTTP_200_OK)
def populate_from_flight_api(db: Session = Depends(get_db)):
    to_database = get_all_articles()
    for article in to_database:
        if article.get('title') == db.query(models.Articles).filter_by(title=article.get('title')).first():
            pass
        else:
            new_article = models.Articles(
                title=article.get('title'),
                url=article.get('url'),
                imageUrl=article.get('imageUrl'),
                newsSite=article.get('newsSite'),
                summary=article.get('summary'),
                publishedAt=article.get('publishedAt'),
                updatedAt=article.get('updatedAt'),
                featured=article.get('featured'))
            db.add(new_article)
    db.commit()
    return {"message": "Articles has succefully updated."}
