import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()

    # Open application
    page.goto("https://tranquil-truffle-2a8000.netlify.app/")

    # Email
    page.get_by_role("textbox", name="college.admin@jozuna.com").click()
    page.get_by_role("textbox", name="college.admin@jozuna.com").press("CapsLock")
    page.get_by_role("textbox", name="college.admin@jozuna.com").fill("K")
    page.get_by_role("textbox", name="college.admin@jozuna.com").press("CapsLock")
    page.get_by_role("textbox", name="college.admin@jozuna.com").fill("Kalpana@yopmail.com")

    # Password
    page.get_by_role("textbox", name="Enter password").click()
    page.get_by_role("textbox", name="Enter password").press("CapsLock")
    page.get_by_role("textbox", name="Enter password").fill("K")
    page.get_by_role("textbox", name="Enter password").press("CapsLock")
    page.get_by_role("textbox", name="Enter password").fill("Kal@2026")

    # Stay logged in
    page.get_by_text("Stay logged in on this device").click()

    # Login
    page.get_by_role("button", name="Login").click()



    # Create Trust
    page.get_by_role("button", name="Create Trust").click()

    # Enter Trust Code
    page.get_by_role("textbox", name="Enter Trust Code").click()
    page.get_by_role("textbox", name="Enter Trust Code").fill("3")

    # Enter Trust Name
    page.get_by_role("textbox", name="Enter Trust Name").click()
    page.get_by_role("textbox", name="Enter Trust Name").fill("rama")

    # Upload file
    page.locator("input[type='file']").set_input_files(
        r"C:\Users\kaviy\Downloads\magnific_trust-handwritten-script-_2923083947.png"
    )

    # Save
    page.get_by_role("button", name="Save").click()

    # Confirmation
    page.get_by_role("button", name="Yes").click()



    # Loader overlay click
    page.locator(".login-loader-overlay").click()

    # Success popup
    page.get_by_role("button", name="Ok").click()

    # Close browser
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)