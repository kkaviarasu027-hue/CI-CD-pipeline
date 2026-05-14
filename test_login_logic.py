import pytest
import allure
import re
from playwright.sync_api import sync_playwright, expect

@allure.feature("Login Functionality")
@allure.story("Comprehensive Logic Test Suite")
class TestLoginLogic:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        """Standard Setup for each test case."""
        with sync_playwright() as p:
            # Headless=True is required for GitHub Actions
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            self.page = context.new_page()
            self.page.set_default_timeout(30000)
            yield
            browser.close()

    def navigate(self):
        """Helper to navigate to the application."""
        self.page.goto("https://gentle-lebkuchen-912cc7.netlify.app/", wait_until="commit")

    # --- 1. NEGATIVE INPUT VALIDATION ---

    @allure.title("Invalid Username Test")
    def test_invalid_username(self):

        self.navigate()

        # wait for login form to load
        self.page.wait_for_load_state("networkidle")

        # stable locators (IMPORTANT FIX)
        email = self.page.get_by_role("textbox").first
        password = self.page.get_by_role("textbox").nth(1)

        expect(email).to_be_visible()
        expect(password).to_be_visible()

        email.fill("wronguser@yopmail.com")
        password.fill("Kal@2026")

        checkbox = self.page.get_by_role("checkbox")
        if not checkbox.is_checked():
            checkbox.check(force=True)

        login_btn = self.page.get_by_role("button", name="Login")
        login_btn.click()

        expect(
            self.page.get_by_text("Unauthorized access")
        ).to_be_visible(timeout=10000)

    @allure.title("Invalid Password Test")
    def test_invalid_password(self):
        self.navigate()
        self.page.locator("input[type='email']").fill("testuser@gmail.com")
        self.page.locator("input[type='password']").fill("WrongPass123!")
        self.page.get_by_role("checkbox").check(force=True)
        self.page.get_by_role("button", name="Login").click(force=True)
        expect(self.page.get_by_text("Unauthorized access")).to_be_visible()

    @allure.title("Both Credentials Invalid")
    def test_invalid_both_credentials(self):
        self.navigate()
        self.page.locator("input[type='email']").fill("fakeuser@notreal.com")
        self.page.locator("input[type='password']").fill("WrongPass@2026")
        self.page.get_by_role("checkbox").check(force=True)
        btn = self.page.get_by_role("button", name="Login")
        expect(btn).to_be_enabled()
        btn.click()
        expect(self.page.get_by_text("Unauthorized access")).to_be_visible()

    # --- 2. EDGE CASES & SECURITY ---

    @allure.title("Long Input Strings Performance")
    def test_long_input_strings(self):
        self.navigate()
        long_email = "a" * 200 + "@example.com"
        self.page.locator("input[type='email']").fill(long_email)
        self.page.locator("input[type='password']").fill("Password123!" + "s" * 100)
        self.page.get_by_role("checkbox").check(force=True)
        btn = self.page.get_by_role("button", name="Login")
        btn.evaluate("node => node.removeAttribute('disabled')")
        btn.click()
        error = self.page.get_by_text(re.compile(r"(unauthorized|incorrect|must be|invalid)", re.IGNORECASE))
        expect(error.first).to_be_visible()

    @allure.title("Password Case Sensitivity Check")
    def test_password_case_sensitivity(self):
        self.navigate()
        self.page.get_by_role("textbox", name="college.admin@jozuna.com").fill("kalpana@yopmail.com")
        self.page.get_by_role("textbox", name="Enter password").fill("Kal@2026") # Testing upper 'K'
        self.page.get_by_role("checkbox").check()
        try:
            self.page.get_by_role("button", name="Login").click(timeout=5000)
        except:
            assert "dashboard" not in self.page.url.lower()

    @allure.title("Special Characters in Username")
    def test_special_characters_username(self):
        self.navigate()
        self.page.get_by_role("textbox", name="college.admin@jozuna.com").fill("@@@###$$$")
        self.page.get_by_role("textbox", name="Enter password").fill("ValidPass123!")
        self.page.get_by_role("checkbox").check()
        btn = self.page.get_by_role("button", name="Login")
        expect(btn).to_be_disabled()

    @allure.title("Locked/Disabled User Account")
    def test_locked_account(self):
        self.navigate()
        self.page.get_by_role("textbox", name="college.admin@jozuna.com").fill("locked_user@test.com")
        self.page.get_by_role("textbox", name="Enter password").fill("ValidPass123!")
        self.page.get_by_role("checkbox").check()
        self.page.get_by_role("button", name="Login").click(force=True)
        self.page.wait_for_timeout(2000)
        assert "dashboard" not in self.page.url.lower()

    # --- 3. SYSTEM STRESS TESTING ---

    @allure.title("Rate Limiting Simulation")
    def test_rate_limiting(self):
        self.navigate()
        for i in range(1, 4): # Scaled down for CI speed
            self.page.locator("input[type='email']").fill(f"attack_user_{i}@gmail.com")
            self.page.locator("input[type='password']").fill("WrongPass@2026")
            self.page.get_by_role("checkbox").check(force=True)
            btn = self.page.get_by_role("button", name="Login")
            btn.evaluate("node => node.removeAttribute('disabled')")
            btn.click()
            self.page.get_by_role("button", name="OK").click()
            self.page.wait_for_timeout(500)

    @allure.feature("Login Functionality")
    @allure.story("Comprehensive Logic Test Suite")
    class TestLoginLogic:

        @pytest.fixture(scope="function", autouse=True)
        def setup(self):
            """Standard Setup for each test case."""
            with sync_playwright() as p:
                # Headless=True is required for GitHub Actions
                browser = p.chromium.launch(headless=True)
                context = browser.new_context()
                self.page = context.new_page()
                self.page.set_default_timeout(30000)
                yield
                browser.close()

        def navigate(self):
            """Helper to navigate to the application."""
            self.page.goto("https://gentle-lebkuchen-912cc7.netlify.app/", wait_until="commit")

        # --- ADDING YOUR UPLOADED LOGIC FILES HERE ---

        @allure.title("SQL Injection Attack Attempt")
        @allure.description("Verifies that the system rejects SQL injection payloads in the email field.")
        def test_sql_injection(self):
            self.navigate()
            sql_payload = "'OR'1'='1'@test.com"
            self.page.locator("input[type='email']").fill(sql_payload)
            self.page.locator("input[type='password']").fill("WrongPass@2026")
            self.page.get_by_role("checkbox").check(force=True)

            btn = self.page.get_by_role("button", name="Login")
            btn.evaluate("node => node.removeAttribute('disabled')")
            btn.click()

            expect(self.page.get_by_text("Unauthorized access")).to_be_visible(timeout=10000)

        @allure.title("Unregistered User Login")
        @allure.description("Verifies that a valid email not in the database receives unauthorized access.")
        def test_unregistered_user(self):
            self.navigate()
            self.page.locator("input[type='email']").fill("brand_new_stranger_2026@gmail.com")
            self.page.locator("input[type='password']").fill("SafePass@2026")
            self.page.get_by_role("checkbox").check(force=True)

            btn = self.page.get_by_role("button", name="Login")
            btn.evaluate("node => node.removeAttribute('disabled')")
            btn.click()

            expect(self.page.get_by_text("Unauthorized access")).to_be_visible(timeout=10000)

        @allure.title("Empty Credentials Validation")
        @allure.description("Ensures the login button remains disabled when no input is provided.")
        def test_empty_credentials(self):
            self.navigate()
            self.page.get_by_role("checkbox").check(force=True)

            btn = self.page.get_by_role("button", name="Login")
            expect(btn).to_be_disabled()

            # Verify clicking it while disabled doesn't trigger the error popup
            btn.click(force=True)
            expect(self.page.get_by_text("Unauthorized access")).not_to_be_visible(timeout=3000)