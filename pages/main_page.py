from pages.base_page import BasePage


class MainPage(BasePage):

    PRESS_ENTER_LOCATOR = "//div[@class='header-toolbar-buttons']/button/span[2]" #Кнопка Войти
    SITE_LOCATOR = "https://allcedo.ru/"
    REGISTRATION_BUTTON_LOCATOR = "//div[@class='loginSocial-register-button']"
    EMAIL_LOCATOR = "//input[@type='email']"
    MOBILE_LOCATOR = "//input[@type='phone']"
    PASSWORD_LOCATOR = "//input[@type='password']"
    ENTER_BUTTON = "//form[@class = 'login']//button"
    login_locator = "zarembawork@yandex.ru"
    password_locator ="allcedo1234"
    CREATE_LOT_BUTTON = "//a[contains(@href,'/account/lot/create')]"
    GET_USER_NAME = "//span[@class='header-toolbar-buttons-dashboard--username block']"
    CHECK_ROBOT_LOCATOR = "//span[@class = 'error--text']"

    def open_mail_page(self):
        self.url_open(self.SITE_LOCATOR)

    def open_registration_form(self):
        self.click(self.PRESS_ENTER_LOCATOR)

    def input_credentials(self):
       self.send_text(self.EMAIL_LOCATOR, self.login_locator)
       self.send_text(self.PASSWORD_LOCATOR, self.password_locator)
       self.click(self.ENTER_BUTTON)

    def create_lot_button(self):
        self.click_the_button_action(self.CREATE_LOT_BUTTON)

    def user_steps_main_page(self):
        self.open_mail_page()
        self.open_registration_form()
        self.input_credentials()

    def get_user_text(self):
        return self.get_element_text(self.GET_USER_NAME)

    def get_robot_text(self):
        return self.get_element_text(self.CHECK_ROBOT_LOCATOR)