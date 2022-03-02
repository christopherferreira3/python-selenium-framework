from selenium import webdriver
import logging


class DriverFactory:
    def __init__(self, browser: str):
        logging.info("Creating a driver for {browser}".format(browser=browser))
        self.browser = browser

    def get_webdriver(self) -> webdriver:
        options = None
        if self.browser == "chrome":
            options = webdriver.ChromeOptions()
            options.set_capability("se:recordVideo", True)
        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=options
        )
        driver.maximize_window()
        return driver
