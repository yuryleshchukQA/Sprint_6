from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def find_element_with_wait(self,locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, some):
        self.wait.until(expected_conditions.element_to_be_clickable(some))
        self.driver.find_element(*some).click()

    def wait_text(self, locator, text):
        self.wait.until_not(expected_conditions.text_to_be_present_in_element_value(locator,text))
        return self.driver.find_element(*locator).text

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_second_tab(self):
        self.wait.until(expected_conditions.number_of_windows_to_be(2))

    def wait_url_contains(self, text):
        self.wait.until(expected_conditions.url_contains(text))

    def switch_to_window_by_index(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method,locator

    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
