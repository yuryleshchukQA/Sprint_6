import allure

from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    @allure.step('Клик по логотипу Яндекса')
    def click_yandex_logo(self):
        self.click_to_element(HeaderLocators.YANDEX_LOGO)

    @allure.step('Дождаться второй вкладки и переключиться на неё')
    def switch_to_second_tab(self):
        self.wait_second_tab()
        self.switch_to_window_by_index(1)

    @allure.step('Дождаться, пока в адресной строке появится dzen.ru')
    def wait_until_dzen_url(self):
        self.wait_url_contains('dzen.ru')

    @allure.step('Клик по логотипу Самоката')
    def click_scooter_logo(self):
        self.click_to_element(HeaderLocators.SCOOTER_LOGO)
