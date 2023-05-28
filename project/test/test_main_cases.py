from project.pages.Main_page import MainPage
from project.pages.Game_page import GamePage

import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger()


class TestUserinterface:

    def test_case_1(self):
        main_page = MainPage()
        rr = main_page.is_open()
        assert main_page.is_open(), 'The Main page is not loaded'
        logger.info('\nThe Main page loaded')

        main_page.click_on_text_here()
        game_page = GamePage()
        assert game_page.is_open(), 'The Game page is not loaded'
        logger.info('\nThe Game page loaded')

        assert game_page.get_number_of_page() == '1', 'The card 1 is not opening'
        logger.info('The card 1 opened')

        game_page.enter_password()
        game_page.enter_email()
        game_page.enter_domain()
        game_page.random_select_second_domain()
        game_page.uncheck_accept_checkbox()
        game_page.click_on_next_card1_button()
        assert game_page.get_number_of_page() == '2', 'The card 2 is not opening'
        logger.info('The card 2 opened')
        game_page.choose_random_several_random_interest()

    def test_case_2(self):
        main_page = MainPage()
        assert 'Hi and welcome to User Inyerface' in main_page.get_welcome_text(), 'The main page is not loaded'
        logger.info('\nThe main page loaded')
        main_page.click_on_text_here()
        game_page = GamePage()
        game_page.hidden_help_form()
        check_form_hidden = game_page.get_help_form_attribute()
        assert check_form_hidden[len(check_form_hidden)-1] == 'is-hidden', 'The form does not hidden'
        logger.info('The form is hidden')

    def test_case_3(self):
        main_page = MainPage()
        assert 'Hi and welcome to User Inyerface' in main_page.get_welcome_text(), 'The main page is not loaded'
        logger.info('\nThe main page loaded')

        # main_page.click_on_text_here()
        # game_page = GamePage()
        #
        # assert game_page.get_number_of_page() == '1', 'The card 1 is not opening'
        # logger.info('The card 1 opened')
        #
        # game_page.enter_password()
        # game_page.enter_email()
        # game_page.enter_domain()
        # game_page.select_second_domain()
        # game_page.uncheck_accept_checkbox()
        # game_page.click_on_next_card1_button()
        #
        # assert game_page.get_number_of_page() == '2', 'The card 2 is not opening'
        # logger.info('The card 2 opened')
        #
        # game_page.choose_random_several_random_interest()
    #
    # def test_case_2(self):
    #     main_page = MainPage()
    #     assert 'Hi and welcome to User Inyerface' in main_page.get_welcome_text(), 'The main page is not loaded'
    #     logger.info('\nThe main page loaded')
    #     main_page.click_on_text_here()
    #     game_page = GamePage()
    #     game_page.hidden_help_form()
    #     check_form_hidden = game_page.get_help_form_attribute()
    #     assert check_form_hidden[len(check_form_hidden)-1] == 'is-hidden', 'The form does not hidden'
    #     logger.info('The form is hidden')
    #
    # def test_case_3(self):
    #     main_page = MainPage()
    #     assert 'Hi and welcome to User Inyerface' in main_page.get_welcome_text(), 'The main page is not loaded'
    #     logger.info('\nThe main page loaded')
    #     main_page.click_on_text_here()
    #     game_page = GamePage()
    #     game_page.wait_until_cookies_visible()
    #     logger.info('visible')
    #     assert game_page.no_cookies_form_on_page() == False, 'The cookies form still displays'
    #
    # def test_case_4(self):
    #     main_page = MainPage()
    #     assert 'Hi and welcome to User Inyerface' in main_page.get_welcome_text(), 'The main page is not loaded'
    #     logger.info('\nThe main page loaded')
    #     main_page.click_on_text_here()
    #     game_page = GamePage()
    #     timer_on_page = game_page.get_text_of_timer()
    #     assert '00:00:00' in timer_on_page,'The tome of page does not start with 00:00:00'
    #     logger.info('The time starts with 00:00:00')
    def test_case_4(self):
        main_page = MainPage()
        assert 'Hi and welcome to User Inyerface' in main_page.get_welcome_text(), 'The main page is not loaded'
        logger.info('\nThe main page loaded')
        main_page.click_on_text_here()
        game_page = GamePage()
        timer_on_page = game_page.get_text_of_timer()
        assert '00:00:00' in timer_on_page, 'The tome of page does not start with 00:00:00'
        logger.info('The time starts with 00:00:00')
