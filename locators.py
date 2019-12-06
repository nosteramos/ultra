from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    LOGIN_EMAIL = (By.NAME, 'email')
    LOGIN_PASSWORD = (By.NAME, 'pass')
    LOGIN_BTN = (By.CSS_SELECTOR, '[data-testid="royal_login_button"]')


class BaseFaceBookPageLocators(object):
    LOGGED_IN_INDICATOR = (By.CSS_SELECTOR, '[aria-label^="What\'s on your mind,"]')


class UpperMenuLocators(object):
    PROFILE_ICON = (By.CSS_SELECTOR, '[data-click="profile_icon"]')


class ProfilePageLocators(object):
    PROFILE_PAGE_INDICATOR = (By.CSS_SELECTOR, '[data-testid="profile_name_in_profile_page"]')
    ABOUT_TAB_INDICATOR = (By.XPATH, "//*[contains(text(), 'About')]")
    ABOUT_TAB = (By.CSS_SELECTOR, '[data-tab-key="about"]')
