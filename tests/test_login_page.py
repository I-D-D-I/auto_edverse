import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from utils.data_generators import generate_login_page_user
import pytest


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
        
        
@pytest.mark.parametrize("email, password", [
    ("test@mail.ru", "wrong_password"),
    ("second@mail.ru", "qwerty"),
    ("third@mail.ru", "123456"),
], ids=["wrong_password", "another_user", "short_password"])
@allure.title("Логин с неверными данными: {email}")
@allure.feature("Авторизация")
def test_login_invalid(page: Page, email, password):
    with allure.step("Открываем страницу логина"):
        LoginPage(page).open("https://edversemovie.ru/login")

    with allure.step("Вводим email и пароль"):
        LoginPage(page).login(email, password)

    with allure.step("Проверяем, что остались на логине"):
        expect(page).to_have_url("https://edversemovie.ru/login")


@pytest.mark.parametrize(
    "attempt",
    range(3),
    ids=["attempt_1", "attempt_2", "attempt_3"]
)
@allure.title("Логин с рандомными данными Faker: {attempt}")
@allure.feature("Авторизация")
def test_login_with_faker(page: Page, attempt):

    user = generate_login_page_user()

    with allure.step("Открываем страницу логина"):
        login_page = LoginPage(page).open(
            "https://edversemovie.ru/login"
        )

    with allure.step(f"Вводим сгенерированные данные: {user['email']}"):
        login_page.login(
            user["email"],
            user["password"]
        )

        allure.attach(
            user["email"],
            name="Email",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Проверяем, что остались на странице логина"):
        expect(page).to_have_url(
            "https://edversemovie.ru/login"
        )