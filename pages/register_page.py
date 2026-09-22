from playwright.sync_api import Page
from pages.base_page import BasePage
from locators.register_locators import RegisterLocators

class RegisterPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.name_input = page.locator(RegisterLocators.NAME_INPUT)
        self.email_input = page.locator(RegisterLocators.EMAIL_INPUT)
        self.password_input = page.locator(RegisterLocators.PASSWORD_INPUT)
        self.repeat_password_input = page.locator(RegisterLocators.PASSWORD_REPEAT_INPUT)
        self.register_button = page.locator(RegisterLocators.REGISTER_BUTTON)
        self.login_link = page.locator(RegisterLocators.LOGIN_LINK)
        
    def register(self, name:str, email: str, password: str, repeat_password: str):
        """Заполняет форму и нажимает «Зарегистрироваться»."""
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.repeat_password_input.fill(repeat_password)
        self.register_button.click()
        return self