import logging

import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from ..exceptions import FrameworkException


class HomePage:

    python_logo = (By.CLASS_NAME, "python-logo")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Getting the python header logo")
    def get_logo(self) -> WebElement:
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.python_logo)
            )
            return element
        except TimeoutException as e:
            raise FrameworkException("Logo not Found", self.driver)

