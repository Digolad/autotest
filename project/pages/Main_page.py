from framework.elements.Label import ElementsLabel
from selenium.webdriver.common.by import By
from framework.pages.BasePage import BasePage


class MainPage(BasePage):
    def __init__(self):
        super().__init__((ElementsLabel(self.LOCATOR_WELCOME_PAGE)))

    LOCATOR_LABEL_HERE = (By.XPATH, '//div[@class="start view view--center"]//a[@class="start__link"]')
    LOCATOR_WELCOME_PAGE = \
        (By.XPATH, '//div[@class="start view view--center"]//div[@class="view__row"]/p[@class="start__paragraph"]')

    def click_on_text_here(self):
        label = ElementsLabel(self.LOCATOR_LABEL_HERE)
        label.click_on_text()

    def get_welcome_text(self):
        label = ElementsLabel(self.LOCATOR_WELCOME_PAGE)
        return label.get_text()

