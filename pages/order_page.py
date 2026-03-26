import time

import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Заполняем первую страницу заказа")
    def set_first_page_info(self, data):
        self.click_to_element(OrderPageLocators.NAME_LOCATOR)
        self.add_text_to_element(OrderPageLocators.NAME_LOCATOR, data['name'])
        self.click_to_element(OrderPageLocators.LAST_NAME_LOCATOR)
        self.add_text_to_element(OrderPageLocators.LAST_NAME_LOCATOR, data['last_name'])
        self.click_to_element(OrderPageLocators.METRO_LOCATOR)
        self.add_text_to_element(OrderPageLocators.METRO_LOCATOR, data['metro'])
        self.click_to_element(OrderPageLocators.METRO_FIRST_STATION_LOCATOR)
        self.click_to_element(OrderPageLocators.NUMBER_LOCATOR)
        self.add_text_to_element(OrderPageLocators.NUMBER_LOCATOR, data['number'])
        self.click_to_element(OrderPageLocators.NEXT_BUTTON_LOCATOR)


    @allure.step("Заполняем вторую страницу заказа")
    def set_second_page_info(self, data_2):
        self.click_to_element(OrderPageLocators.DATE_LOCATOR)
        self.add_text_to_element(OrderPageLocators.DATE_LOCATOR, data_2['date'])
        self.click_to_element(OrderPageLocators.DAY_LOCATOR)
        self.click_to_element(OrderPageLocators.DELIVERY_DATE_LOCATOR)
        self.click_to_element(OrderPageLocators.RENT_DURATION_DAY_LOCATOR)
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_LOCATOR)
        self.click_to_element(OrderPageLocators.CONFIRMATION_ORDER_LOCATOR)

    @allure.step("Отправка заказа")
    def set_order(self, data):
        self.set_first_page_info(data)
        self.set_second_page_info(data)


