from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, '//*[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//*[@id="accordion__panel-{}"]'
    QUESTION_LOCATOR_TO_SCROLL = By.XPATH, '//*[@id="accordion__heading-7"]'
    ORDER_BUTTON_UP = By.XPATH, "(//button[text()='Заказать'])[1]"
    ORDER_BUTTON_DOWN = By.XPATH, "(//button[text()='Заказать'])[2]"
