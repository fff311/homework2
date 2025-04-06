import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests with")
    parser.addoption("--url", action="store", default="http://192.168.1.40:8080/", help="Base URL for the application")


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser").lower()
    base_url = request.config.getoption("--url")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromiumService())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(options=FFOptions(), service=FFService())
    elif browser_name == "edge":
        driver = webdriver.Edge(options=EdgeOptions(), service=EdgeService())
    else:
        raise ValueError("Некорректный браузер")
    driver.base_url = base_url
    yield driver
    driver.quit()





