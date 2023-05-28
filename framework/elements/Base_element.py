from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from framework.browser.Browser import Browser
from utils.FileManager import FileManager


class BaseElement:
    def __init__(self, locator):
        self.locator = locator

    wait_until_element_load = FileManager().get_data_from_json_file()['wait_until_load']

    def _wait_for_element(self, time=wait_until_element_load, poll_frequency=1):
        return WebDriverWait(Browser.driver, time, poll_frequency).until(EC.presence_of_element_located(self.locator),
                                                      message=f"Can't find element by locator {self.locator}")

    def _find_element(self):
        return Browser.driver.find_element(*self.locator)

    def _find_elements(self):
        return Browser.driver.find_elements(*self.locator)

    def is_exist(self) -> bool:
        if len(self._find_elements()) > 0:
            return True
        else:
            return False

    def wait_for_exist(self) -> bool:
        pass

    def _wait_for_elements(self, time=wait_until_element_load, poll_frequency=1):
        return WebDriverWait(Browser.driver, time, poll_frequency).until(EC.presence_of_all_elements_located(self.locator),
                                                      message=f"Can't find elements by locator {self.locator}")

    def wait_until_text_update(self, text, time=wait_until_element_load, poll_frequency=1):
        return WebDriverWait(Browser.driver, time, poll_frequency).until(EC.text_to_be_present_in_element(self.locator, text))

    def wait_until_element_loaded(self, time=wait_until_element_load, poll_frequency=1):
        return WebDriverWait(Browser.driver, time, poll_frequency).until(EC.visibility_of_element_located(self.locator))

    def wait_until_presence_of_element_located(self, time=wait_until_element_load, poll_frequency=1):
        return WebDriverWait(Browser.driver, time, poll_frequency).until(EC.presence_of_element_located(self.locator))

    def move_to_element(self):
        if self.is_exist():
            actions = ActionChains(Browser.driver)
            actions.move_to_element(self._find_element()).perform()

    def get_attribute_of_element(self, attribute: str):
        return self._find_element().get_attribute(attribute)
