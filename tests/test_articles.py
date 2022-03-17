import pytest
from fastapi import status


def test_get_default_articles(client, test_articles):
    response = client.get('/articles/')
    assert len(response.json()) == len(test_articles)
    assert response.status_code == status.HTTP_200_OK


def test_get_article_by_id(client, test_articles):
    response = client.get(f'/articles/{test_articles[0].id}')
    assert response.status_code == status.HTTP_200_OK


def test_get_article_by_page(client, test_articles):
    response = client.get('/articles/?page_num=1')
    assert response.status_code == status.HTTP_200_OK


def test_not_exist_article(client, test_articles):
    response = client.get('/articles/1000')
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_unprocessable_article(client, test_articles):
    response = client.get('/articles/asd')
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.parametrize("title, url, imageUrl, newsSite, summary, featured", [
    ("Title", "Url", "ImageUrl", "newsSite", "Summary", True),
    ("Second title", "Second Url", "Second imageUrl",
     "Second newsSite", "Second summary", False),
])
def test_create_article(client, title, url, imageUrl, newsSite, summary, featured):
    response = client.post(
        "/articles/", json={"title": title,
                            "url": url,
                            "imageUrl": imageUrl,
                            "newsSite": newsSite,
                            "summary": summary,
                            "featured": featured})

    assert response.status_code == status.HTTP_201_CREATED


def test_create_article_featured_false_by_default(client):
    response = client.post(
        "/articles/", json={"title": "Title",
                            "url": "Url",
                            "imageUrl": "ImageUrl",
                            "newsSite": "newsSite",
                            "summary": "Summary", })
    created_article = client.get("/articles/").json()[0]
    assert created_article["featured"] == False
    assert created_article["title"] == "Title"
    assert created_article["url"] == "Url"
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.parametrize("id_indice", [
    (0),
    (1),
    (2)
])
def test_delete_articles(client, test_articles, id_indice):
    response = client.delete(f"/articles/{test_articles[id_indice].id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_delete_articles_non_exist(client, test_articles):
    response = client.delete("/articles/9999")
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.parametrize("id_indice, title, url, imageUrl, newsSite, summary, featured", [
    (0, "Title", "Url", "ImageUrl", "newsSite", "Summary", True),
    (1, "Second title", "Second Url", "Second imageUrl",
     "Second newsSite", "Second summary", False),
    (2, "Third title", "Third Url", "Third imageUrl",
     "Third newsSite", "Third summary", True)])
def test_update_articles(client, test_articles, id_indice, title, url, imageUrl, newsSite, summary, featured):
    response = client.put(
        f"/articles/{test_articles[id_indice].id}", json={"title": title,
                                                          "url": url,
                                                          "imageUrl": imageUrl,
                                                          "newsSite": newsSite,
                                                          "summary": summary,
                                                          "featured": featured})
    assert response.status_code == status.HTTP_202_ACCEPTED
