import allure

from src.pages.home_page import HomePage
from src.test_base import TestBase


class HomePageTest(TestBase):
    URL = "https://www.python.org/"

    @allure.description("""
    Opens the Python HomePage and checks if the python logo is displayed
    """)
    def test_home_page(self):
        self.driver.get(self.URL)
        self.assertEqual(self.driver.current_url, self.URL, "Current URL is different than it it supposed to")

        home_page = HomePage(self.driver)
        self.assertTrue(home_page.get_logo().is_displayed())

