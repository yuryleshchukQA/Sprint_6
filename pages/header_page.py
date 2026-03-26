import allure
from selenium.webdriver.support.ui import WebDriverWait

from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


def second_tab_opened(driver):
    return len(driver.window_handles) >= 2


def dzen_url_in_address_bar(driver):
    return 'dzen.ru' in driver.current_url


class HeaderPage(BasePage):
    @allure.step('Клик по логотипу Яндекса')
    def click_yandex_logo(self):
        self.click_to_element(HeaderLocators.YANDEX_LOGO)

    @allure.step('Дождаться второй вкладки и переключиться на неё')
    def switch_to_second_tab(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(second_tab_opened)
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Дождаться, пока в адресной строке появится dzen.ru')
    def wait_until_dzen_url(self):
        wait = WebDriverWait(self.driver, 25)
        wait.until(dzen_url_in_address_bar)

    @allure.step('Клик по логотипу Самоката')
    def click_scooter_logo(self):
        self.click_to_element(HeaderLocators.SCOOTER_LOGO)
