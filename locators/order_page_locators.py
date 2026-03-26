from selenium.webdriver.common.by import By


class OrderPageLocators:
    #FIRST_PAGE = By.XPATH, '//*[@id="accordion__heading-{}"]'
    #SECOND_PAGE = By.XPATH, '//*[@id="accordion__panel-{}"]'
    NAME_LOCATOR = By.XPATH, "//input[@placeholder='* Имя']"
    LAST_NAME_LOCATOR = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADDRESS_LOCATOR = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO_LOCATOR = By.XPATH, "//input[@placeholder='* Станция метро']"
    NUMBER_LOCATOR = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    METRO_FIRST_STATION_LOCATOR = By.XPATH, "(//button[contains(@class,'select-search__option')])[1]"
    NEXT_BUTTON_LOCATOR = By.XPATH, "(//button[text()='Далее'])"
    DATE_LOCATOR = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    DELIVERY_DATE_LOCATOR = By.XPATH, "//div[text()='* Срок аренды']"
    RENT_DURATION_DAY_LOCATOR = (By.XPATH, "//div[text()='сутки']")
    ORDER_BUTTON_LOCATOR = By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[.='Заказать']"
    CONFIRMATION_ORDER_LOCATOR = By.XPATH, "(//button[text()='Да'])"
    ORDER_SUCCESS = By.XPATH, "//div[contains(text(), 'Заказ оформлен')]"
    DAY_LOCATOR= By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='26']"

