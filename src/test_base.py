import logging
import unittest
from .test_context import TestContext


class TestBase(unittest.TestCase, TestContext):

    def setUp(self) -> None:
        self.context = TestContext("chrome")
        self.driver = self.context.create_driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
