class BasePage:
    def __init__(self, element):
        self.element = element

    def is_open(self) -> bool:
       return self.element.is_exist()
