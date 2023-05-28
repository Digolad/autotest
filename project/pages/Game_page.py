from selenium.webdriver.common.by import By
from framework.elements.Input import ElementsInput
from framework.elements.DropDown import DropDownElements
from framework.elements.CheckBox import CheckBoxElements
from framework.elements.Button import ElementsButton
from framework.elements.Form import FormElements
from framework.elements.Label import ElementsLabel
import random
from utils.FileManager import FileManager
from framework.pages.BasePage import BasePage
from project.test_data.Generate_test_data import GenerationTestData


class GamePage(BasePage):
    def __init__(self):
        super(GamePage, self).__init__(FormElements(self.LOCATOR_GAME_PAGE))

    fm = FileManager()
    LOCATOR_GAME_PAGE = (By.XPATH, '//div[@class="game view"]/div[@class="view__content"]')
    LOCATOR_CHOOSE_PASSWORD = (By.XPATH, '//input[@placeholder="Choose Password"]')
    LOCATOR_YOUR_EMAIL = (By.XPATH, '//input[@placeholder="Your email"]')
    LOCATOR_DOMAIN = (By.XPATH, '//input[@placeholder="Domain"]')
    LOCATOR_DROPDOWN = (By.XPATH, '//div[@class="dropdown dropdown--gray"]//div[@class="dropdown__opener"]')
    LOCATOR_DROPDOWN_LIST_SECOND_ITEM = (By.XPATH, '//div[@class="dropdown__list"]//div[2]')
    #LOCATOR_DROPDOWN_LIST = (By.XPATH, '//div[@class="dropdown__list"]//div[contains(@class,"dropdown__list-item")]')
    LOCATOR_DROPDOWN_LIST = (By.XPATH, '//div[@class="dropdown__list"]//div[@class="dropdown__list-item"]')
    LOCATOR_PAGE_INDICATOR = (By.XPATH, '//div[@class="page-indicator"]')
    LOCATOR_TERMS_AND_CONDITIONS = (By.XPATH,
                                    '//div[@class="login-form__section"]//a[@class="login-form__terms-conditions"]')
    LOCATOR_ACCEPT_BUTTON = (By.XPATH, '//button[@class="button button--solid button--blue"]')
    LOCATOR_HELP_FORM = (By.XPATH, '//div[@class="game view"]/div[contains(@class, "help-form")]')

    LOCATOR_SEND_BUTTON = \
        (By.XPATH, '//div[@class="align__cell u-right"]/button[@class="button button--solid button--blue help-form__send-to-bottom-button"]')
    LOCATOR_CARD1_NEXT_BUTTON = \
        (By.XPATH, '//div[@class="align__cell button-container__secondary"]/a[@class="button--secondary"]')

    LOCATOR_ACCEPT_CHECKBOX = (By.XPATH, '//span[@class="checkbox"]//span[@class="icon icon-check checkbox__check"]')
    LOCATOR_CARD2_INTERESTS = (By.XPATH,
                               '//div[@class="avatar-and-interests__interests-list"]//span[@class="checkbox small"]')
    LOCATOR_TIMER = (By.XPATH, '//div[@class="timer timer--white timer--center"]')
    LOCATOR_CARD2_UPLOAD = (By.XPATH,
                            '//p[@class="avatar-and-interests__text"]/a[@class="avatar-and-interests__upload-button"]')
    LOCATOR_COOKIES = (By.XPATH, '//div[@class="cookies"]')
    LOCATOR_COOKIES_NOT_REALLY_BUTTON = \
        (By.XPATH, '//div[@class="cookies"]//button[@class="button button--solid button--transparent"]')

    test_data = GenerationTestData().generation()

    def enter_password(self):
        password = ElementsInput(self.LOCATOR_CHOOSE_PASSWORD)
        password.enter_data_to_input(data=self.test_data['password'])

    def enter_email(self):
        email = ElementsInput(self.LOCATOR_YOUR_EMAIL)
        email.enter_data_to_input(data=self.test_data['email'])

    def enter_domain(self):
        domain = ElementsInput(self.LOCATOR_DOMAIN)
        domain.enter_data_to_input(data=self.test_data['domain'])

    def random_select_second_domain(self):
        domain_element = DropDownElements(self.LOCATOR_DROPDOWN)
        domain_element.click_on()
        dropdown = DropDownElements(self.LOCATOR_DROPDOWN_LIST)
        dropdown_list = dropdown.get_list_from_dropdown()
        rand = random.randrange(0, len(dropdown_list))
        dropdown_list[rand].click()

    def hidden_help_form(self) -> list:
        help_form = FormElements(self.LOCATOR_HELP_FORM)

        if help_form.check_form_exist() == True:
            button = ElementsButton(self.LOCATOR_SEND_BUTTON)
            button.click_on_button()

    def get_help_form_attribute(self):
        help_form = FormElements(self.LOCATOR_HELP_FORM)
        attribute = help_form.get_attribute_class()
        attribute = attribute.split()

        return attribute

    def uncheck_accept_checkbox(self):
        checkbox = CheckBoxElements(self.LOCATOR_ACCEPT_CHECKBOX)
        if checkbox.is_exist():
            checkbox.select_checkbox()

    def get_number_of_page(self):
        page = ElementsLabel(self.LOCATOR_PAGE_INDICATOR)
        number = page.get_text().split()
        return number[0]

    def click_on_next_card1_button(self):
        next_button = ElementsButton(self.LOCATOR_CARD1_NEXT_BUTTON)
        next_button.move_to_element()
        next_button.click_on_button()

    def choose_random_several_random_interest(self):
        checkboxes_list = CheckBoxElements(self.LOCATOR_CARD2_INTERESTS)
        checkboxes = checkboxes_list.get_checkbox_list()
        instance_count = self.fm.get_data_from_json_file()['instance_count']
        x = 0
        while x < instance_count:
            random_checkbox = random.randrange(0, len(checkboxes)-1)
            checkboxes[random_checkbox].click()
            x += 1

    def wait_until_cookies_visible(self):
        cookies_form = FormElements(self.LOCATOR_COOKIES)
        cookies_form.wait_presence_of_form_located()
        accept_button = ElementsButton(self.LOCATOR_COOKIES_NOT_REALLY_BUTTON)
        accept_button.click_on_button()

    def no_cookies_form_on_page(self):
        cookies_form = FormElements(self.LOCATOR_COOKIES)
        return cookies_form.check_form_exist()

    def get_text_of_timer(self):
        timer_on_page = ElementsLabel(self.LOCATOR_TIMER)
        return timer_on_page.get_text()
