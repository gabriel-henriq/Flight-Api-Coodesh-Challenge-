from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import models
from app.main import app
from app.config import settings
from app.database import get_db
from app.database import Base

db_hostname = settings.database_hostname
db_username = settings.database_username
db_name = settings.database_name
db_pass = settings.database_password
db_port = settings.database_port
SQLALCHEMY_DATABASE_URL = f"postgresql://{db_username}:{db_pass}@{db_hostname}:{db_port}/{db_name}_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def test_articles(session):
    articles_data = [
        {
            "url": "https://spaceflightnow.com/2019/11/10/spacex-readies-upgraded-starlink-satellites-for-launch/",
            "newsSite": "Spaceflight Now",
            "featured": True,
            "imageUrl": "https://mk0spaceflightnoa02a.kinstacdn.com/wp-content/uploads/2019/11/f9_starlink1.jpg",
            "title": "SpaceX readies upgraded Starlink satellites for launch",
            "summary": "",
        },
        {
            "url": "https://spaceflightnow.com/2019/11/09/next-three-man-soyuz-crew-training-to-have-space-station-to-themselves/",
            "newsSite": "Spaceflight Now",
            "featured": False,
            "imageUrl": "https://mk0spaceflightnoa02a.kinstacdn.com/wp-content/uploads/2019/11/exp62emu.jpg",
            "title": "Next three-man Soyuz crew training to have space station to themselves",
            "summary": "",
        },
        {
            "url": "https://www.teslarati.com/spacex-drone-ship-satellite-image-falcon-9-ocean-landing/",
            "newsSite": "Teslarati",
            "featured": True,
            "imageUrl": "https://www.teslarati.com/wp-content/uploads/2019/05/Falcon-9-B1056-infrared-landing-SpaceX-7-edit-1000x600.jpg",
            "title": "SpaceX drone ship spotted by satellite ahead of first Falcon 9 ocean landing in five months",
            "summary": "",
        },
    ]

    def create_article_model(article):
        return models.Articles(**article)

    article_map = map(create_article_model, articles_data)
    articles = list(article_map)
    session.add_all(articles)
    session.commit()
    articles = session.query(models.Articles).all()

    return articles
