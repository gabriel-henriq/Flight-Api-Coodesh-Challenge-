import requests

url = 'https://api.spaceflightnewsapi.net/v3/articles'


def fetch(url):
    response = requests.get(url)
    return response.json()


def get_all_articles() -> dict:
    count = fetch(f'{url}/count')
    response = requests.get(
        f'{url}?_limit={count}')
    return response.json()
