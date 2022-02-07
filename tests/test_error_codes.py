import pytest
import requests


# Test GET method raising statusCode:5
def test_get_error_code_5():
    respond = requests.post("http://127.0.0.1:17678/api/state", json={})
    assert respond.json() == {"statusCode": 5, "statusMessage": " state - Не верное имя задачи или тип HTTP запроса"}


# Test POST methods raising statusCode:5 with JSON format error
@pytest.mark.parametrize("task", ["addition", "multiplication", "division", "remainder"])
def test_post_error_code_5_1(task):
    respond = requests.post(f"http://127.0.0.1:17678/api/{task}", data={b"some data"})
    assert respond.json() == {'statusCode': 5, "statusMessage": "Не допустимый формат json"}


# Test POST methods raising statusCode:5 with HTTP method or task name error
@pytest.mark.parametrize("task", ["my_own_task_lol", "addition", "multiplication", "division", "remainder"])
def test_post_error_code_5_2(task):
    respond = requests.get(f"http://127.0.0.1:17678/api/{task}", json={})
    assert respond.json() == {"statusCode": 5, "statusMessage": f": {task} - Не верное имя задачи или тип HTTP запроса"}


# Test POST methods raising statusCode:2 Required parameters are not specified
@pytest.mark.parametrize("task, json", [("addition", {"x": 5}), ("multiplication", {"y": 5}),
                                        ("division", {}), ("remainder", {"x": 5,})])
def test_post_error_code_2(task, json):
    respond = requests.post(f"http://127.0.0.1:17678/api/{task}", json=json)
    assert respond.json() == {'statusCode': 2, 'statusMessage': 'Не указаны необходимые параметры'}


if __name__ == "__main__":
    pytest.main()
