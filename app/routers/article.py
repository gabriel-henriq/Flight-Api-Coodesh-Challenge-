from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas
from..database import get_db

router = APIRouter(
    prefix="/articles",
    tags=["Articles"]
)


@router.get("/", status_code=status.HTTP_200_OK)
def get_articles(db: Session = Depends(get_db), page_num: int = 1, page_size: int = 10):
    start = (page_num - 1) * page_size
    end = start + page_size

    articles = db.query(models.Articles).all()
    return articles[start:end]


@router.get("/{article_id}", status_code=status.HTTP_200_OK)
def get_article_by_id(article_id: int, db: Session = Depends(get_db)):
    article = db.query(models.Articles).filter(
        models.Articles.id == article_id).first()
    if article is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
    return article


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_articles(article: schemas.CreateArticle, db: Session = Depends(get_db)):
    new_article = models.Articles(**article.dict())
    db.add(new_article)
    db.commit()
    return {"message": "Article has succefully created."}


@router.put("/{article_id}", status_code=status.HTTP_202_ACCEPTED)
def update_articles(article_id: int, article: schemas.CreateArticle, db: Session = Depends(get_db)):
    db_article = db.query(models.Articles).filter(
        models.Articles.id == article_id).first()
    if db_article:
        db_article.title = article.title
        db_article.url = article.url
        db_article.imageUrl = article.imageUrl
        db_article.newsSite = article.newsSite
        db_article.summary = article.summary
        db_article.featured = article.featured
        db.commit()
        return {"message": "Article has succefully updated."}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")


@router.delete("/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_articles(article_id: int, db: Session = Depends(get_db)):
    db_article = db.query(models.Articles).filter(
        models.Articles.id == article_id).first()
    if db_article:
        db.delete(db_article)
        db.commit()
        return {"message": "Article has succefully deleted."}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
