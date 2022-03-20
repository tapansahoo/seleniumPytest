from seleniumpagefactory.Pagefactory import PageFactory

class BasePage(PageFactory):
    def __init__(self, driver):       # It is necessary to to initialise driver as page class member to implement Page Factory

        self.driver = driver