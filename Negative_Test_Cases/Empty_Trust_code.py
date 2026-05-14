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

        # Fill Email
        email = page.get_by_role(
            "textbox",
            name="college.admin@jozuna.com"
        )

        email.click()
        email.fill("Kalpana@yopmail.com")

        # Fill Password
        password = page.get_by_role(
            "textbox",
            name="Enter password"
        )

        password.click()
        password.fill("Kal@2026")

        # Click Stay Logged In checkbox
        page.locator("//input[@id='stayLoggedIn']").click()

        # Wait for Login button enabled
        login_button = page.get_by_role(
            "button",
            name="Login"
        )

        expect(login_button).to_be_enabled(timeout=10000)

        # Click Login
        login_button.click()

        # Click Create Trust
        page.get_by_role(
            "button",
            name="Create Trust"
        ).click()

        # Leave Trust Code Empty

        # Enter Trust Name
        page.get_by_role(
            "textbox",
            name="Enter Trust Name"
        ).fill("Rama Trust")

        # Upload Image
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

        # Validate Trust Code required message
        expect(
            page.get_by_text("Trust Code is required")
        ).to_be_visible()

        print("SUCCESS : Trust Code required validation displayed correctly")



        # Close browser
        context.close()

        browser.close()

    except Exception as e:

        print("FAILURE : Trust Code validation failed")
        print("ERROR :", e)


with sync_playwright() as playwright:
    run(playwright)