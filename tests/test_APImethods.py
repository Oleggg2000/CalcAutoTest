import pytest
import requests


# Testing GET method structure
def test_GETmethods():
    respond = requests.get("http://127.0.0.1:17678/api/state")
    assert respond.json() == {'statusCode': 0, 'state': 'OК'}


# Testing OPTION method structure
def test_OPTIONSmethods():
    respond = requests.options("http://127.0.0.1:17678")
    assert respond.headers["Access-Control-Request-Method"] == 'POST, GET, OPTIONS'


# Testing POST methods structure
@pytest.mark.parametrize("x, y, task, expected_response", [(10, 2, "addition", {'statusCode': 0, 'result': 12}),
                                                           (5, 2, "multiplication", {'statusCode': 0, 'result': 10}),
                                                           (7, 2, "division", {'statusCode': 0, 'result': 3}),
                                                           (32, 7, "remainder", {'statusCode': 0, 'result': 4})])
def test_POSTmethods(x, y, task, expected_response):
    respond = requests.post(f"http://127.0.0.1:17678/api/{task}", json={"x": x, "y": y})
    assert respond.json() == expected_response


if __name__ == "__main__":
    pytest.main()
