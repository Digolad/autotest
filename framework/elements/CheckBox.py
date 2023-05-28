from framework.elements.Base_element import BaseElement


class CheckBoxElements(BaseElement):

    def select_checkbox(self):
        self._find_element().click()

    def get_checkbox_list(self):
        return self._wait_for_elements()
