import asyncio
import re
from playwright.async_api import async_playwright, Playwright, expect


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

    await page.wait_for_load_state("networkidle")

    await page.locator(
        "//a[contains(@class,'cm-menu-item') and contains(@class,'cm-active')]//*[name()='svg']"
    ).first.click()

    await page.locator(
        "//span[normalize-space()='Department Associate']"
    ).click()

    await page.locator(
        "//input[@placeholder='Search mappings...']"
    ).fill("English")


    # Create Department Associate
    await page.locator(
        "//button[normalize-space()='Create Department Associate']"
    ).click()
    await page.locator(
        "//div[contains(@class,'dept-assoc-form-card')]//div[1]//div[2]//div[1]//div[1]"
    ).click()

    # Select Institution
    await page.locator(
        "//div[normalize-space()='Sree sowdambika college of engineering']"
    ).click()

    # Open Category dropdown
    await page.locator(
        "//span[normalize-space()='Select Category']"
    ).click()

    # Select Category
    await page.locator(
        "//div[normalize-space()='FASHION DESIGNER']"
    ).click()

    # Open Course dropdown
    await page.locator(
        "//span[normalize-space()='Select Course']"
    ).click()

    # Select Course
    await page.locator(
        "//div[normalize-space()='computer science and engineering']"
    ).click()

    # Select Department checkbox
    await page.locator(
        "//div[contains(@class,'dept-assoc-list-container')]//div[1]//label[1]"
    ).click()

    # 2. Wait for the confirmation popup modal to appear and click 'Save' inside it
    # (Using .last handles the modal button if multiple 'Save' elements exist on screen)
    save_popup_btn = page.get_by_role("button", name="Save", exact=True).last
    await save_popup_btn.wait_for(state="visible")
    await save_popup_btn.click()
    # Clicks the 'Save' button inside the confirmation popup using its specific classes
    await page.locator("//button[@class='alert-btn confirm']").click()

    # 3. Click the 'OK' button on the green success confirmation that follows
    ok_popup_btn = page.get_by_role("button", name="OK", exact=True)
    await ok_popup_btn.wait_for(state="visible")
    await ok_popup_btn.click()
    # 1. Open the dropdown menu
    # Change line 86 to this:
    await page.locator("//div[@class='dropdown-header']").first.click()

    # 2. Click "All Institutions" from the opened list
    # Change line 90 to this:
    await page.locator("div.dropdown-item").get_by_text("All Institutions", exact=True).click()
    # 1. Click the Edit button on the target row
    await page.locator("//button[@aria-label='Edit']").click()

    # Step 1: Open the dropdown selection box wrapper
    # (Replaces the fragile SVG path tracking entirely)
    await page.locator(".dropdown-header").first.click()

    # Step 2: Select the first available option row inside the dropdown wrapper
    # Change Line 100 to this:
    await page.locator(".dropdown-items-wrapper > div").first.click(force=True)

    # 1. Click 'Save' inside the creation card to trigger the popup
    await page.locator("//button[normalize-space()='Save']").click()

    # 2. Click the 'Save' confirm button inside the popup alert box
    confirm_popup_btn = page.locator("//button[@class='alert-btn confirm']")
    await confirm_popup_btn.wait_for(state="visible", timeout=3000)
    await confirm_popup_btn.click()

    # 3. Handle the final success popup by clicking 'OK'
    ok_btn = page.get_by_role("button", name="OK", exact=True)
    await ok_btn.wait_for(state="visible", timeout=3000)
    await ok_btn.click()
    # Clicks the action icon button using your explicit tree structure
    # Change line 116 to this:
    # 1. Target ONLY visible delete buttons on the current page layout
    delete_btn = page.locator("//button[@aria-label='Delete']").filter(has_not=page.locator("hidden")).first
    # Alternative native Playwright approach:
    # delete_btn = page.locator("button[aria-label='Delete'] >> visible=true").first

    # 2. Check if there are any VISIBLE records to clean up
    # We use is_visible() on the first match since count() can include hidden items
    if not await delete_btn.is_visible():
        print("\nℹ️  Skipping Cleanup: No visible records found in the data table.")
    else:
        print("Record found in table! Cleaning up test data...")
        await delete_btn.click()

        # Handle the confirmation popup modal
        confirm_btn = page.locator("//button[contains(@class, 'confirm') or normalize-space()='Delete']").last
        await confirm_btn.wait_for(state="visible", timeout=3000)
        await confirm_btn.click()

        # Clear the final success notification alert window
        ok_btn = page.get_by_role("button", name="OK", exact=True)
        await ok_btn.wait_for(state="visible", timeout=3000)
        await ok_btn.click()
        print("✅ Cleanup complete! Table row cleared cleanly.")

async def main():
    async with async_playwright() as playwright:
        await create_course_flow(playwright)


if __name__ == "__main__":
    asyncio.run(main())