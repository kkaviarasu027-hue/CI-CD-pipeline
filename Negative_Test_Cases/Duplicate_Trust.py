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

        # Enter Existing Trust Code
        page.get_by_role(
            "textbox",
            name="Enter Trust Code"
        ).fill("TR001")

        # Enter Valid Trust Name
        page.get_by_role(
            "textbox",
            name="Enter Trust Name"
        ).fill("Duplicate Trust")

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

        # Wait for validation message
        page.wait_for_timeout(3000)

        print("SUCCESS : Duplicate Trust Code negative test executed successfully")

        # Close browser
        context.close()
        browser.close()

    except Exception as e:
        print("FAILURE : Test execution failed")
        print("ERROR :", e)


with sync_playwright() as playwright:
    run(playwright)