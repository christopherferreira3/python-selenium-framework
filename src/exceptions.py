import allure
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class FrameworkException(NoSuchElementException, TimeoutException):
    def __init__(self, message: str, driver: webdriver):
        super().__init__(msg=message)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
        # Create a request to post the failed step
        # Send a notification somewhere to report the bug
