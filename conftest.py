import pytest
from selenium import webdriver
from settings import REMOTE_BROWSER_VERSION


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser used")
    parser.addoption("--headless", action="store_const", const=True, default=False, help="headless used")
    parser.addoption("--selenoid", action="store_const", const=True, default=False, help="use selenoid hub")


@pytest.fixture()
def driver(request):
    global driver
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    selenoid = request.config.getoption("--selenoid")

    match browser:
        case "chrome":
            options = webdriver.ChromeOptions()
        case "firefox":
            options = webdriver.FirefoxOptions()
        case _:
            raise ValueError("Необходимо указать корректное имя браузера")
    if headless:
        options.headless = True

    if selenoid:
        selenoid_capabilities = {
            "enableVNC": False,
            "enableVideo": False
        }
        options.set_capability("selenoid:options", selenoid_capabilities)
        options.browser_version = REMOTE_BROWSER_VERSION

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=options)
    else:
        match browser:
            case "chrome":
                driver = webdriver.Chrome(options=options)
            case "firefox":
                driver = webdriver.Firefox(options=options)

    yield driver
    driver.quit()
