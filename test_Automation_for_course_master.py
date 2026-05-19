import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# ================= FIXTURE ADDED =================
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


# ================= YOUR SCRIPT (NO FLOW CHANGED) =================
def test_course_category(driver):

    # Launch Chrome is already handled by fixture

    # Wait object
    wait = WebDriverWait(driver, 10)

    # Open login page
    driver.get("https://tranquil-truffle-2a8000.netlify.app/")

    # Enter Username
    username = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='college.admin@jozuna.com']")
        )
    )
    username.send_keys("Kalpana@yopmail.com")

    # Enter Password
    password = driver.find_element(
        By.XPATH, "//input[@placeholder='Enter password']"
    )
    password.send_keys("Kal@2026")

    # Click Toggle Button
    toggle_button = driver.find_element(
        By.XPATH, "//input[@id='stayLoggedIn']"
    )
    toggle_button.click()

    # Click Login Button
    login_button = driver.find_element(
        By.XPATH, "//button[normalize-space()='Login']"
    )
    login_button.click()

    time.sleep(5)

    institute_logo = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[@href='/dashboard/course-master']//*[name()='svg']"
            )
        )
    )

    institute_master = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[@class='cm-menu-item cm-active']"
            )
        )
    )

    institute_master.click()
    time.sleep(2)

    institute_master = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[@href='/dashboard/course-master']"
            )
        )
    )

    institute_master.click()
    time.sleep(7)

    create_institute = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[normalize-space()='Course Category']"
            )
        )
    )

    # 1. Click NEW CATEGORY
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='New Category']")
    )).click()

    # 2. Enter Category Code
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Enter Category Code']")
    )).send_keys("CAT007")

    # 3. Enter Category Name
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Enter Category Name']")
    )).send_keys("Arts and Science")

    # 4. Select NO radio button
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@value='false']")
    )).click()

    # 5. Click SAVE
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Save']")
    )).click()

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Yes']")
    )).click()

    wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         "//body/div[@id='root']/div[@class='cm-container']/div[@class='cm-content']/div[@class='main-content']/div[@class='course-master-content']/div/div/div[@class='table-outer-container']/div[@class='table-wrapper']/div[@class='table-card fit-3-cols']/div[@class='table-body']/div[7]/div[3]/div[1]/button[1]//*[name()='svg']")
    )).click()

    # 3. Enter Category Name
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Enter Category Name']")
    )).clear()

    driver.find_element(
        By.XPATH,
        "//input[@placeholder='Enter Category Name']"
    ).send_keys("Updated Category")

    # 4. Select NO radio button
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@value='false']")
    )).click()

    # 5. Click UPDATE
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Update']")
    )).click()

    # 6. Click YES
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Yes']")
    )).click()

    # delete icon
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[contains(@aria-label,'Delete category')]//button")
    )).click()

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Yes']")
    )).click()