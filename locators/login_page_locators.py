from selenium.webdriver.common.by import By


class LoginPageLocator(object):
    LOGIN_TITLE = (By.XPATH, '//h3["Login"]')
    EMAIL_INPUT_FIELD = (By.ID, 'input_email')
    PASSWORD_INPUT_FIELD = (By.ID, 'input_password')
    SUBMIT_BUTTON = (By.NAME, 'form.submitted')