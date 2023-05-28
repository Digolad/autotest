from framework.elements.Base_element import BaseElement


class DropDownElements(BaseElement):

    def click_on(self):
        if self.is_exist():
            self._find_element().click()

    def wait_until_dropdown_items_load(self):
        return self.wait_until_element_loaded()

    def get_list_from_dropdown(self):
        if self.is_exist():
            return self._find_elements()
