import pytest
from subprocess import PIPE, Popen


# Getting stdout and executing command
def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]


# Testing defaults parameters (start, stop, restart)
@pytest.mark.parametrize("str, output", [
    ("cd .. & webcalculator.exe start", "Сервер уже запущен\r\n"),
    ("cd .. & webcalculator.exe restart", "Пытаемся остановить Веб-калькулятор\r\nВеб-калькулятор остановлен\r\n"
                                          "Запуск Веб-калькулятора на 127.0.0.1:17678\r\n"
                                          "Веб-калькулятор запущен на 127.0.0.1:17678\r\n"),
    ("cd .. & webcalculator.exe stop", "Пытаемся остановить Веб-калькулятор\r\nВеб-калькулятор остановлен\r\n"),
    ("cd .. & webcalculator.exe restart", 'Веб-калькулятор не запущен. Используйте команду "start"\r\n')])
def test_launching(str, output):
    assert cmdline(str).decode('cp1251') == output


# Testing optional parameters host, port (star [host] [port])
@pytest.mark.parametrize("str, output", [
    ("cd .. & webcalculator.exe start 0.0.0.0", "Запуск Веб-калькулятора на 0.0.0.0:17678\r\n"
                                                "Веб-калькулятор запущен на 0.0.0.0:17678\r\n"),
    ("cd .. & webcalculator.exe stop", "Пытаемся остановить Веб-калькулятор\r\nВеб-калькулятор остановлен\r\n"),
    ("cd .. & webcalculator.exe start 127.5.5.5 5555", "Запуск Веб-калькулятора на 127.5.5.5:5555\r\n"
                                                         "Веб-калькулятор запущен на 127.5.5.5:5555\r\n"),
    ("cd .. & webcalculator.exe stop", "Пытаемся остановить Веб-калькулятор\r\nВеб-калькулятор остановлен\r\n"),
    ("cd .. & webcalculator.exe start", "Запуск Веб-калькулятора на 127.0.0.1:17678\r\n"
                                        "Веб-калькулятор запущен на 127.0.0.1:17678\r\n"),
    ])
def test_launching_with_params(str, output):
    assert cmdline(str).decode('cp1251') == output


if __name__ == "__main__":
    pytest.main()




