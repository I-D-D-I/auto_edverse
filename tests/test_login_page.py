import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from utils.data_generators import generate_login_page_user


@allure.title("Тест авторизации с неверными данными")
@allure.feature("Авторизация")
def test_login_with_wrong_password(page: Page):
    user = generate_login_page_user()
    login_page = LoginPage(page).open("https://edversemovie.ru/login")

    with allure.step("Вводим email"):
        login_page.email_input.fill(user["email"])
        allure.attach(user["email"], name="Email", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Вводим пароль"):
        login_page.password_input.fill(user["password"])
        allure.attach(user["password"], name="Пароль", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Нажимаем кнопку входа"):
        login_page.login_button.click()
        page.wait_for_timeout(1000)  # Ждем ответа

    with allure.step("Проверяем URL (остались на логине)"):
        expect(page).to_have_url("https://edversemovie.ru/login")