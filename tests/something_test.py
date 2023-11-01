import requests
from configuration import SEVRICE_URL
from src.enums.global_enums import GlobalErrorMessages


def test_getting_posts():
    response = requests.get(url=SEVRICE_URL)
    received_posts = response.json()

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(received_posts) == 3, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
