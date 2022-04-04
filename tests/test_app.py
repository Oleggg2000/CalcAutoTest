import requests
from conftest import *
from CalcAutoTest.config import HOST, PORT


# Testing defaults parameters (start, stop, restart)
@pytest.mark.parametrize("str, output", [
    ("cd .. & webcalculator.exe start", "Сервер уже запущен\r\n"),
    ("cd .. & webcalculator.exe restart", "Пытаемся остановить Веб-калькулятор\r\nВеб-калькулятор остановлен\r\n"
                                          "Запуск Веб-калькулятора на 127.0.0.1:17678\r\n"
                                          "Веб-калькулятор запущен на 127.0.0.1:17678\r\n"),
    ("cd .. & webcalculator.exe stop", "Пытаемся остановить Веб-калькулятор\r\nВеб-калькулятор остановлен\r\n"),
    ("cd .. & webcalculator.exe restart", 'Веб-калькулятор не запущен. Используйте команду "start"\r\n')])
def test_launching(str, output):
    try:
        respond = requests.get(f"http://{HOST}:{PORT}/api/state").json()
        assert cmdline(str).decode('cp1251') == output and respond == {'statusCode': 0, 'state': 'OК'}
    except Exception as e:
        print(e)
        assert cmdline(str).decode('cp1251') == output


# Testing optional parameters host, port (star [host] [port])
@pytest.mark.parametrize("str_, host, port, output", [
    ("cd .. & webcalculator.exe start 0.0.0.0", "0.0.0.0", f"{PORT}", "Запуск Веб-калькулятора на 0.0.0.0:17678\r\n"
                                                                    "Веб-калькулятор запущен на 0.0.0.0:17678\r\n"),
    ("cd .. & webcalculator.exe stop", f"{HOST}", f"{PORT}", "Пытаемся остановить Веб-калькулятор\r\n"
                                                        "Веб-калькулятор остановлен\r\n"),
    ("cd .. & webcalculator.exe start 127.5.5.5 5555", "127.5.5.5", "5555",
     "Запуск Веб-калькулятора на 127.5.5.5:5555\r\nВеб-калькулятор запущен на 127.5.5.5:5555\r\n"),
    ("cd .. & webcalculator.exe stop", f"{HOST}", f"{PORT}", "Пытаемся остановить Веб-калькулятор\r\n"
                                                        "Веб-калькулятор остановлен\r\n")
    ])
@pytest.mark.usefixtures("setup_for_CLI_test_launching_with_params")
def test_launching_with_params(str_, host, port, output):
    try:
        respond = requests.get(f"http://{host}:{port}/api/state").json()
        assert cmdline(str_).decode('cp1251') == output and respond == {'statusCode': 0, 'state': 'OК'}
    except Exception as e:
        print(e)
        assert cmdline(str_).decode('cp1251') == output


if __name__ == "__main__":
    pytest.main()




