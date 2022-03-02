from .driver_factory import DriverFactory


class TestContext:
    def __init__(self, browser: str):
        self.driver_factory = DriverFactory(browser=browser)
        self.browser = browser
        self.custom_context = {}

    def get_custom_context(self):
        return self.custom_context

    def create_driver(self):
        return self.driver_factory.get_webdriver()
