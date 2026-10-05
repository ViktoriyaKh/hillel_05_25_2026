import allure


@allure.feature("Registration")
def test_registration(registration_page):
    registration_page.register_user(
        "Victoria",
        "Khromenko",
        "victoria_test_2019@example.com",
        "Test12345!"
    )
    registration_page.check_registration()