import pytest
import requests
from config import HOST, PORT


# Validation input values. Only integers are allowed!
@pytest.mark.parametrize("task", ["addition", "multiplication", "division", "remainder"])
@pytest.mark.parametrize("x, y", [("15", 1), (8.1, 1), (12e+5, 1), (1, "15"), (1, 8.1), (1, 12e+5)])
def test_type_error(x, y, task):
    respond = requests.post(f"http://{HOST}:{PORT}/api/{task}", json={"x": x, "y": y})
    assert respond.json() == {'statusCode': 3, 'statusMessage': 'Значения параметров должны быть целыми'}


# Boundary Value Analysis of input parameters. (from -2147483648 to 2147483647)
@pytest.mark.parametrize("task", ["addition", "multiplication", "division", "remainder"])
@pytest.mark.parametrize("x, y", [(-2147483649, 1), (2147483648, 1), (1, -2147483649), (1, 2147483648)])
def test_value_error(x, y, task):
    respond = requests.post(f"http://{HOST}:{PORT}/api/{task}", json={"x": x, "y": y})
    assert respond.json() == {'statusCode': 4, 'statusMessage': 'Превышены максимальные значения параметров'}


# Addition task (BVA + sign checking)
@pytest.mark.parametrize("x, y", [(10, 5), (10, -5), (-10, 5), (-10, -5),
                                  (-2147483648, 0), (2147483647, 0), (0, -2147483648), (0, 2147483647)])
def test_addition_good(x, y):
    respond = requests.post(f"http://{HOST}:{PORT}/api/addition", json={"x": x, "y": y})
    assert respond.json() == {"statusCode": 0, "result": x + y}


# Multiplication task (BVA + sign checking)
@pytest.mark.parametrize("x, y", [(10, 5), (10, -5), (-10, 5), (-10, -5), (0, -5), (-10, 0),
                                  (-2147483648, 1), (2147483647, 1), (1, -2147483648), (1, 2147483647)])
def test_multiplication_good(x, y):
    respond = requests.post(f"http://{HOST}:{PORT}/api/multiplication", json={"x": x, "y": y})
    assert respond.json() == {"statusCode": 0, "result": x * y}


# Division task (BVA + sign checking)
@pytest.mark.parametrize("x, y", [(10, 5), (10, -5), (-10, 5), (-10, -5),
                                  (-2147483648, 1), (2147483647, 1), (1, -2147483648), (1, 2147483647)])
def test_division_good(x, y):
    respond = requests.post(f"http://{HOST}:{PORT}/api/division", json={"x": x, "y": y})
    assert respond.json() == {"statusCode": 0, "result": x // y}


# Remainder task (BVA + sign checking)
@pytest.mark.parametrize("x, y", [(13, 5), (13, -5), (-13, 5), (-13, -5),
                                  (-2147483648, 1), (2147483647, 1), (1, -2147483648), (1, 2147483647)])
def test_remainder_good(x, y):
    respond = requests.post(f"http://{HOST}:{PORT}/api/remainder", json={"x": x, "y": y})
    assert respond.json() == {"statusCode": 0, "result": x % y}


# Division by zero test (integer/remainder division)
@pytest.mark.parametrize("x, y, task", [(1, 0, "division"), (1, 0, "remainder")])
def test_zero_division_error(x, y, task):
    respond = requests.post(f"http://{HOST}:{PORT}/api/{task}", json={"x": x, "y": y})
    assert respond.json() == {'statusCode': 1, 'statusMessage': 'Ошибка вычисления'}


if __name__ == "__main__":
    pytest.main()
