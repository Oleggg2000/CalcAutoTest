import allure
import requests

from config import HOST, PORT


# Testing GET method structure
@allure.feature("Smoke tests")
@allure.title("Проверка работоспособности GET метода")
@allure.link("https://docs.pytest.org/en/6.2.x/example/markers.html", name="Полезная ссылочка)))")
def test_get_methods():
    respond = requests.get(f"http://{HOST}:{PORT}/api/state")
    assert respond.json() == {'statusCode': 0, 'state': 'OК'}


@allure.feature("Smoke tests")
@allure.title("Проверка работоспособности POST метода")
@allure.link("https://docs.pytest.org/en/6.2.x/example/markers.html")
def test_post_method():
    respond = requests.post(f"http://{HOST}:{PORT}/api/addition", json={"x": 5, "y": 8})
    assert respond.json() == {"statusCode": 0, "result": 5 + 8}


# Testing OPTION method structure
@allure.feature("Smoke tests")
@allure.title("Проверка работоспособности OPTIONS метода")
def test_options_methods():
    respond = requests.options(f"http://{HOST}:{PORT}")
    assert respond.headers["Access-Control-Request-Method"] == 'POST, GET, OPTIONS'
