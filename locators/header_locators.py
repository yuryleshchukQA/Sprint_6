from selenium.webdriver.common.by import By


class HeaderLocators:
    YANDEX_LOGO = By.XPATH, "//img[@alt='Yandex']/ancestor::a[1]"
    SCOOTER_LOGO = By.XPATH, "//a[contains(@class,'Header_LogoScooter')]"
