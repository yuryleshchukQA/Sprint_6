
import allure

from pages.header_page import HeaderPage
from urls import URL_MAIN_PAGE, URL_ORDER_PAGE


@allure.title('Шапка: логотипы Яндекс и Самокат')
class TestHeader:
    @allure.title('Логотип Яндекса открывает Дзен')
    def test_yandex_logo_opens_dzen(self, driver):
        page = HeaderPage(driver)
        page.go_to_url(URL_MAIN_PAGE)
        page.click_yandex_logo()
        page.switch_to_second_tab()
        page.wait_until_dzen_url()
        url = page.driver.current_url
        assert 'dzen.ru' in url
        assert 'yredirect' in url

    @allure.title('Логотип Самоката ведёт на главную')
    def test_scooter_logo_opens_main(self, driver):
        page = HeaderPage(driver)
        page.go_to_url(URL_ORDER_PAGE)
        page.click_scooter_logo()
        assert page.driver.current_url == URL_MAIN_PAGE
