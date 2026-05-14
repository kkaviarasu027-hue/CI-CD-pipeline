import pytest
import allure
from playwright.sync_api import sync_playwright, expect


@allure.feature("Trust Master")
@allure.story("Comprehensive Negative Validation Test Suite")
class TestTrustMaster:

    # ---------------- SETUP ----------------
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):

        with sync_playwright() as p:

            self.browser = p.chromium.launch(headless=False)

            self.context = self.browser.new_context()

            self.page = self.context.new_page()

            self.page.set_default_timeout(30000)

            yield

            self.context.close()

            self.browser.close()

    # ---------------- LOGIN FUNCTION ----------------
    def login(self):

        self.page.goto(
            "https://tranquil-truffle-2a8000.netlify.app/"
        )

        self.page.get_by_role(
            "textbox",
            name="college.admin@jozuna.com"
        ).fill("Kalpana@yopmail.com")

        self.page.get_by_role(
            "textbox",
            name="Enter password"
        ).fill("Kal@2026")

        self.page.get_by_role(
            "checkbox",
            name="Stay logged in on this device"
        ).check(force=True)

        self.page.get_by_role(
            "button",
            name="Login"
        ).click()

    # ---------------- OPEN CREATE TRUST ----------------
    def open_create_trust(self):

        self.page.get_by_role(
            "button",
            name="Create Trust"
        ).click()

    # ---------------- UPLOAD FILE ----------------
    def upload_valid_file(self):

        self.page.locator(
            "input[type='file']"
        ).set_input_files(
            r"C:\Users\kaviy\Downloads\magnific_trust-handwritten-script-_2923083947.png"
        )

    # =========================================================
    # 1. EMPTY TRUST CODE
    # =========================================================
    @allure.title("Empty Trust Code Validation")
    def test_empty_trust_code(self):

        self.login()

        self.open_create_trust()

        self.page.get_by_role(
            "textbox",
            name="Enter Trust Name"
        ).fill("Rama Trust")

        self.upload_valid_file()

        self.page.get_by_role(
            "button",
            name="Save"
        ).click()

        expect(
            self.page.get_by_text("Trust Code is required")
        ).to_be_visible()

    # =========================================================
    # 2. EMPTY TRUST NAME
    # =========================================================
    @allure.title("Empty Trust Name Validation")
    def test_empty_trust_name(self):

        self.login()

        self.open_create_trust()

        self.page.get_by_role(
            "textbox",
            name="Enter Trust Code"
        ).fill("TR001")

        self.upload_valid_file()

        self.page.get_by_role(
            "button",
            name="Save"
        ).click()

        expect(
            self.page.get_by_text("Trust Name is required")
        ).to_be_visible()

    # =========================================================
    # 3. DUPLICATE TRUST CODE
    # =========================================================
    @allure.title("Duplicate Trust Code Validation")
    def test_duplicate_trust_code(self):

        self.login()

        self.open_create_trust()

        self.page.get_by_role(
            "textbox",
            name="Enter Trust Code"
        ).fill("001")

        self.page.get_by_role(
            "textbox",
            name="Enter Trust Name"
        ).fill("Duplicate Trust")

        self.upload_valid_file()

        self.page.get_by_role(
            "button",
            name="Save"
        ).click()

    # =========================================================
    # 4. EMPTY ALL FIELDS
    # =========================================================
    @allure.title("Empty All Fields Validation")
    def test_empty_all_fields(self):

        self.login()

        self.open_create_trust()

        self.page.get_by_role(
            "button",
            name="Save"
        ).click()

        expect(
            self.page.get_by_text("Trust Code is required")
        ).to_be_visible()

        expect(
            self.page.get_by_text("Trust Name is required")
        ).to_be_visible()

    # =========================================================
    # 5. INVALID TRUST CODE
    # =========================================================
    @allure.title("Invalid Trust Code Validation")
    def test_invalid_trust_code(self):

        self.login()

        self.open_create_trust()

        self.page.get_by_role(
            "textbox",
            name="Enter Trust Code"
        ).fill("@@@###")

        self.page.get_by_role(
            "textbox",
            name="Enter Trust Name"
        ).fill("Special Trust")

        self.upload_valid_file()

        self.page.get_by_role(
            "button",
            name="Save"
        ).click()

    # =========================================================
    # 6. NUMERIC TRUST NAME
    # =========================================================
    @allure.title("Numeric Trust Name Validation")
    def test_numeric_trust_name(self):

        self.login()

        self.open_create_trust()

        self.page.get_by_role(
            "textbox",
            name="Enter Trust Code"
        ).fill("TR123")

        self.page.get_by_role(
            "textbox",
            name="Enter Trust Name"
        ).fill("123456")

        self.upload_valid_file()

        self.page.get_by_role(
            "button",
            name="Save"
        ).click()

    # =========================================================
    # 7. SPACE ONLY VALIDATION
    # =========================================================
    @allure.title("Space Only Validation")
    def test_space_only_validation(self):

        self.login()

        self.open_create_trust()

        self.page.get_by_role(
            "textbox",
            name="Enter Trust Code"
        ).fill("     ")

        self.page.get_by_role(
            "textbox",
            name="Enter Trust Name"
        ).fill("     ")

        self.upload_valid_file()

        self.page.get_by_role(
            "button",
            name="Save"
        ).click()

    # =========================================================
    # 8. SQL INJECTION
    # =========================================================
    @allure.title("SQL Injection Validation")
    def test_sql_injection(self):

        self.login()

        self.open_create_trust()

        self.page.get_by_role(
            "textbox",
            name="Enter Trust Code"
        ).fill("TR128")

        self.page.get_by_role(
            "textbox",
            name="Enter Trust Name"
        ).fill("' OR '1'='1")

        self.upload_valid_file()

        self.page.get_by_role(
            "button",
            name="Save"
        ).click()

    # =========================================================
    # 9. UNSUPPORTED FILE
    # =========================================================
    @allure.title("Unsupported File Upload")
    def test_unsupported_file(self):

        self.login()

        self.open_create_trust()

        self.page.get_by_role(
            "textbox",
            name="Enter Trust Code"
        ).fill("TR126")

        self.page.get_by_role(
            "textbox",
            name="Enter Trust Name"
        ).fill("Unsupported File Trust")

        self.page.locator(
            "input[type='file']"
        ).set_input_files(
            r"C:\Users\kaviy\Videos\Screen Recordings\Screen Recording 2026-04-25 202706.mp4"
        )

        self.page.get_by_role(
            "button",
            name="Save"
        ).click()

    # =========================================================
    # 10. LARGE FILE
    # =========================================================
    @allure.title("Large File Upload")
    def test_large_file(self):

        self.login()

        self.open_create_trust()

        self.page.get_by_role(
            "textbox",
            name="Enter Trust Code"
        ).fill("TR127")

        self.page.get_by_role(
            "textbox",
            name="Enter Trust Name"
        ).fill("Large File Trust")

        self.page.locator(
            "input[type='file']"
        ).set_input_files(
            r"C:\Users\kaviy\Videos\Screen Recordings\Screen Recording 2026-04-25 202706.mp4"
        )

        self.page.get_by_role(
            "button",
            name="Save"
        ).click()

    # =========================================================
    # 11. LONG TRUST NAME
    # =========================================================
    @allure.title("Long Trust Name Validation")
    def test_long_trust_name(self):

        self.login()

        self.open_create_trust()

        long_name = "RamaTrust" * 50

        self.page.get_by_role(
            "textbox",
            name="Enter Trust Code"
        ).fill("TR125")

        self.page.get_by_role(
            "textbox",
            name="Enter Trust Name"
        ).fill(long_name)

        self.upload_valid_file()

        self.page.get_by_role(
            "button",
            name="Save"
        ).click()

    # =========================================================
    # 12. XSS PAYLOAD
    # =========================================================
    @allure.title("XSS Payload Validation")
    def test_xss_payload(self):

        self.login()

        self.open_create_trust()

        self.page.get_by_role(
            "textbox",
            name="Enter Trust Code"
        ).fill("TR129")

        self.page.get_by_role(
            "textbox",
            name="Enter Trust Name"
        ).fill("<script>alert('XSS')</script>")

        self.upload_valid_file()

        self.page.get_by_role(
            "button",
            name="Save"
        ).click()