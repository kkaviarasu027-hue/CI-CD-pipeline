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

        # Enter Spaces in Trust Code
        page.get_by_role(
            "textbox",
            name="Enter Trust Code"
        ).fill("     ")

        # Enter Spaces in Trust Name
        page.get_by_role(
            "textbox",
            name="Enter Trust Name"
        ).fill("     ")

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

        # Validate required field messages
        expect(
            page.get_by_text("Trust Code is required")
        ).to_be_visible()

        expect(
            page.get_by_text("Trust Name is required")
        ).to_be_visible()

        print("SUCCESS : Space-only validation displayed correctly")

        # Pause for inspection
        page.pause()

        # Close browser
        context.close()

        browser.close()

    except Exception as e:

        print("FAILURE : Space-only validation failed")
        print("ERROR :", e)


with sync_playwright() as playwright:
    run(playwright)