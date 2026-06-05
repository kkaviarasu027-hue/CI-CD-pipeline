import re
import random
from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:


    # BROWSER SETUP

    browser = playwright.chromium.launch(
        headless=False
    )

    context = browser.new_context()

    page = context.new_page()


    # OPEN WEBSITE

    page.goto(
        "https://gentle-lebkuchen-912cc7.netlify.app/"
    )

    page.wait_for_load_state("networkidle")

   # NEGATIVE LOGIN

    page.get_by_role(
        "textbox",
        name="college.admin@jozuna.com"
    ).fill("kalpana@gmail.com")

    page.get_by_role(
        "textbox",
        name="Enter password"
    ).fill("ksl@2028K")

    page.get_by_role(
        "checkbox",
        name="Stay logged in on this device"
    ).check()

    page.get_by_role(
        "button",
        name="Login"
    ).click()

    # Error Popup
    try:
        page.get_by_role(
            "button",
            name="OK"
        ).click(timeout=5000)

        print("Negative Login Popup Closed")

    except:
        print("Negative Login Popup Not Found")

    print("Negative Login Passed")


    # POSITIVE LOGIN

    page.get_by_role(
        "textbox",
        name="college.admin@jozuna.com"
    ).fill("kalpana@yopmail.com")

    page.get_by_role(
        "textbox",
        name="Enter password"
    ).fill("Kal@2026")

    page.get_by_role(
        "button",
        name="Login"
    ).click()

    page.wait_for_load_state("networkidle")

    print("Positive Login Passed")


    ################### TRUST CREATE

    page.wait_for_timeout(3000)

    page.get_by_role("button", name="All Status arrow").click()
    page.get_by_text("Mapped Institutions", exact=True).click()
    page.get_by_role("button", name="Mapped Institutions arrow").click()
    page.get_by_text("Unmapped Institutions").click()
    page.get_by_role("textbox", name="Search Trusts...").click()
    page.get_by_role("textbox", name="Search Trusts...").fill("jozuna ")
    page.get_by_role("textbox", name="Search Trusts...").fill("")
    page.get_by_role("button", name="Edit Trust").nth(1).click()
    page.get_by_role("button", name="Update").click()
    page.get_by_role("button", name="Yes").click()
    page.get_by_role("button", name="Ok").click()
    page.locator(".table-cell > div > .toggle-switch > .toggle-slider").first.click()
    page.get_by_role("button", name="Yes").click()
    page.get_by_role("button", name="Ok").click()
    page.locator("div:nth-child(5) > div:nth-child(5) > div").click()
    page.get_by_role("button", name="Delete Trust").nth(4).click()
    page.get_by_role("button", name="Yes").click()
    page.get_by_role("button", name="Ok").click()

    page.get_by_role(
        "button",
        name="Create Trust"
    ).click()

    # Dynamic Trust Code
    trust_code = f"T{random.randint(100, 999)}"

    # Dynamic Trust Name
    trust_name = f"JOZUNA TRUST {random.randint(100, 999)}"

    page.get_by_role(
        "textbox",
        name="Enter Trust Code"
    ).fill(trust_code)

    page.get_by_role(
        "textbox",
        name="Enter Trust Name"
    ).fill(trust_name)

    # Upload Logo
    page.locator(
        "input[type='file']"
    ).set_input_files(
        r"C:\Users\91636\Downloads\jozuna\selenium\logo.jpg"
    )

    # Save Trust
    page.get_by_role(
        "button",
        name="Save"
    ).click()

    # Confirm Save
    page.get_by_role(
        "button",
        name="Yes"
    ).click()

    # Success Popup
    try:

        page.get_by_role(
            "button",
            name=re.compile(r"ok", re.IGNORECASE)
        ).click(timeout=5000)

    except:
        print("Trust Success Popup Not Found")

    print("Trust Created Successfully")

    page.wait_for_timeout(8000)


    ######################OPEN INSTITUTE MASTER PAGE

    page.goto(
        "https://gentle-lebkuchen-912cc7.netlify.app/dashboard/institute-master"
    )

    page.wait_for_load_state("networkidle")

    page.wait_for_timeout(5000)

    print("Institute Master Opened")

    page.get_by_role("button", name="Course Association").nth(1).click()
    page.locator("div").filter(has_text=re.compile(r"^Select$")).first.click()
    page.locator("div").filter(has_text=re.compile(r"^Engineering College$")).click()
    page.locator("div").filter(has_text=re.compile(r"^Select$")).first.click()
    page.locator("div").filter(has_text=re.compile(r"^UNDER GRADUATE$")).click()
    page.get_by_role("button", name="Save").click()
    page.locator("div").filter(has_text=re.compile(r"^Select$")).nth(1).click()
    page.locator("div").filter(has_text=re.compile(r"^B\.TECH$")).nth(1).click()
    page.get_by_role("button", name="Save").click()
    page.get_by_role("button", name="Yes").click()
    page.get_by_role("button", name="OK").click()
    page.get_by_role("button", name="Back To List").click()

    page.get_by_role("button").nth(3).click()
    page.get_by_role("button", name="Yes").click()
    page.get_by_role("button", name="Ok").click()
    page.get_by_role("button", name="Edit").first.click()
    page.get_by_role("textbox", name="Enter institution name").click()
    page.get_by_role("textbox", name="Enter institution name").fill("SethuRAM")
    page.get_by_role("button", name="Update").click()
    page.get_by_role("button", name="Yes").click()
    page.get_by_role("button", name="Back").click()
    page.get_by_role("textbox", name="Search institutions...").click()
    page.get_by_role("textbox", name="Search institutions...").fill("DIR")

    # CREATE INSTITUTE

    page.get_by_role(
        "button",
        name="Create Institute"
    ).click()

    page.wait_for_timeout(3000)


    # TRUST DROPDOWN

    page.get_by_role(
        "button",
        name=re.compile(r"select trust", re.IGNORECASE)
    ).click()

    page.wait_for_timeout(3000)

    # Use Stable Existing Trust
    page.get_by_text(
        "JOZUNA TRUSTs",
        exact=True
    ).click()

    print("Default Trust Selected Successfully")


    # INSTITUTE DETAILS

    institute_code = str(
        random.randint(400, 999)
    )

    page.get_by_role(
        "textbox",
        name="Enter code"
    ).fill(institute_code)

    page.get_by_role(
        "textbox",
        name="Enter short name"
    ).fill("VJTS")

    institute_name = (
        f"Vela Jozuna Technology Institute "
        f"{random.randint(1, 999)}"
    )

    page.get_by_role(
        "textbox",
        name="Enter institution name"
    ).fill(institute_name)

    page.get_by_role(
        "textbox",
        name="Enter start roll number"
    ).fill("6001")

    page.get_by_role(
        "textbox",
        name="Enter telephone"
    ).fill("5638293867")

    page.get_by_role(
        "textbox",
        name="Enter address"
    ).fill("Kamaraj Street, GH Road")


    # STATE

    page.get_by_role(
        "button",
        name=re.compile(
            r"select state",
            re.IGNORECASE
        )
    ).click()

    page.wait_for_timeout(2000)

    page.get_by_text(
        "Tamil Nadu",
        exact=True
    ).click()

    # City
    page.get_by_role(
        "textbox",
        name="Enter city"
    ).fill("Gobi")

    # Pincode
    page.get_by_role(
        "textbox",
        name="Enter pincode"
    ).fill("638456")


    # SAVE INSTITUTE

    page.get_by_role(
        "button",
        name="Save"
    ).click()

    page.wait_for_timeout(2000)

    page.get_by_role(
        "button",
        name="Yes"
    ).click()

    try:

        page.get_by_role(
            "button",
            name=re.compile(r"ok", re.IGNORECASE)
        ).click(timeout=5000)

    except:
        print("Institute Success Popup Not Found")

    print("Institute Created Successfully")



    ################ OPEN COURSE CATEGORY PAGE

    page.goto(
        "https://gentle-lebkuchen-912cc7.netlify.app/dashboard/course-master"
    )

    page.wait_for_load_state("domcontentloaded")

    page.wait_for_timeout(5000)

    print("Course Page Opened")

    page.locator("div:nth-child(6) > div:nth-child(3) > .actions > span > .action-btn").click()
    page.get_by_role("button", name="Yes").click()
    page.get_by_role("button", name="Edit").nth(4).click()
    page.get_by_role("textbox", name="Enter Category Name").click()
    page.get_by_role("textbox", name="Enter Category Name").press("ControlOrMeta+A")
    page.get_by_role("textbox", name="Enter Category Name").fill("EDUCATION OF LAW")
    page.get_by_role("button", name="Update").click()
    page.get_by_role("button", name="Yes").click()

    # Open Category Tab
    page.get_by_role(
        "button",
        name="Category",
        exact=True
    ).click()

    # Create Category
    page.get_by_role(
        "button",
        name="New Category"
    ).click()

    page.get_by_role(
        "textbox",
        name="Enter Category Code"
    ).fill("C0010")

    page.get_by_role(
        "textbox",
        name="Enter Category Name"
    ).fill("FASHION DESIGNING")

    page.get_by_role(
        "radio",
        name="No"
    ).check()

    page.get_by_role(
        "button",
        name="Save"
    ).click()

    page.get_by_role(
        "button",
        name="Yes"
    ).click()

    print("Category Created Successfully")

    # Open Course Tab
    page.get_by_role(
        "button",
        name="Course",
        exact=True
    ).click()

    # Create Course
    page.get_by_role(
        "button",
        name="New Course"
    ).click()

    page.locator(
        "div"
    ).filter(
        has_text=re.compile(r"^Select Category$")
    ).nth(1).click()

    page.get_by_text(
        "FASHION DESIGNING"
    ).click()

    page.get_by_role(
        "textbox",
        name="Enter Course Code"
    ).fill("22FAD01")

    page.get_by_role(
        "textbox",
        name="Enter Course Name"
    ).fill("FASHION MERCHANDISING")

    page.get_by_role(
        "textbox",
        name="e.g. 1",
        exact=True
    ).fill("6")

    page.get_by_role(
        "textbox",
        name="e.g. 3"
    ).fill("3")

    page.get_by_role(
        "textbox",
        name="e.g. 18"
    ).fill("19")

    page.get_by_role(
        "button",
        name="Save"
    ).click()

    page.get_by_role(
        "button",
        name="Yes"
    ).click()

    print("Course Created Successfully")

    page.get_by_text("All Categories").click()
    page.get_by_text("UNDER GRADUATE").first.click()
    page.locator("div").filter(has_text=re.compile(r"^UNDER GRADUATE$")).nth(3).click()
    page.get_by_text("All Categories").click()
    page.get_by_role("textbox", name="Search Course...").click()
    page.get_by_role("textbox", name="Search Course...").fill("UN")


    ######################### OPEN DEPARTMENT MASTER PAGE
    page.goto(
        "https://gentle-lebkuchen-912cc7.netlify.app/dashboard/department-master"
    )

    page.wait_for_load_state("domcontentloaded")

    page.wait_for_timeout(5000)

    print("Department Master Page Opened")


    # CREATE DEPARTMENT

    page.get_by_role(
        "button",
        name="Create Department"
    ).click()

    page.wait_for_timeout(3000)


    # DEPARTMENT DETAILS

    department_code = (
        f"FAD{random.randint(10, 99)}"
    )

    department_name = (
        f"FASHION DESIGNING "
        f"{random.randint(1, 999)}"
    )

    department_number = str(
        random.randint(100, 999)
    )

    # Department Code
    page.get_by_role(
        "textbox",
        name="Enter Department Code"
    ).fill(department_code)

    # Department Name
    page.get_by_role(
        "textbox",
        name="Enter Department Name"
    ).fill(department_name)

    # Department Number
    page.get_by_role(
        "textbox",
        name="Enter Department Number"
    ).fill(department_number)


    # SAVE DEPARTMENT

    page.get_by_role(
        "button",
        name="Save"
    ).click()

    page.wait_for_timeout(2000)

    page.get_by_role(
        "button",
        name="Yes"
    ).click()

    # Success Popup
    try:

        page.get_by_role(
            "button",
            name=re.compile(r"ok", re.IGNORECASE)
        ).click(timeout=5000)

    except:
        print("Department Success Popup Not Found")

    print("Department Created Successfully")


    # FILTER STATUS

    page.get_by_role(
        "button",
        name=re.compile(r"all status", re.IGNORECASE)
    ).click()

    page.wait_for_timeout(2000)

    page.get_by_text(
        "Active",
        exact=True
    ).click()

    print("Active Filter Selected")

    page.wait_for_timeout(2000)

    page.get_by_role(
        "button",
        name=re.compile(r"active", re.IGNORECASE)
    ).click()

    page.wait_for_timeout(2000)

    page.get_by_text(
        "Inactive",
        exact=True
    ).click()

    print("Inactive Filter Selected")

    page.wait_for_timeout(2000)

    page.get_by_role(
        "button",
        name=re.compile(r"inactive", re.IGNORECASE)
    ).click()

    page.wait_for_timeout(2000)

    page.get_by_text(
        "All Status",
        exact=True
    ).click()

    print("All Status Filter Selected")

    # SEARCH DEPARTMENT

    page.get_by_role(
        "textbox",
        name="Search Departments..."
    ).fill("FAS")

    print("Department Search Completed")

    page.wait_for_timeout(5000)

    #################### PROFILE SECTION

    page.goto(
        "https://gentle-lebkuchen-912cc7.netlify.app/dashboard"
    )

    page.wait_for_load_state("networkidle")

    page.wait_for_timeout(5000)

    print("Dashboard Opened")


    # OPEN PROFILE DROPDOWN

    try:

        page.get_by_text(
            re.compile(r"JMJulio Morgan", re.IGNORECASE)
        ).click()

    except:

        page.locator(
            ".lucide.lucide-chevron-down"
        ).first.click()

    page.wait_for_timeout(3000)

    print("Profile Dropdown Opened")

    # OPEN MY PROFILE
    page.get_by_text(
        "My Profile",
        exact=True
    ).click()

    page.wait_for_load_state("networkidle")

    page.wait_for_timeout(5000)

    print("My Profile Opened")


    # PROFILE PAGE ACTIONS

    try:

        page.get_by_role(
            "button",
            name="Edit"
        ).click()

        print("Edit Button Clicked")

    except:

        print("Edit Button Not Found")

    page.wait_for_timeout(3000)


    # NOTIFICATION ICON

    try:

        page.locator(
            ".lucide.lucide-bell"
        ).click()

        print("Notification Opened")

    except:

        print("Notification Icon Not Found")

    page.wait_for_timeout(3000)


    # OPEN CHATBOT

    try:

        page.get_by_role(
            "img",
            name="chatbot_icon"
        ).click()

        print("Chatbot Opened")

    except:

        print("Chatbot Icon Not Found")

    page.wait_for_timeout(5000)


