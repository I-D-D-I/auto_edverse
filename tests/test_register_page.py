import allure
from playwright.sync_api import Page, expect
from pages.register_page import RegisterPage
from utils.data_generators import generate_register_page_user


@allure.title("Тест регистрации с несовпадающими паролями")
@allure.feature("Регистрация")
def test_register_with_wrong_repeat_password(page: Page):
    user = generate_register_page_user()
    register_page = RegisterPage(page).open("https://edversemovie.ru/register")

    with allure.step("Вводим name"):
        register_page.name_input.fill(user["name"])
        allure.attach(user["name"], name="name", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Вводим email"):
        register_page.email_input.fill(user["email"])
        allure.attach(user["email"], name="Email", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Вводим пароль"):
        register_page.password_input.fill(user["password"])
        allure.attach(user["password"], name="Пароль", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Вводим пароль повторно"):
        register_page.repeat_password_input.fill(user["repeat_password"])
        allure.attach(user["repeat_password"], name="Повторный пароль", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Нажимаем кнопку регистрации"):
        register_page.register_button.click()
        page.wait_for_timeout(1000)  # Ждем ответа

    with allure.step("Проверяем URL (остались на странице регистрации) и что регистрация не произошла"):
        expect(page).to_have_url("https://edversemovie.ru/register")