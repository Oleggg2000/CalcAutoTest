import pytest
import requests

ERROR_3 = {'statusCode': 3, 'statusMessage': 'Значения параметров должны быть целыми'}
ERROR_4 = {'statusCode': 4, 'statusMessage': 'Превышены максимальные значения параметров'}

params_type_error = [(arg[0], arg[1], task, arg[2]) for task in ["addition", "multiplication", "division", "remainder"]
                     for arg in [["15", 1, ERROR_3], [8.1, 1, ERROR_3], [12e+5, 1, ERROR_3],
                                 [1, "15", ERROR_3], [1, 8.1, ERROR_3], [1, 12e+5, ERROR_3]]]

params_limit_value_error = [(var[0], var[1], task, ERROR_4) for task
                            in ["addition", "multiplication", "division", "remainder"] for var in
                            [[-2147483649, 1], [2147483648, 1], [1, -2147483649], [1, 2147483648]]]


# Validation input values. Only integers are allowed!
@pytest.mark.parametrize("x, y, task, expected_response", params_type_error)
def test_type_error(x, y, task, expected_response):
    respond = requests.post(f"http://127.0.0.1:17678/api/{task}", json={"x": x, "y": y})
    assert respond.json() == expected_response


# Boundary Value Analysis of input parameters. (from -2147483648 to 2147483647)
@pytest.mark.parametrize("x, y, task, expected_response", params_limit_value_error)
def test_value_error(x, y, task, expected_response):
    respond = requests.post(f"http://127.0.0.1:17678/api/{task}", json={"x": x, "y": y})
    assert respond.json() == expected_response


# Addition task (BVA + sign checking)
@pytest.mark.parametrize("x, y, expected_response", [(10, 5, {"statusCode": 0, "result": 15}),
                                                     (10, -5, {"statusCode": 0, "result": 5}),
                                                     (-10, 5, {"statusCode": 0, "result": -5}),
                                                     (-10, -5, {"statusCode": 0, "result": -15}),
                                                     (-2147483648, 0, {"statusCode": 0, "result": -2147483648}),
                                                     (2147483647, 0, {"statusCode": 0, "result": 2147483647}),
                                                     (0, -2147483648, {"statusCode": 0, "result": -2147483648}),
                                                     (0, 2147483647, {"statusCode": 0, "result": 2147483647})])
def test_addition_good(x, y, expected_response):
    respond = requests.post("http://127.0.0.1:17678/api/addition", json={"x": x, "y": y})
    assert respond.json() == expected_response


# Multiplication task (BVA + sign checking)
@pytest.mark.parametrize("x, y, expected_response", [(10, 5, {"statusCode": 0, "result": 50}),
                                                     (10, -5, {"statusCode": 0, "result": -50}),
                                                     (-10, 5, {"statusCode": 0, "result": -50}),
                                                     (-10, -5, {"statusCode": 0, "result": 50}),
                                                     (0, -5, {"statusCode": 0, "result": 0}),
                                                     (-10, 0, {"statusCode": 0, "result": 0}),
                                                     (-2147483648, 1, {"statusCode": 0, "result": -2147483648}),
                                                     (2147483647, 1, {"statusCode": 0, "result": 2147483647}),
                                                     (1, -2147483648, {"statusCode": 0, "result": -2147483648}),
                                                     (1, 2147483647, {"statusCode": 0, "result": 2147483647})])
def test_multiplication_good(x, y, expected_response):
    respond = requests.post("http://127.0.0.1:17678/api/multiplication", json={"x": x, "y": y})
    assert respond.json() == expected_response


# Division task (BVA + sign checking)
@pytest.mark.parametrize("x, y, expected_response", [(10, 5, {"statusCode": 0, "result": 2}),
                                                     (10, -5, {"statusCode": 0, "result": -2}),
                                                     (-10, 5, {"statusCode": 0, "result": -2}),
                                                     (-10, -5, {"statusCode": 0, "result": 2}),
                                                     (-2147483648, 1, {"statusCode": 0, "result": -2147483648}),
                                                     (2147483647, 1, {"statusCode": 0, "result": 2147483647}),
                                                     (1, -2147483648, {"statusCode": 0, "result": -1}),
                                                     (1, 2147483647, {"statusCode": 0, "result": 0})])
def test_division_good(x, y, expected_response):
    respond = requests.post("http://127.0.0.1:17678/api/division", json={"x": x, "y": y})
    assert respond.json() == expected_response


# Division by zero test
@pytest.mark.parametrize("x, y, expected_response", [(1, 0, {'statusCode': 1, 'statusMessage': 'Ошибка вычисления'})])
def test_ZeroDivisionError(x, y, expected_response):
    respond = requests.post("http://127.0.0.1:17678/api/division", json={"x": x, "y": y})
    assert respond.json() == expected_response


# Remainder task (BVA + sign checking)
@pytest.mark.parametrize("x, y, expected_response", [(13, 5, {"statusCode": 0, "result": 3}),
                                                     (13, -5, {"statusCode": 0, "result": -2}),
                                                     (-13, 5, {"statusCode": 0, "result": 2}),
                                                     (-13, -5, {"statusCode": 0, "result": -3}),
                                                     (-2147483648, 1, {"statusCode": 0, "result": 0}),
                                                     (2147483647, 1, {"statusCode": 0, "result": 0}),
                                                     (1, -2147483648, {'result': -2147483647, 'statusCode': 0}),
                                                     (1, 2147483647, {"statusCode": 0, "result": 1})])
def test_remainder_good(x, y, expected_response):
    respond = requests.post("http://127.0.0.1:17678/api/remainder", json={"x": x, "y": y})
    assert respond.json() == expected_response


# Division by zero test
@pytest.mark.parametrize("x, y, expected_response", [(1, 0, {'statusCode': 1, 'statusMessage': 'Ошибка вычисления'})])
def test_remainder_error(x, y, expected_response):
    respond = requests.post("http://127.0.0.1:17678/api/remainder", json={"x": x, "y": y})
    assert respond.json() == expected_response


if __name__ == "__main__":
    pytest.main()
