import pytest
from utils.FileManager import FileManager
from framework.browser.Browser import Browser

import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger()


@pytest.fixture(scope="function", autouse=True)
def browser():
    """
    check configurations,
    get webdriver,
    if a test completed - close the browser
    :return:
    """
    fm = FileManager()
    logger.info("\n Start driver for test..")
    data = fm.get_data_from_json_file()
    mode = ''
    if data['browser']['mode']:
        mode = data['browser']['mode']
    browser_name = data['browser']['browser_name']

    Browser(browser_name, mode)
# Navigate to home page.
    Browser.get_page('https://userinyerface.com')

    yield

    logger.info("\n Quit driver..")
    Browser.close_the_browser()
