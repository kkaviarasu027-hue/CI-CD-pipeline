from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:

    try:
        # Launch browser
        browser = playwright.chromium.launch(headless=False)

        # Create browser context
        context = browser.new_context()

        page = context.new_page()

        # Open application
        page.goto("https://tranquil-truffle-2a8000.netlify.app/")

        # Enter Email
        page.get_by_role(
            "textbox",
            name="college.admin@jozuna.com"
        ).fill("Kalpana@yopmail.com")

        # Enter Password
        page.get_by_role(
            "textbox",
            name="Enter password"
        ).fill("Kal@2026")

        # Click Stay Logged In checkbox
        page.locator(
            "//input[@id='stayLoggedIn']"
        ).click()

        # Click Login
        page.get_by_role(
            "button",
            name="Login"
        ).click()

        # Click Create Trust
        page.get_by_role(
            "button",
            name="Create Trust"
        ).click()

        # Enter valid Trust Code
        page.get_by_role(
            "textbox",
            name="Enter Trust Code"
        ).fill("TR001")

        # Leave Trust Name Empty

        # Upload valid image
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

        # Validate Trust Name required message
        expect(
            page.get_by_text("Trust Name is required")
        ).to_be_visible()

        print("SUCCESS : Trust Name required validation displayed correctly")


        context.close()

        browser.close()

    except Exception as e:

        print("FAILURE : Trust Name validation failed")
        print("ERROR :", e)


with sync_playwright() as playwright:
    run(playwright)