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
        ).fill("TR126")

        # Enter Valid Trust Name
        page.get_by_role(
            "textbox",
            name="Enter Trust Name"
        ).fill("Unsupported File Trust")

        # Upload Unsupported File
        page.locator(
            "input[type='file']"
        ).set_input_files(
            r"C:\Users\kaviy\Videos\Screen Recordings\Screen Recording 2026-04-25 202706.mp4"
        )

        # Click Save
        page.get_by_role(
            "button",
            name="Save"
        ).click()

        # Validate unsupported file message
        expect(
            page.get_by_text("Unsupported file format")
        ).to_be_visible()

        print("SUCCESS : Unsupported file validation displayed correctly")


        context.close()

        browser.close()

    except Exception as e:

        print("FAILURE : Unsupported file upload validation failed")
        print("ERROR :", e)


with sync_playwright() as playwright:
    run(playwright)