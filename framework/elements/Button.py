from framework.elements.Base_element import BaseElement


class ElementsButton(BaseElement):

    def click_on_button(self):
        if self.is_exist():
            self._find_element().click()
        else:
            print('The element does not exist')
