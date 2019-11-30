import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

TIMEOUT_UNTIL_ITEM_APPEARS = 5


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    browser_name = request.config.getoption("browser_name") # get browser name
    browser_lang = request.config.getoption("language") # get browser language
    print(browser_lang)
    browser = None  # clear browser
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
        browser = webdriver.Chrome(options=options) # start chrome browser with options
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", browser_lang)
        browser = webdriver.Firefox(firefox_profile=fp) # start chrome browser with options
    else:
        raise pytest.UsageError("Browser {} still is not implemented".format(browser_name))
    browser.implicitly_wait(TIMEOUT_UNTIL_ITEM_APPEARS) # waited for UNTIL_ITEM_APPEARS
    yield browser
    print("\nquit browser..")
    browser.quit()


def pytest_addoption(parser):
    """Method to add pytest startup options

    :param parser: Options parser
    :return None
    """
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en", help="Choose your language")
