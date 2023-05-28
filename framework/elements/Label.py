from framework.elements.Base_element import BaseElement


class ElementsLabel(BaseElement):

    def click_on_text(self):
        if self.is_exist():
            button = self._find_element()
            button.click()

    def get_text(self):
        if self.is_exist():
            return self._find_element().text
