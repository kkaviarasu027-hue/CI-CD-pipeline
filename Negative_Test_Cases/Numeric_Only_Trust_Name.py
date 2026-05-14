from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:

    try:
        # Launch browser
        browser = playwright.chromium.launch(headless=False)

        # Create browser context
        context = browser.new_context()

        page = context.new_page()

        # Open Application
        page.goto("https://tranquil-truffle-2a8000.netlify.app/")

        # Login
        page.get_by_role(
            "textbox",
            name="college.admin@jozuna.com"
        ).fill("Kalpana@yopmail.com")

        page.get_by_role(
            "textbox",
            name="Enter password"
        ).fill("Kal@2026")

        page.locator(
            "//input[@id='stayLoggedIn']"
        ).click()

        page.get_by_role(
            "button",
            name="Login"
        ).click()

        # Click Create Trust
        page.get_by_role(
            "button",
            name="Create Trust"
        ).click()

        # Enter Valid Trust Code
        page.get_by_role(
            "textbox",
            name="Enter Trust Code"
        ).fill("TR123")

        # Enter Numeric Trust Name
        page.get_by_role(
            "textbox",
            name="Enter Trust Name"
        ).fill("123456")

        # Upload Valid Image
        page.locator(
            "input[type='file']"
        ).set_input_files(
            r"C:\Users\kaviy\Downloads\magnific_trust-handwritten-script-_2923083947.png"
        )

        # Click Save
        page.get_by_role(
            "button",
            name="Save"
        ).click()

        # Validate numeric trust name message
        expect(
            page.get_by_text("Trust Name should contain alphabets")
        ).to_be_visible()

        print("SUCCESS : Numeric Trust Name validation displayed correctly")


        context.close()

        browser.close()

    except Exception as e:

        print("FAILURE : Numeric Trust Name validation failed")
        print("ERROR :", e)


with sync_playwright() as playwright:
    run(playwright)