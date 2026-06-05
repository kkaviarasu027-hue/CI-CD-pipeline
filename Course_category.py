import asyncio
import re
from playwright.async_api import async_playwright, Playwright, expect


# --- HELPER FUNCTION TO HANDLE CONFIRMATION MODALS RESILIENTLY ---
async def handle_popup(page, action_button_name: str):
    """
    Waits for a popup/alert button to become visible on screen
    using case-insensitive matching, preventing sudden TimeoutErrors.
    """
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
    await course_category_svg.wait_for(state="visible", timeout=10000)
    await course_category_svg.click()
    print("Successfully opened the layout via SVG element interaction!")
    print("Navigating to Course section via text span tracking...")
    course_master_span = page.locator("//span[normalize-space()='Course Category']").first
    await course_master_span.wait_for(state="visible", timeout=10000)
    await course_master_span.click()

    # Create New Category Form
    await page.get_by_role("button", name="New Category").click()
    await page.get_by_role("textbox", name="Enter Category Code").fill("C89")
    await page.get_by_role("textbox", name="Enter Category Name").fill("FASHION DESIGN")
    await page.get_by_text("Yes").click()
    await page.get_by_role("radio", name="No").check()

    # Save & handle confirmation popup
    await page.get_by_role("button", name="Save").click()
    await handle_popup(page, "Yes")
    await page.get_by_role("button", name="OK").click()
    await page.locator("//button[@class='course-master-back-btn']").click()
    # Wait for modal backdrop to fade out completely
    print("Waiting for save animation to clear...")
    await page.wait_for_timeout(1500)

    # Open the Course Master layout using its respective SVG structure
    print("Navigating to Course section via text span tracking...")
    # Navigate to Course menu
    course_tab = page.locator("//button[normalize-space()='Course']")

    await course_tab.wait_for(state="visible")
    await course_tab.click(force=True)

    # Create Course Form
    await page.get_by_role("button", name="New Course").click()

    await page.locator("div").filter(
        has_text=re.compile(r"^Select Category$")
    ).nth(1).click()

    await page.get_by_text("FASHION DESIGNING").click()

    # Inputs
    await page.get_by_role(
        "textbox",
        name="Enter Course Code"
    ).fill("22FAD01")

    await page.get_by_role(
        "textbox",
        name="Enter Course Name"
    ).fill("FASHION MERCHANDISING")

    await page.get_by_role(
        "textbox",
        name="e.g. 1",
        exact=True
    ).fill("56")

    await page.get_by_role(
        "textbox",
        name="e.g. 3"
    ).fill("3")

    await page.get_by_role(
        "textbox",
        name="e.g. 18"
    ).fill("19")

    # Save
    await page.get_by_role("button", name="Save").click()

    await handle_popup(page, "Yes")

    # Verification
    await page.get_by_text("All Categories").click()

    await page.get_by_role(
        "textbox",
        name="Search Course..."
    ).fill("FAS")

    await page.wait_for_timeout(2000)

    await context.close()
    await browser.close()
    print("Flow 1 Completed successfully.")


# --- FLOW 2: DATA MODIFICATION & TABLE UPDATE ---
async def edit_category_flow(playwright: Playwright) -> None:
    print("\nStarting Flow 2: Existing Record Modification...")
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()

    await page.goto("https://brilliant-choux-3ddb91.netlify.app/ ")

    # Login Authentication
    await page.get_by_role("textbox", name="college.admin@jozuna.com").fill("kalpana@yopmail.com")
    await page.get_by_role("textbox", name="Enter password").fill("Kal@2026")
    await page.get_by_role("checkbox", name="Stay logged in on this device").check()
    await page.get_by_role("button", name="Login").click()

    await page.wait_for_load_state("networkidle")

    # FIX: Open the Course Category menu using the exact same SVG node element structure here too
    print("Opening the Course Category menu using the SVG element...")
    course_category_svg = page.locator("//a[contains(@class, 'cm-menu-item')]//*[name()='svg']").first
    await course_category_svg.wait_for(state="visible", timeout=10000)
    await course_category_svg.click()

    # Inline row action targeting row 6
    await page.locator("div:nth-child(6) > div:nth-child(3) > .actions > span > .action-btn").click()
    await handle_popup(page, "Yes")

    # Select specific edit instance index 4
    await page.get_by_role("button", name="Edit").nth(4).click()

    # Wipe data input and override with new record value
    category_name_field = page.get_by_role("textbox", name="Enter Category Name")
    await category_name_field.fill("EDUCATION OF LAW ")

    # Commit modifications past security alert dialogues
    await page.get_by_role("button", name="Update").click()
    await handle_popup(page, "Yes")
    await page.wait_for_timeout(2000)

    await context.close()
    await browser.close()
    print("Flow 2 Completed successfully.")


# --- MAIN ENGINE RUNNER ---
async def main():
    async with async_playwright() as playwright:
        await create_course_flow(playwright)
        await edit_category_flow(playwright)


if __name__ == "__main__":
    try:
        loop = asyncio.get_running_loop()
        loop.create_task(main())
    except RuntimeError:
        asyncio.run(main())