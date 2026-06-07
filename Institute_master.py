import asyncio
from playwright.async_api import async_playwright, Playwright, TimeoutError


async def run(playwright: Playwright) -> None:
    # Launch the browser
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()

    try:
        print("Navigating to login page...")
        response = await page.goto(
            "https://polite-kleicha-37f855.netlify.app/",
            wait_until="domcontentloaded",
            timeout=10000
        )

        if response:
            print(f"Page loaded with Status: {response.status}")

        print(f"Title: {await page.title()}")
        print(f"URL: {page.url}")

        # --- Login Flow ---
        print("Filling login credentials...")
        await page.get_by_role(
            "textbox",
            name="college.admin@jozuna.com"
        ).fill("kalpana@yopmail.com")

        await page.get_by_role(
            "textbox",
            name="Enter password"
        ).fill("Kal@2026")

        await page.get_by_role(
            "checkbox",
            name="Stay logged in on this device"
        ).check()

        print("Clicking login button...")
        await page.get_by_role("button", name="Login").click()

        # Wait for the dashboard to completely load before continuing
        print("Waiting for dashboard redirect...")
        await page.wait_for_url("**/dashboard/**", timeout=10000)

        # --- Dashboard Navigation ---
        print("Navigating to Institute Master...")
        # Note: Your previous code had both the href click and text click.
        # Usually, just clicking the sidebar link item itself is enough:
        await page.locator("a[href='/dashboard/institute-master']").click()

        # --- Action ---
        print("Clicking 'Create Institute' button...")
        await page.get_by_role("button", name="Create Institute", exact=True).click()

        print("Successfully opened the Create Institute modal/page!")

        await page.locator(".common-dropdown-full.dropdown-down button[type='button']").click()
        await page.get_by_text("XYZ Educational Trust", exact=True).click()
        await page.wait_for_timeout(4000)
        await page.get_by_placeholder("Enter code", exact=False).fill("5677")
        await page.get_by_placeholder("Enter short name").fill("AU")
        await page.get_by_placeholder("Enter institution name").fill("anna university")
        await page.get_by_placeholder("Enter start roll number").fill("001")
        await page.wait_for_timeout(5000)
        print("Setting radio button option to 'No'...")
        await page.get_by_label("No", exact=True).check()
        print("Entering telephone number...")
        await page.get_by_placeholder("Enter telephone").fill("4364657588")
        print("Entering address...")
        address_text = """Anna University Campus,
        Sardar Patel Road, Guindy,
        Chennai, Tamil Nadu - 600025"""

        await page.get_by_placeholder("Enter address").fill(address_text)
        print("Opening State dropdown...")
        # 1. Target the dropdown button component safely without strict mode conflicts
        await page.locator("span.common-dropdown-text", has_text="Select state").click()

        print("Selecting 'Tamil Nadu' from the list...")
        # 2. Click the 'Tamil Nadu' option once the dropdown opens
        await page.get_by_text("Tamil Nadu", exact=True).click()
        print("Entering pincode...")
        print("Entering city...")
        await page.get_by_placeholder("Enter city", exact=False).fill("Chennai")
        await page.get_by_placeholder("Enter pincode").fill("600025")
        # --- Submission Flow ---
        print("Clicking the Save button...")
        await page.get_by_role("button", name="Save", exact=True).click()

        print("Waiting for confirmation popup and clicking 'Yes'...")
        try:
            # Try targeting it as an interactive button first
            await page.get_by_role("button", name="Yes", exact=True).click(timeout=3000)
        except Exception:
            # Fallback if "Yes" is a custom styled text element
            await page.get_by_text("Yes", exact=True).click()

        print("Clicking OK...")
        await page.get_by_role("button", name="Ok", exact=True).click()

        print("Successfully created the new Institute entry!")
        print("Searching for Anna University...")
        search_input = page.get_by_placeholder("Search institutions...")
        await search_input.fill("Anna University")
        await search_input.press("Enter")
        await page.wait_for_timeout(1000)
        await page.get_by_placeholder("Search institutions...").clear()
        await page.wait_for_timeout(5000)
        print("Targeting the action button in the first row...")

        # 1. Target the first data row inside your table body
        first_row = page.locator(".table-body > div").first

        # 2. Target the action button inside that specific row and click it
        # (Filtering by the button role or class to find it inside the row)
        await first_row.get_by_role("button").first.click()
        await page.wait_for_timeout(1000)
        address_text = """Anna University Campus,
                Sardar Patel Road, Guindy,
                Chennai, Tamil Nadu - 600025"""

        await page.get_by_placeholder("Enter address").fill(address_text)
        print("Clicking the Update button...")
        await page.get_by_role("button", name="Update", exact=True).click()
        print("Waiting for confirmation popup and clicking 'Yes'...")

        try:
            # Try targeting it as an interactive button first
            await page.get_by_role("button", name="Yes", exact=True).click(timeout=3000)
        except Exception:
            # Fallback if "Yes" is a custom styled text element
            await page.get_by_text("Yes", exact=True).click()

        print("Clicking OK...")
        await page.get_by_role("button", name="Ok", exact=True).click()
        print("Successfully created the new Institute entry!")
        # Open the trust dropdown
        await page.locator("//span[normalize-space()='All Trusts']").click()

        # Select the trust
        await page.locator("//div[normalize-space()='XYZ Educational Trust']").click()
        # Click the SVG button
        # Click the checkbox/toggle
        await page.locator(
            "//div[contains(@class,'table-card scroll-mode')]//div[1]//div[5]//div[1]//label[1]//span[1]"
        ).click()

        # Click Yes in the confirmation popup
        await page.get_by_role("button", name="Yes").click()
        await page.get_by_role("button", name="OK").click()
        await page.locator(
            "//div[@class='table-card scroll-mode']//div[1]//div[6]//div[1]//span[1]//button[1]//*[name()='svg']"
        ).click()

        # Click Yes
        await page.get_by_role("button", name="Yes").click()

        # Click OK
        await page.get_by_role("button", name="OK").click()

    except TimeoutError:
        print("Error: One of the elements or page loads timed out.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Ensures your terminal doesn't hang and resources are freed up
        print("Closing browser context...")
        await context.close()
        await browser.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


if __name__ == "__main__":
    asyncio.run(main())