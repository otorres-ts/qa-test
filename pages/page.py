from selenium.webdriver.support import expected_conditions as ec


class Page(object):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait