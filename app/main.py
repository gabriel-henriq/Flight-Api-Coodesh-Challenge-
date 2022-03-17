from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.tasks import repeat_every
import requests

from app.utils import get_9am_hour_in_seconds
from .models import Base
from .database import engine
from .routers import article, scrape_article

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(article.router)
app.include_router(scrape_article.router)

Base.metadata.create_all(bind=engine)


@app.on_event("startup")
@repeat_every(seconds=get_9am_hour_in_seconds(), wait_first=True)
def scrape_articles_on_startup():
    response = requests.get('http://localhost:8000/scrape-articles/')
    if response.status_code == status.HTTP_200_OK:
        print('Articles has succefully updated.')


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"message": "Back-end Challenge 2021 🏅 - Space Flight News"}
