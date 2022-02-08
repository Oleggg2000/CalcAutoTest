from selenium import webdriver
import pytest

if __name__ == "__main__":
    pytest.main()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    options.headless = True
    options.add_argument("--windowws-size=1920,1080")