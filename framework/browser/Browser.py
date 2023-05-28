from framework.browser.BrowserFactory import WebdriverFactory
from framework.browser.Singleton import MetaSingleton


class Browser(metaclass=MetaSingleton):
    driver = None

    @classmethod
    def __init__(cls, browser, mode):
         cls.driver = WebdriverFactory.get_webdriver(browser, mode)

    @classmethod
    def get_page(cls, url):
        cls.driver.get(url)

    @classmethod
    def close_the_browser(cls):
        cls.driver.quit()
        MetaSingleton.clean(MetaSingleton)

    def scroll_page_body_by_height(self):
        Browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

