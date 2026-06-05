import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://brilliant-choux-3ddb91.netlify.app/")
    page.get_by_role("textbox", name="college.admin@jozuna.com").click()
    page.get_by_role("textbox", name="college.admin@jozuna.com").fill("kalpana@yopmail.com")
    page.get_by_role("textbox", name="Enter password").click()
    page.get_by_role("textbox", name="Enter password").fill("Kal@2026")
    page.locator("div").filter(has_text=re.compile(r"^Stay logged in on this device$")).click()
    page.get_by_role("checkbox", name="Stay logged in on this device").check()
    page.get_by_role("button", name="Login").click()

    print("Waiting for dashboard rendering...")
    page.wait_for_load_state("networkidle")

    # Dynamic SVG Selector to break through custom web layouts
    print("Locating menu item via target SVG icon node...")
    department_menu_svg = page.locator(
        "//a[@href='/dashboard/department-master']//*[name()='svg']"
    )

    department_menu_svg.wait_for(state="visible", timeout=10000)
    department_menu_svg.click(force=True)
    # Locate the Institute Master text span directly using custom XPath
    print("Locating menu item via explicit text span...")
    Department_Associate_span = page.locator("").first
    Department_Associate_span.wait_for(state="visible", timeout=10000)
    Department_Associate_span.click()

    page.get_by_role("link", name="Department Master").click()
    page.get_by_role("button", name="Create Department").click()
    page.get_by_role("textbox", name="Enter Department Code").click()
    page.get_by_role("textbox", name="Enter Department Code").fill("")
    page.get_by_role("textbox", name="Enter Department Code").press("CapsLock")
    page.get_by_role("textbox", name="Enter Department Code").fill("FADA")
    page.get_by_role("textbox", name="Enter Department Name").click()
    page.get_by_role("textbox", name="Enter Department Name").fill("FASHION DESIGNING")
    page.get_by_role("textbox", name="Enter Department Number").click()
    page.get_by_role("textbox", name="Enter Department Number").fill("200")

    # Saving and handling popups
    page.get_by_role("button", name="Save").click()
    page.get_by_role("button", name="Yes").click()
    page.get_by_role("button", name="Ok").click()

    # FIX: Wait for the underlying table DOM state to stabilize after closing the popup modal
    page.wait_for_load_state("domcontentloaded")



    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)