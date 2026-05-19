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
def test_trust_master(driver):

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

    time.sleep(10)

    # ======================================================
    # CREATE TRUST
    # ======================================================
    wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[normalize-space()='Create Trust']"
            )
        )
    ).click()

    time.sleep(3)

    # Trust Code
    wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//input[@placeholder='Enter Trust Code']"
            )
        )
    ).send_keys("TRUST001")

    # Trust Name
    wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//input[@placeholder='Enter Trust Name']"
            )
        )
    ).send_keys("ABC Educational Trust")

    # Upload Logo
    upload = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//input[@type='file']"
            )
        )
    )

    upload.send_keys(
        r"C:\Users\kaviy\Downloads\Gemini_Generated_Image_os3jhpos3jhpos3j.png"
    )

    time.sleep(3)

    # Click Save
    wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[normalize-space()='Save']"
            )
        )
    ).click()
    time.sleep(10)
    # Click Yes
    yes_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(text(),'Yes')]"
            )
        )
    )

    yes_button.click()
    time.sleep(15)
    # ======================================================
    # HANDLE OK POPUP
    # ======================================================
    ok_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[normalize-space()='OK' or normalize-space()='Ok']"
            )
        )
    )

    ok_button.click()

    time.sleep(5)
    driver.close()


