from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from math import log, sin


class BasePage():
    def __init__(self, browser, url, timeout=10):
        """Base class for the web page

        :param selenium.webdriver.Remote browser: Selenium WebDriver instance
        :param str url: Link to the page
        :param int timeout: implicitly wait timeout
        """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """Open the given web page in the browser

        :return: None
        """
        self.browser.get(self.url)

    def solve_quiz_and_get_code(self):
        """ Method for solving alert quiz

        """
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(log(abs((12 * sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_element_present(self, how, what):
        """ Check that the element exists

        :param how: Choosing a selector search method
        :param what: Element selector
        :return bool:
        """
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

