import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Клик на вопрос')
    def click_to_question(self,num):
        locators_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR,num)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.click_to_element(locators_q_formatted)

    @allure.step('Получение ответа')
    def get_answer_text(self, num):
        locators_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(locators_a_formatted)

    @allure.step('Проверка вопроса-ответа')
    def check_question_and_answer(self, num):
        self.click_to_question(num)
        return self.get_answer_text(num)




