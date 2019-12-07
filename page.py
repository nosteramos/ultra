from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from locators import LoginPageLocators, BaseFaceBookPageLocators, UpperMenuLocators, ProfilePageLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def find(self, text):
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//*[contains(text(), '" + text + "')]")))
            # Consider replacing with JQuery for better performance
        except:
            return False

        return True


class BaseFaceBookPage(BasePage):

    def is_logged_in(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            elm = wait.until(
                expected_conditions.presence_of_element_located(BaseFaceBookPageLocators.LOGGED_IN_INDICATOR))
        except:
            return False

        return True


class HomePage(BaseFaceBookPage):

    def show_profile(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(UpperMenuLocators.PROFILE_ICON)).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(ProfilePageLocators.PROFILE_PAGE_INDICATOR))

    def show_about(self):
        pass


class LoginPage(BaseFaceBookPage):
    def login(self, email, password):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(LoginPageLocators.LOGIN_EMAIL)).send_keys(email)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(LoginPageLocators.LOGIN_PASSWORD)).send_keys(password)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(LoginPageLocators.LOGIN_BTN)).submit()

    def is_displayed(self):
        try:
            li = WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located(LoginPageLocators.LOGIN_BTN))
            em = WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located(LoginPageLocators.LOGIN_EMAIL))
            pa = WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located(LoginPageLocators.LOGIN_PASSWORD))
            return True
        except:
            return False


class ProfilePage(BaseFaceBookPage):
    def navigate_to_about(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(ProfilePageLocators.ABOUT_TAB)).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(ProfilePageLocators.ABOUT_TAB_INDICATOR))

    def birthday_found(self, date):
        self.navigate_to_about()
        date_str = date.strftime("%B %d, %Y")
        return self.find(date_str)

    def name_found(self, name):
        self.navigate_to_about()
        return self.find(name)
