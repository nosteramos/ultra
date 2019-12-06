import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from TestsData import TestData
import page


class Tests(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome("chromedriver.exe", options=options)
        self.driver.get("https//facebook.com")
        login_page = page.LoginPage(self.driver)
        if login_page.is_displayed():
            login_page.login(TestData.FACEBOOK_USER, TestData.FACEBOOK_PASSWORD)
        home_page = page.HomePage(self.driver)
        assert home_page.is_logged_in()

    def test_facebook(self):
        home_page = page.HomePage(self.driver)
        assert home_page.find(TestData.MY_NAME)

        home_page.show_profile()

        profile_page = page.ProfilePage(self.driver)
        profile_page.navigate_to_about()  # Navigate to AND Verify the correct page is displayed

        assert profile_page.birthday_found(TestData.BIRTHDAY)

        pass

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
