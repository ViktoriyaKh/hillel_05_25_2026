import allure
from playwright.sync_api import Page, expect


class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.sign_up_button = page.get_by_role("button", name="Sign up", exact=True)
        self.name = page.locator("#signupName")
        self.last_name = page.locator("#signupLastName")
        self.email = page.locator("#signupEmail")
        self.password = page.locator("#signupPassword")
        self.re_password = page.locator("#signupRepeatPassword")
        self.register_button = page.get_by_role("button", name="Register", exact=True)
        self.garage_title = page.get_by_role("heading", name="Garage")

    @allure.step("Fill name")
    def fill_name(self, name):
        self.name.fill(name)

    @allure.step("Fill last name")
    def fill_last_name(self, last_name):
        self.last_name.fill(last_name)

    @allure.step("Fill email")
    def fill_email(self, email):
        self.email.fill(email)

    @allure.step("Fill password")
    def fill_password(self, password):
        self.password.fill(password)

    @allure.step("Fill repeat password")
    def fill_repeat_password(self, password):
        self.re_password.fill(password)

    @allure.step("Register user")
    def register_user(self, name, last_name, email, password):
        self.fill_name(name)
        self.fill_last_name(last_name)
        self.fill_email(email)
        self.fill_password(password)
        self.fill_repeat_password(password)
        self.register_button.click()

    @allure.step("Check successful registration")
    def check_registration(self):
        expect(self.garage_title).to_be_visible()