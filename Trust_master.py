import asyncio
from playwright.async_api import async_playwright, Playwright, expect


# --- HELPER FUNCTION TO HANDLE POPUPS RESILIENTLY ---
async def handle_popup(page, action_button_name: str):
    """
    Handles confirmation modals dynamically by waiting for visibility
    and using case-insensitive locator matching.
    """
    btn = page.get_by_role("button", name=action_button_name, exact=False)
    # Give the modal up to 7 seconds to animate/render on screen
    await btn.wait_for(state="visible", timeout=7000)
    await btn.click()


# --- FIRST AUTOMATION FLOW: CREATE TRUST ---
async def run_create_trust(playwright: Playwright) -> None:
    print("Starting Trust Creation Flow...")
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()

    await page.goto("https://polite-kleicha-37f855.netlify.app/")

    # Login
    await page.get_by_role("checkbox", name="Stay logged in on this device").check()
    await page.get_by_role("textbox", name="college.admin@jozuna.com").fill("kalpana@yopmail.com")
    await page.get_by_role("textbox", name="Enter password").fill("Kal@2026")
    await page.get_by_role("button", name="Login").click()

    # Wait for the dashboard network requests to settle
    await page.wait_for_load_state("networkidle")

    # Create Trust
    await page.get_by_role("button", name="Create Trust").click()

    # Trust Code & Name
    await page.get_by_role("textbox", name="Enter Trust Code").fill("T08323201")
    await page.get_by_role("textbox", name="Enter Trust Name").fill("JOZUNA TRUST")

    # Upload Logo
    await page.locator("input[type='file']").set_input_files(r"C:\Users\kaviy\Documents\logo.jpg")

    # Save and confirm
    await page.get_by_role("button", name="Save").click()
    await handle_popup(page, "Yes")

    await page.wait_for_timeout(3000)
    await context.close()
    await browser.close()
    print("Trust Creation Flow Completed Successfully.")


# --- SECOND AUTOMATION FLOW: INSTITUTION MAPPING & MANAGING ---
async def run_manage_institutions(playwright: Playwright) -> None:
    print("\nStarting Institution Management Flow...")
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()

    await page.goto("https://brilliant-choux-3ddb91.netlify.app/")
    await page.get_by_role("textbox", name="college.admin@jozuna.com").fill("kalpana@yopmail.com")
    await page.get_by_role("textbox", name="Enter password").fill("Kal@2026")
    await page.get_by_role("checkbox", name="Stay logged in on this device").check()
    await page.get_by_role("button", name="Login").click()

    # Ensure page elements load completely post-login
    await page.wait_for_load_state("networkidle")

    await page.get_by_role("button", name="All Status arrow").click()
    await page.get_by_text("Mapped Institutions", exact=True).click()
    await page.get_by_role("button", name="Mapped Institutions arrow").click()
    await page.get_by_text("Unmapped Institutions").click()

    await page.get_by_role("textbox", name="Search Trusts...").fill("jozuna ")

    # 1st Update Sequence
    await page.get_by_role("button", name="Edit Trust").nth(1).click()
    await page.get_by_role("button", name="Update").click()
    await handle_popup(page, "Yes")
    await handle_popup(page, "Ok")  # Safe case-insensitive wait and click

    # Toggle Switch Sequence
    await page.locator(".table-cell > div > .toggle-switch > .toggle-slider").first.click()
    await handle_popup(page, "Yes")
    await handle_popup(page, "Ok")

    # 1st Delete Sequence
    await page.locator("div:nth-child(5) > div:nth-child(5) > div").click()
    await page.get_by_role("button", name="Delete Trust").nth(4).click()
    await handle_popup(page, "Yes")
    await handle_popup(page, "Ok")

    # 2nd Delete Sequence
    await page.get_by_role("button", name="Delete Trust").first.click()
    await handle_popup(page, "Yes")
    await handle_popup(page, "Ok")

    # Final Modification Action
    await page.locator("div:nth-child(7) > div:nth-child(5) > div > button:nth-child(2)").click()
    await handle_popup(page, "Yes")
    await handle_popup(page, "Ok")

    await context.close()
    await browser.close()
    print("Institution Management Flow Completed Successfully.")


# --- MAIN ASYNC EXECUTIVE BLOCK ---
async def main():
    async with async_playwright() as playwright:
        await run_create_trust(playwright)
        await run_manage_institutions(playwright)


if __name__ == "__main__":
    try:
        loop = asyncio.get_running_loop()
        loop.create_task(main())
    except RuntimeError:
        asyncio.run(main())