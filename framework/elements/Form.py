from framework.elements.Base_element import BaseElement


class FormElements(BaseElement):

    def get_attribute_class(self):
        if self.is_exist():
            return self.get_attribute_of_element("class")

    def wait_presence_of_form_located(self):
        self.wait_until_presence_of_element_located()

    def check_form_exist(self) -> bool:
        return self.is_exist()
