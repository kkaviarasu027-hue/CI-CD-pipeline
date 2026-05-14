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

        # Leave all fields empty

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

        print("SUCCESS : Empty field validation messages displayed correctly")



        # Close browser
        context.close()
        browser.close()

    except Exception as e:

        print("FAILURE : Empty field validation failed")
        print("ERROR :", e)


with sync_playwright() as playwright:
    run(playwright)