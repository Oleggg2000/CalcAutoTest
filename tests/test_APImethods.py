import pytest
import requests
from CalcAutoTest.config import HOST, PORT


# Testing GET method structure
def test_get_methods():
    respond = requests.get(f"http://{HOST}:{PORT}/api/state")
    assert respond.json() == {'statusCode': 0, 'state': 'OК'}


# Testing OPTION method structure
def test_options_methods():
    respond = requests.options(f"http://{HOST}:{PORT}")
    assert respond.headers["Access-Control-Request-Method"] == 'POST, GET, OPTIONS'


if __name__ == "__main__":
    pytest.main()
