import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# ======================================================
# FIXTURE
# ======================================================
@pytest.fixture
def driver():

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.maximize_window()

    yield driver

    driver.quit()


# ======================================================
# TEST CASE
# ======================================================
def test_create_institute(driver):

    wait = WebDriverWait(driver, 20)

    # ======================================================
    # LOGIN
    # ======================================================
    driver.get("https://tranquil-truffle-2a8000.netlify.app/")

    username = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//input[@placeholder='college.admin@jozuna.com']"
            )
        )
    )

    username.send_keys("Kalpana@yopmail.com")

    password = driver.find_element(
        By.XPATH,
        "//input[@placeholder='Enter password']"
    )

    password.send_keys("Kal@2026")

    toggle_button = driver.find_element(
        By.XPATH,
        "//input[@id='stayLoggedIn']"
    )

    toggle_button.click()

    login_button = driver.find_element(
        By.XPATH,
        "//button[normalize-space()='Login']"
    )

    login_button.click()

    time.sleep(5)

    # ======================================================
    # OPEN INSTITUTE MASTER
    # ======================================================

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

    institute_master = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[normalize-space()='Institute Master']"
            )
        )
    )

    institute_master.click()

    time.sleep(7)

    # ======================================================
    # CLICK CREATE INSTITUTE
    # ======================================================

    create_institute = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[normalize-space()='Create Institute']"
            )
        )
    )

    create_institute.click()

    # ======================================================
    # SELECT TRUST
    # ======================================================

    dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(.,'Select')]"
            )
        )
    )

    dropdown.click()

    option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[normalize-space()='JOZUNA TRUSTS']"
            )
        )
    )

    option.click()

    time.sleep(3)

    # ======================================================
    # ENTER CODE
    # ======================================================

    code_input = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//input[@placeholder='Enter code']"
            )
        )
    )

    code_input.clear()
    code_input.send_keys("9217")

    # ======================================================
    # ENTER SHORT NAME
    # ======================================================

    short_name_input = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//input[@placeholder='Enter short name']"
            )
        )
    )

    short_name_input.clear()
    short_name_input.send_keys("SSCE")

    # ======================================================
    # ENTER INSTITUTION NAME
    # ======================================================

    inst_name_input = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//input[@placeholder='Enter institution name']"
            )
        )
    )

    inst_name_input.clear()

    inst_name_input.send_keys(
        "Sree Sowdambika College of Engineering"
    )

    # ======================================================
    # ENTER START ROLL NUMBER
    # ======================================================

    roll_input = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//input[@placeholder='Enter start roll number']"
            )
        )
    )

    roll_input.clear()
    roll_input.send_keys("1")

    driver.execute_script(
        "arguments[0].scrollIntoView(true);",
        roll_input
    )

    time.sleep(1)

    # ======================================================
    # ENTER TELEPHONE
    # ======================================================

    phone_input = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//input[@placeholder='Enter telephone']"
            )
        )
    )

    phone_input.clear()
    phone_input.send_keys("123456789")

    # ======================================================
    # ENTER ADDRESS
    # ======================================================

    address_input = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//textarea[@placeholder='Enter address']"
            )
        )
    )

    address_input.clear()

    address_input.send_keys(
        "Chettikurichi, APK"
    )

    # ======================================================
    # SELECT STATE
    # ======================================================

    dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(.,'Select')]"
            )
        )
    )

    dropdown.click()

    option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[normalize-space()='Andaman and Nicobar Islands']"
            )
        )
    )

    option.click()

    # ======================================================
    # ENTER CITY
    # ======================================================

    city_input = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//input[contains(@placeholder,'Enter city')]"
            )
        )
    )

    city_input.clear()
    city_input.send_keys("APK")

    # ======================================================
    # ENTER PINCODE
    # ======================================================

    pincode_input = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//input[contains(@placeholder,'Enter pincode')]"
            )
        )
    )

    pincode_input.clear()
    pincode_input.send_keys("628134")

    # ======================================================
    # CLICK SAVE
    # ======================================================

    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )

    save_btn = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[normalize-space()='Save']"
            )
        )
    )

    save_btn.click()

    # ======================================================
    # CLICK YES
    # ======================================================

    yes_btn = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[normalize-space()='Yes']"
            )
        )
    )

    yes_btn.click()

    print("Institute created successfully")

    time.sleep(5)