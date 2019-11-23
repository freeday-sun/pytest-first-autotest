import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    browser_name = request.config.getoption("browser_name")
    browser_lang = request.config.getoption("language")
    print(browser_lang)
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", browser_lang)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("Browser {} still is not implemented".format(browser_name))
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en", help="Choose your language")
