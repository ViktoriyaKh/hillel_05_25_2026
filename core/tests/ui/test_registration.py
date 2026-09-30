import allure
from playwright.sync_api import expect


@allure.feature("Registration")
def test_registration(registration_page):
    with allure.step("Fill registration form"):
        registration_page.name.fill("Victoria")
        registration_page.last_name.fill("Khromenko")
        registration_page.email.fill("victoria_test_2028@example.com")
        registration_page.password.fill("Test12345!")
        registration_page.re_password.fill("Test12345!")

    with allure.step("Click Register"):
        registration_page.register_button.click()

    with allure.step("Check successful registration"):
        expect(registration_page.garage_title).to_be_visible()