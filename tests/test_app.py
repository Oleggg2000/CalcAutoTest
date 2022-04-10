import allure
import requests
from conftest import *
from tests.config import HOST, PORT


# Testing defaults parameters (start, stop, restart)
@allure.feature("CLI check")
@pytest.mark.parametrize("shell_command, result", [
    ("cd .. & webcalculator.exe start", "Сервер уже запущен\r\n"),
    ("cd .. & webcalculator.exe restart", "Пытаемся остановить Веб-калькулятор\r\nВеб-калькулятор остановлен\r\n"
                                          "Запуск Веб-калькулятора на 127.0.0.1:17678\r\n"
                                          "Веб-калькулятор запущен на 127.0.0.1:17678\r\n"),
    ("cd .. & webcalculator.exe stop", "Пытаемся остановить Веб-калькулятор\r\nВеб-калькулятор остановлен\r\n"),
    ("cd .. & webcalculator.exe restart", 'Веб-калькулятор не запущен. Используйте команду "start"\r\n')],
    ids=["Калькулятор уже запущен", "Калькулятор рестартанул", "Калькулятор остановлен", "Калькулятор не запущен"])
def test_launching(shell_command, result):
    with allure.step(f"Запущен на {HOST}:{PORT}"):
        try:
            respond = requests.get(f"http://{HOST}:{PORT}/api/state").json()
            assert cmdline(shell_command).decode('cp1251') == result and respond == {'statusCode': 0, 'state': 'OК'}
        except Exception as e:
            print(e)
            assert cmdline(shell_command).decode('cp1251') == result


# Testing optional parameters host, port (star [host] [port])
@allure.feature("CLI check")
@pytest.mark.parametrize("shell_command, host, port, result", [
    ("cd .. & webcalculator.exe start 0.0.0.0", "0.0.0.0", f"{PORT}", "Запуск Веб-калькулятора на 0.0.0.0:17678\r\n"
                                                                    "Веб-калькулятор запущен на 0.0.0.0:17678\r\n"),
    ("cd .. & webcalculator.exe stop", f"{HOST}", f"{PORT}", "Пытаемся остановить Веб-калькулятор\r\n"
                                                        "Веб-калькулятор остановлен\r\n"),
    ("cd .. & webcalculator.exe start 127.5.5.5 5555", "127.5.5.5", "5555",
     "Запуск Веб-калькулятора на 127.5.5.5:5555\r\nВеб-калькулятор запущен на 127.5.5.5:5555\r\n"),
    ("cd .. & webcalculator.exe stop", f"{HOST}", f"{PORT}", "Пытаемся остановить Веб-калькулятор\r\n"
                                                        "Веб-калькулятор остановлен\r\n")],
    ids=["Калькулятор запущен", "Калькулятор остановлен", "Калькулятор запущен", "Калькулятор остановлен"])
@pytest.mark.usefixtures("setup_for_CLI_test_launching_with_params")
def test_launching_with_params(shell_command, host, port, result):
    with allure.step(f"Запущен на {host}:{port}"):
        try:
            respond = requests.get(f"http://{host}:{port}/api/state").json()
            assert cmdline(shell_command).decode('cp1251') == result and respond == {'statusCode': 0, 'state': 'OК'}
        except Exception as e:
            print(e)
            assert cmdline(shell_command).decode('cp1251') == result


if __name__ == "__main__":
    pytest.main()