# CHATBOT - ATTENDANCE

    try:

        page.get_by_role(
            "button",
            name="Attendance"
        ).click()

        page.wait_for_timeout(2000)

        page.get_by_role(
            "button",
            name="chatbot-send"
        ).click()

        print("Attendance Prompt Sent")

    except:

        print("Attendance Prompt Failed")

    page.wait_for_timeout(4000)


    # NEW CHAT
    try:

        page.get_by_role(
            "button",
            name=re.compile(r"new chat", re.IGNORECASE)
        ).click()

        print("New Chat Opened")

    except:

        print("New Chat Button Not Found")

    page.wait_for_timeout(3000)

    # SUMMARIZE BUTTON

    try:

        page.get_by_role(
            "button",
            name="Summarize"
        ).click()

        page.wait_for_timeout(2000)

        page.get_by_role(
            "button",
            name="chatbot-send"
        ).click()

        print("Summarize Prompt Sent")

    except:

        print("Summarize Failed")

    page.wait_for_timeout(4000)

    # CUSTOM CHAT MESSAGE

    try:

        chat_box = page.get_by_role(
            "textbox",
            name=re.compile(
                r"What would you like to create",
                re.IGNORECASE
            )
        )

        chat_box.fill("mark")

        page.get_by_role(
            "button",
            name="chatbot-send"
        ).click()

        print("Custom Chat Message Sent")

    except:

        print("Custom Chat Message Failed")

    page.wait_for_timeout(5000)

 ##################### DEPARTMENT ASSOCIATE
    page.goto(
        "https://gentle-lebkuchen-912cc7.netlify.app/dashboard/department-associate"
    )

    page.wait_for_load_state("networkidle")

    page.wait_for_timeout(5000)

    print("Department Associate Opened")

    # SELECT ENGINEERING COLLEGE
    # Open Dropdown
    page.locator(
        ".arrow"
    ).first.click()

    page.wait_for_timeout(2000)

    # Select Institution
    page.locator(
        ".dropdown-item"
    ).filter(
        has_text="Engineering College"
    ).first.click()

    print("Engineering College Selected")

    page.wait_for_timeout(3000)

    # SELECT GLOBAL ENGINEERING COLLEGE

    # Open Dropdown Again
    page.locator(
        ".arrow"
    ).first.click()

    page.wait_for_timeout(2000)

    # Select Institution
    page.locator(
        ".dropdown-item"
    ).filter(
        has_text="Global Engineering College"
    ).first.click()

    print("Global Engineering College Selected")

    page.wait_for_timeout(3000)


    # SELECT HYDERABAD ARTS SCHOOL

    # Open Dropdown Again
    page.locator(
        ".arrow"
    ).first.click()

    page.wait_for_timeout(2000)

    # Select Institution
    page.locator(
        ".dropdown-item"
    ).filter(
        has_text="Hyderabad Arts School"
    ).first.click()

    print("Hyderabad Arts School Selected")

    page.wait_for_timeout(3000)


    # RESET TO ALL INSTITUTIONS

    # Open Dropdown Again
    page.locator(
        ".arrow"
    ).first.click()

    page.wait_for_timeout(2000)

    page.locator(
        ".dropdown-item"
    ).filter(
        has_text="All Institutions"
    ).first.click()

    print("All Institutions Selected")

    page.wait_for_timeout(3000)

    # SEARCH MAPPING

    page.get_by_role(
        "textbox",
        name="Search mapping..."
    ).fill("engineer")

    print("Department Associate Search Completed")

    page.wait_for_timeout(5000)
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)