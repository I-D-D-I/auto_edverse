from faker import Faker

fake = Faker()


def generate_login_page_user():
    return {
        "email": fake.email(),
        "password": fake.password(length=12),
    }

def generate_register_page_user():
    password = fake.password(length=12)

    return {
        "name": fake.name(),
        "email": fake.email(),
        "password": password,
        "repeat_password": password + "1",
    }