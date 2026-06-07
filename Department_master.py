import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://polite-kleicha-37f855.netlify.app/")
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
    Department_Associate_span = page.locator(
        "//a[contains(@class,'cm-menu-item') and contains(@class,'cm-active')]//*[name()='svg']"
    ).first

    Department_Associate_span.click()

    page.get_by_role("link", name="Department Master").click()
    page.get_by_role("button", name="Create Department").click()
    page.get_by_role("textbox", name="Enter Department Code").click()
    page.get_by_role("textbox", name="Enter Department Code").fill("")
    page.get_by_role("textbox", name="Enter Department Code").press("CapsLock")
    page.get_by_role("textbox", name="Enter Department Code").fill("FA9S")
    page.get_by_role("textbox", name="Enter Department Name").click()
    page.get_by_role("textbox", name="Enter Department Name").fill("FkHO09N")
    page.get_by_role("textbox", name="Enter Department Number").click()
    page.get_by_role("textbox", name="Enter Department Number").fill("0200")

    # Saving and handling popups
    page.get_by_role("button", name="Save").click()
    page.get_by_role("button", name="Yes").click()
    page.get_by_role("button", name="Ok").click()
    page.locator("//input[@placeholder='Search Departments...']").fill(
        "FASHION DESIGNING"
    )
    page.locator("//input[@placeholder='Search Departments...']").clear()
    page.locator("//span[contains(@class,'common-dropdown-text')]").click()
    page.locator("//div[normalize-space()='Not Associated']").click()

    # Click Edit Department
    page.locator("//button[@title='Edit Department']").first.click()

    # Update Department Code
    dept_code = page.locator("//input[@placeholder='Enter Department Code']")
    dept_code.wait_for(state="visible")
    dept_code.fill("CoFSA")

    # Click Update
    page.locator("//button[normalize-space()='Update']").click()

    # Confirmation popup

    page.locator("button:has-text('Yes')").wait_for(timeout=20000)
    page.locator("button:has-text('Yes')").click()
    ok_btn = page.locator("button:has-text('OK')")
    ok_btn.wait_for(state="visible", timeout=20000)
    ok_btn.click()
    page.locator(
        "//div[@class='table-card scroll-mode']//div[1]//div[4]//div[1]//label[1]//span[1]"
    ).click()
    page.locator("button:has-text('Yes')").wait_for(timeout=2000)
    page.locator("button:has-text('Yes')").click()
    page.locator("button:has-text('OK')").click()
    page.locator(
        "//div[contains(@class,'table-card scroll-mode')]//div[1]//div[6]//div[1]//button[2]//*[name()='svg']"
    ).click()

    page.locator("button:has-text('Yes')").click(force=True)
    page.get_by_role("button", name="OK").click()

    # FIX: Wait for the underlying table DOM state to stabilize after closing the popup modal
    page.wait_for_load_state("domcontentloaded")



    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)