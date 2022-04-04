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


# Using for setup and teardown all session
@pytest.fixture(scope="session", autouse=True)
def setup_app():
    cmdline("cd ..&webcalculator.exe start").decode('cp1251')
    yield
    cmdline("cd ..&webcalculator.exe stop").decode('cp1251')


# Using for test_launching_with_params() test
@pytest.fixture(scope="function")
def setup_for_CLI_test_launching_with_params(request):
    cmdline("cd ..&webcalculator.exe stop").decode('cp1251')
    yield
    cmdline("cd ..&webcalculator.exe start").decode('cp1251')
