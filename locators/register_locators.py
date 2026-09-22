class RegisterLocators:
    """Локаторы для страницы регистрации"""
    # Поля ввода
    NAME_INPUT = "[data-qa-id='register_full_name_input']"
    EMAIL_INPUT = "[data-qa-id='register_email_input']"
    PASSWORD_INPUT = "[data-qa-id='register_password_input']"
    PASSWORD_REPEAT_INPUT = "[data-qa-id='register_password_repeat_input']"
    # Кнопки
    REGISTER_BUTTON = "[data-qa-id='register_submit_button']"
    # Войти
    LOGIN_LINK = ("link", "Войти")