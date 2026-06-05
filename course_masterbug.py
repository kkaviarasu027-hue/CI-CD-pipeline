import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    # Launch browser (Headless=False lets you watch the execution)
    browser = playwright.chromium.launch(headless=False)

    # 1. Initialize Browser Context with Video Recording Settings
    context = browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width": 1280, "height": 720}
    )

    # 2. Start Test Tracing Feature
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    try:
        # --- Login Flow ---
        page.goto("https://brilliant-choux-3ddb91.netlify.app/dashboard/trust-master")
        page.get_by_role("button", name="OK").click()
        page.get_by_role("textbox", name="college.admin@jozuna.com").fill("Kalpana@yopmail.com")
        page.get_by_role("textbox", name="Enter password").fill("Kal@2026")
        page.get_by_role("textbox", name="Enter password").press("Enter")
        page.get_by_text("Stay logged in on this device").click()
        page.get_by_role("button", name="Login").click()

        # --- Navigation to Course Master ---
        course_category_svg = page.locator(
            "//a[@class='cm-menu-item cm-active']//*[name()='svg']"
        ).first
        course_category_svg.wait_for(state="visible", timeout=10000)
        course_category_svg.click()

        page.get_by_role("link", name="Course Category").click()

        # --- Navigate to Courses Tab ---
        page.get_by_role("button", name="Course").click()

        # --- Clean & Dynamic Course Deletion Code ---
        target_course_name = "Primary School - Class 2"

        # 3. Locate the targeted element using the customized aria-label strategy
        delete_icon = page.locator(f"span[aria-label='Delete course \"{target_course_name}\"'] button.action-btn svg")

        # 4. Fire the click interaction on the delete trash icon
        delete_icon.click()

        # 5. Handle modal confirmations ("Yes" -> "OK")
        page.get_by_role("button", name="Yes").click()
        page.get_by_role("button", name="OK").click()

    except Exception as e:
        print(f"An error occurred during execution: {e}")

    finally:
        # 6. Stop Tracing and Export the zip file
        context.tracing.stop(path="trace.zip")
        import os

        # Put this line inside your 'finally:' block right after context.close()
        print(
            f"🎥 Your video is saved here: {os.path.abspath('videos/')}"
        )

        # 7. Close Context & Browser (This strictly finalizes and writes your video file)
        context.close()
        browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)