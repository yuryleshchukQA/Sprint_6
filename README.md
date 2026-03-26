# Sprint_6

Автотесты UI для учебного сервиса [Яндекс.Самокат](https://qa-scooter.praktikum-services.ru/): Selenium, Page Object, pytest, Allure.

## Стек

- Python 3.10+
- Mozilla Firefox (драйвер подхватывается Selenium Manager)
- Selenium WebDriver
- pytest
- allure-pytest

## Структура проекта

| Путь | Описание |
|------|----------|
| `pages/` | Page Object: `BasePage`, `MainPage`, `OrderPage`, `HeaderPage` |
| `locators/` | Локаторы по страницам/шапке |
| `test/` | Тесты и `conftest.py` (фикстура `driver`, `main_page`) |
| `data.py` | Ожидаемые ответы FAQ и данные для заказа |
| `urls.py` | URL-ы сервиса |


## Что покрыто тестами

- **Главная:** блок «Вопросы о важном» (параметризация по номерам вопросов).
- **Шапка:** логотип Яндекса (Дзен), логотип Самоката (возврат на главную).
- **Заказ:** позитивный сценарий с двумя точками входа «Заказать» и двумя наборами данных.