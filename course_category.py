import asyncio
import re
from playwright.async_api import async_playwright, Playwright, expect


# --- HELPER FUNCTION TO HANDLE CONFIRMATION MODALS RESILIENTLY ---
async def handle_popup(page, action_button_name: str):

    btn = page.get_by_role("button", name=action_button_name, exact=False)
    await btn.wait_for(state="visible", timeout=7000)
    await btn.click()


# --- FLOW 1: COURSE CATEGORY & COURSE REGISTRATION ---
async def create_course_flow(playwright: Playwright) -> None:
    print("Starting Flow 1: Course and Category Registration...")
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()

    await page.goto("https://polite-kleicha-37f855.netlify.app/")

    # Login Authentication
    await page.get_by_role("textbox", name="college.admin@jozuna.com").fill("kalpana@yopmail.com")
    await page.get_by_role("textbox", name="Enter password").fill("Kal@2026")
    await page.get_by_role("checkbox", name="Stay logged in on this device").check()
    await page.get_by_role("button", name="Login").click()

    # Wait for post-login dashboard network calls to stabilize
    await page.wait_for_load_state("networkidle")

    # FIX: Open the Course Category menu utilizing the raw SVG node element
    print("Opening the Course Category menu using the SVG element...")
    course_category_svg = page.locator("//a[@class='cm-menu-item cm-active']//*[name()='svg']").first
    await course_category_svg.click()
    print("Successfully opened the layout via SVG element interaction!")
    print("Navigating to Course section via text span tracking...")
    course_master_span = page.locator("//span[normalize-space()='Course Category']").first
    await course_master_span.wait_for(state="visible", timeout=10000)
    await course_master_span.click()

    # Create New Category Form
    await page.get_by_role("button", name="New Category").click()
    await page.get_by_role("textbox", name="Enter Category Code").fill("C4ERd")
    await page.get_by_role("textbox", name="Enter Category Name").fill("ERP")
    await page.get_by_text("Yes").click()
    await page.get_by_role("radio", name="No").check()

    # Save & handle confirmation popup
    await page.get_by_role("button", name="Save").click()
    await handle_popup(page, "Yes")
    await page.get_by_role("button", name="OK").click()
    await page.locator("//input[@placeholder='Search Category...']").fill("Engineering")
    await page.locator("//input[@placeholder='Search Category...']").clear()
    # Open dropdown
    await page.locator("//div[@class='dropdown-header']").click()

    await page.locator("//div[normalize-space()='School']").click()

    await page.locator("//input[@placeholder='Search Category...']").fill("ERP")
    await page.locator("//input[@placeholder='Search Category...']").clear()
    await page.locator("//div[@class='dropdown-header']").click()
    await page.locator("//div[@class='dropdown-item selected']").click()
   

async def main():
    async with async_playwright() as playwright:
        await create_course_flow(playwright)

if __name__ == "__main__":
    asyncio.run(main())



