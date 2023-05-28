from selenium import webdriver


class WebdriverFactory:

    @staticmethod
    def get_webdriver(browser_name, mode):

        if browser_name == 'firefox':
            return webdriver.Firefox()

        elif browser_name == 'chrome':
            browser_mode = webdriver.ChromeOptions()
            browser_mode.add_argument(mode)
            browser_mode.add_argument("--start-fullscreen")

            return webdriver.Chrome(options=browser_mode)

        elif browser_name == 'ie':
            return webdriver.Ie()

        raise Exception("No such " + browser_name + " browser exists")
