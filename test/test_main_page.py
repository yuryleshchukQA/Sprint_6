import allure
import pytest

from data import answers_data
from urls import URL_MAIN_PAGE


@allure.title('Тесты на проверку вопросов-ответов')
class TestMainPage:
    @pytest.mark.parametrize(
        'num',
        [0, 1, 2, 3, 4, 5, 6, 7]
    )
    def test_questions_and_answers(self, num, main_page):
        main_page.go_to_url(URL_MAIN_PAGE)
        assert main_page.check_question_and_answer(num) == answers_data[num], f'Check answer for {num} question'
