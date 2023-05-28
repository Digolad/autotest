from framework.elements.Base_element import BaseElement


class ElementsInput(BaseElement):

    def enter_data_to_input(self, data):
        if self.is_exist():
            new_input = self._find_element()
            new_input.clear()
            new_input.send_keys(data)
