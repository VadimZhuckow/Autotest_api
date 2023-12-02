import requests
from jsonschema import validate
from configuration import SEVRICE_URL
from src.enums.global_enums import GlobalErrorMessages
from src.shemas.posts import POST_SCHEMA

def test_getting_posts():
    response = requests.get(url=SEVRICE_URL)
    received_posts = response.json()
    print(received_posts)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(received_posts) == 3, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
    for item in received_posts:
        validate(item, POST_SCHEMA)

# [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]
